from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, make_response
import os
import json
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token, get_jwt_identity,
    verify_jwt_in_request, set_access_cookies, unset_jwt_cookies,
    set_refresh_cookies, get_jwt, unset_refresh_cookies
)
from functools import wraps
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['JWT_SECRET_KEY'] = 'jwt-super-secret-key'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False  # True yaparsanız sadece HTTPS'te çalışır
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False  # İsterseniz True yapabilirsiniz

# Oturumun süresi (ör: 10 dakika)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)  # Kısa süreli access token
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=7)    # Refresh token süresi

jwt = JWTManager(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Maksimum dosya boyutu: 10 MB
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB

USERS_FILE = 'users.json'
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as f:
        json.dump({}, f)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_users():
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

# Cookie'den JWT doğrulama için decorator
def jwt_required_cookie(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except Exception:
            flash("Lütfen giriş yapınız.")
            return redirect(url_for('login'))
        return fn(*args, **kwargs)
    return wrapper

@app.route('/')
@jwt_required_cookie
def index():
    email = get_jwt_identity()
    user_folder = os.path.join(app.config['UPLOAD_FOLDER'], email)
    os.makedirs(user_folder, exist_ok=True)
    files = os.listdir(user_folder)
    return render_template('dashboard.html', files=files)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']

        users = load_users()
        if email in users:
            flash('Bu e-posta zaten kayıtlı.')
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password)
        users[email] = {
            'name': name,
            'surname': surname,
            'phone': phone,
            'password': hashed_password
        }
        save_users(users)
        flash('Kayıt başarılı. Giriş yapabilirsiniz.')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users = load_users()
        if email not in users:
            flash('Kullanıcı bulunamadı')
            return render_template('login.html')
        if check_password_hash(users[email]['password'], password):
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)
            resp = make_response(redirect(url_for('index')))
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            return resp
        flash('Hatalı giriş bilgisi')
    return render_template('login.html')

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('login')))
    unset_jwt_cookies(resp)
    unset_refresh_cookies(resp)
    return resp

@app.route('/refresh', methods=['POST'])
def refresh():
    try:
        verify_jwt_in_request(refresh=True)
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        resp = make_response({'msg': 'Token yenilendi'})
        set_access_cookies(resp, access_token)
        return resp
    except Exception:
        return {'msg': 'Refresh token geçersiz'}, 401

@app.route('/upload', methods=['POST'])
@jwt_required_cookie
def upload_file():
    email = get_jwt_identity()
    if 'file' not in request.files:
        flash('Dosya seçilmedi')
        return redirect(url_for('index'))

    files = request.files.getlist('file')
    if not files or files[0].filename == '':
        flash('Dosya seçilmedi.', 'error')
        return redirect(url_for('dashboard'))

    for file in files:
        if file and allowed_file(file.filename):
            user_folder = os.path.join(app.config['UPLOAD_FOLDER'], email)
            os.makedirs(user_folder, exist_ok=True)
            filename = secure_filename(file.filename)
            filepath = os.path.join(user_folder, filename)
            if os.path.exists(filepath):
                flash('Aynı isimde bir dosya zaten mevcut. Lütfen farklı bir dosya adı kullanın.')
                return redirect(url_for('index'))
            file.save(filepath)
        else:
            flash(f"{file.filename} geçersiz dosya türü.", 'error')

    flash('Dosya(lar) başarıyla yüklendi.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/delete/<filename>')
@jwt_required_cookie
def delete_file(filename):
    email = get_jwt_identity()
    user_folder = os.path.join(app.config['UPLOAD_FOLDER'], email)
    filepath = os.path.join(user_folder, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        flash(f'{filename} silindi')
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
@jwt_required_cookie
def uploaded_file(filename):
    email = get_jwt_identity()
    user_folder = os.path.join(app.config['UPLOAD_FOLDER'], email)
    return send_from_directory(user_folder, filename)

@app.route('/delete_account', methods=['POST'])
@jwt_required_cookie
def delete_account():
    email = get_jwt_identity()
    users = load_users()
    # Kullanıcıyı users.json'dan sil
    if email in users:
        del users[email]
        save_users(users)
    # Kullanıcının dosya klasörünü sil
    user_folder = os.path.join(app.config['UPLOAD_FOLDER'], email)
    if os.path.exists(user_folder):
        import shutil
        shutil.rmtree(user_folder)
    resp = make_response(redirect(url_for('signup')))
    unset_jwt_cookies(resp)
    flash('Hesabınız ve tüm dosyalarınız silindi.')
    return resp

@app.errorhandler(413)
def request_entity_too_large(error):
    flash('Dosya boyutu 10 MB\'dan büyük olamaz.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)