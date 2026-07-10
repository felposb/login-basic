const botao = document.querySelector("#botao");

botao.addEventListener("click", () => {
    const email = document.querySelector("#email").value;
    const senha = document.querySelector("#senha").value;

    fetch("http://127.0.0.1:5000/dados", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
        email: email,
        senha: senha
    })
}
)
})