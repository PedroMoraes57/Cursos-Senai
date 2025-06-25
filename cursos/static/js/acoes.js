document.addEventListener("DOMContentLoaded", function () {
    const formInteresse = document.getElementById("form-interesse");

    if (formInteresse) {
        formInteresse.addEventListener("submit", function () {
            setTimeout(function () {
                alert("Seu interesse foi enviado! Obrigado por escolher o SENAI.");
            }, 200);
        });
    }
});