document.addEventListener("DOMContentLoaded", function() {
    const inputElements = document.querySelectorAll("input[type=file]");
    inputElements.forEach(function(inputElement) {
        inputElement.addEventListener("change", function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const previewContainer = inputElement.parentElement.querySelector('.preview-container');
                    let previewImage = previewContainer.querySelector('#image-preview');
                    if (!previewImage) {
                        previewImage = document.createElement("img");
                        previewImage.id = "image-preview";
                        previewContainer.appendChild(previewImage);
                    }
                    previewImage.src = e.target.result;

                    let cropButton = previewContainer.querySelector('#crop-button');
                    if (!cropButton) {
                        cropButton = document.createElement('button');
                        cropButton.id = 'crop-button';
                        cropButton.textContent = 'Crop';
                        cropButton.classList.add('button');
                        previewContainer.appendChild(cropButton);

                        cropButton.addEventListener('click', function() {
                            const cropper = new Cropper(previewImage, {
                                aspectRatio: 16 / 9,
                                viewMode: 1,
                                autoCropArea: 0.5,
                            });

                            cropButton.textContent = 'Save Crop';
                            cropButton.addEventListener('click', function() {
                                const canvas = cropper.getCroppedCanvas();
                                previewImage.src = canvas.toDataURL('image/jpeg');
                                cropper.destroy();
                                cropButton.remove();
                            }, { once: true });
                        });
                    }
                };
                reader.readAsDataURL(file);
            }
        });
    });
});
