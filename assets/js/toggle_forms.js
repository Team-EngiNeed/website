// toggle_forms.js
document.addEventListener("DOMContentLoaded", () => {
    const tabs = document.querySelectorAll(".tab-btn");
    const forms = document.querySelectorAll(".auth-form");

    tabs.forEach(tab => {
        tab.addEventListener("click", () => {
            tabs.forEach(t => t.classList.remove("active"));
            forms.forEach(f => f.classList.remove("active"));

            tab.classList.add("active");
            document.getElementById(tab.dataset.tab).classList.add("active");
        });
    });

    // Password toggle for login and register
    const showPasswordLogin = document.getElementById("showPasswordLogin");
    const loginPasswordField = document.querySelector("#login-form input[type='password']");
    if (showPasswordLogin && loginPasswordField) {
        showPasswordLogin.addEventListener("change", () => {
            loginPasswordField.type = showPasswordLogin.checked ? "text" : "password";
        });
    }

    const showPasswordRegister = document.getElementById("showPasswordRegister");
    const registerPasswordField = document.querySelector("#register-form input[type='password']");
    if (showPasswordRegister && registerPasswordField) {
        showPasswordRegister.addEventListener("change", () => {
            registerPasswordField.type = showPasswordRegister.checked ? "text" : "password";
        });
    }
});
    