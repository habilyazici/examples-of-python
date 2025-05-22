document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    if (uploadForm) {
        uploadForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const files = document.getElementById('fileInput').files;
            if (!files.length) return;

            const progress = document.getElementById('uploadProgress');
            progress.style.display = 'block';
            progress.value = 0;

            const formData = new FormData();
            for (let i = 0; i < files.length; i++) {
                formData.append('file', files[i]);
            }

            const xhr = new XMLHttpRequest();
            xhr.open('POST', uploadForm.action, true);

            xhr.upload.onprogress = function(e) {
                if (e.lengthComputable) {
                    progress.value = (e.loaded / e.total) * 100;
                }
            };
            xhr.onload = function() {
                progress.style.display = 'none';
                if (xhr.status === 200) {
                    window.location.reload();
                } else {
                    alert('Yükleme sırasında hata oluştu.');
                }
            };
            xhr.onerror = function() {
                progress.style.display = 'none';
                alert('Yükleme sırasında hata oluştu.');
            };
            xhr.send(formData);
        });
    }
});


function confirmDeleteAccount() {
    if (confirm("Hesabınızı silmek istediğinize emin misiniz? Bu işlem geri alınamaz.")) {
        document.getElementById('deleteAccountForm').submit();
    }
}