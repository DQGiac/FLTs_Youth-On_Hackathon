window.addEventListener("DOMContentLoaded", (event) => {
    const anh = document.getElementById("upload-anh");
    const useDiv = document.getElementById("use-div");
    const preview = document.getElementById("preview");

    function handleImageUpload() {
        const anh = document.getElementById("upload-anh").files[0];
        if (anh) {
            const reader = new FileReader();
            reader.onload = function (e) {
                const image = new Image();
                image.src = e.target.result;
                image.style.width = "100%";
                image.style.height = "100%";
                image.style.objectFit = "contain";
                preview.innerHTML = "";
                preview.appendChild(image);
                let xhr = new XMLHttpRequest();
                xhr.open("POST", "/save-image");
                xhr.setRequestHeader("Accept", "application/json");
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === 4) {
                        result = (JSON.parse(xhr.responseText)["generated_image"])
                        console.log(result)
                    }
                };
                xhr.send(JSON.stringify({ "image": image }));
            };
            reader.readAsDataURL(anh);
        }
    }

    function displayResults(filename, segments) {
        document.querySelector("#loading-overlay").style.display = "none";
        document.body.classList.remove("loading");
        
    }
    anh.addEventListener("change", handleImageUpload);
    useDiv.addEventListener("click", function (e) {
        e.preventDefault(); // Prevent form submission
        inp = anh.files[0];
        console.log(inp);
        // func(inp);
    });
});