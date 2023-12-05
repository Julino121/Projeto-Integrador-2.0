document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("complete-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        // var submitButton = form.querySelector('input[type="submit"]');
        // submitButton.disabled = true;

        var formData = new FormData(form);
        var jsonData = {};

        formData.forEach(function (value, key) {
            jsonData[key] = value;
        });

        const dateObj = new Date(jsonData.date);
        const timeArray = jsonData.time.split(":");
        const hours = timeArray[0];
        const minutes = timeArray[1];

        dateObj.setHours(hours);
        dateObj.setMinutes(minutes);

        jsonData.date = dateObj;

        console.log({ dateObj })

        fetch('http://localhost:3100/appointments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
        })
        .then(response => response.json())
        .then(data => {
            window.location.href = "/front-End/obrigado.html?name=teste"
        })
        .catch(error => {
            alert('Erro ao realizar agenda!')
        });
    });
});
