window.addEventListener("DOMContentLoaded", (event) => {
    document.getElementById("buttons").addEventListener("click", function (e) {
        e.preventDefault(); // Prevent form submission
        inp = document.getElementById("keys").value;
        console.log(inp);
        func(inp);
    });
    async function func(a) {
        loading = document.getElementById("loading");
        loading.innerHTML = "Hãy đợi, việc này có thể mất từ 10 đến 20 giây...";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", "/askGPT");
        xhr.setRequestHeader("Accept", "application/json");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(JSON.stringify({ "message": a }));
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                console.log(JSON.parse(xhr.responseText)["generated_image"])
                result = document.getElementById("show_image");
                result.src = (JSON.parse(xhr.responseText)["generated_image"])
                loading.innerHTML = "";
            }
        };
    }
});