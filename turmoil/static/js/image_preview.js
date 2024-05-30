document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("input[type=file]").forEach(function(inputElement) {
        inputElement.addEventListener("change", function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const previewImage = document.getElementById("image-preview");
                    if (previewImage) {
                        previewImage.src = e.target.result;
                    } else {
                        const img = document.createElement("img");
                        img.id = "image-preview";
                        img.src = e.target.result;
                        img.style.maxWidth = "100%";
                        inputElement.parentElement.appendChild(img);
                    }
                };
                reader.readAsDataURL(file);
            }
        });
    });
});
