window.addEventListener("DOMContentLoaded", (event) => {
    const uploadInput = document.getElementById("upload-anh");
    const preview = document.getElementById("preview");
    const useButton = document.getElementById("use-button");
  
    let uploadedFilename = "";
  
    async function handleImageUpload() {
        const file = uploadInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                const image = new Image();
                image.src = e.target.result;
                image.style.width = "100%";
                image.style.height = "100%";
                image.style.objectFit = "contain";
                preview.innerHTML = "";
                preview.appendChild(image);
            };
            reader.readAsDataURL(file);
        }
        if (file) {
            const formData = new FormData();
            formData.append("image", file);
            const response = await fetch("/save-image", {
                method: "POST",
                body: formData
            });
            const result = await response.json();
            uploadedFilename = result["filename"]
        }
    }
  
    async function handleUseButtonClick() {
        let result = ""
        const file = uploadInput.files[0];
        if (file) {
            const formData = new FormData();
            formData.append("image", file);
            const response = await fetch("/ocr", {
                method: "POST",
                body: formData
            });
            result = await response.json();
            console.log(result)
        } else {
            const vanban = document.getElementById("upload-vanban")
            result = vanban.innerHTML;
        }
        const formData = new FormData();
        formData.append("message", result);
        const response = await fetch("/strtell_gen", {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },     
            body: JSON.stringify( {"message": result} )
        });
    }

    uploadInput.addEventListener("change", handleImageUpload);
    useButton.addEventListener("click", handleUseButtonClick);
});