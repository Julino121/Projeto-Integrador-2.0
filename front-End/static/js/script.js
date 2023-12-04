document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("complete-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        var submitButton = form.querySelector('input[type="submit"]');
        submitButton.disabled = true;

        var formData = new FormData(form);
        var jsonData = {};

        formData.forEach(function (value, key) {
            jsonData[key] = value;
        });
        console.log({ jsonData })

        fetch('http://localhost:80/style_form', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams(jsonData).toString()
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert('Consulta agendada com sucesso!')
        })
        .catch(error => {
            alert('Erro ao realizar agenda!')
        });
    });
});
