// Selecting DOM elements for menu toggle
const menu = document.querySelector("#mobile-menu");
const menuLinks = document.querySelector(".navbar__menu");

// Toggle the menu
menu.addEventListener("click", function () {
  menu.classList.toggle("is-active");
  menuLinks.classList.toggle("active");
});

document.addEventListener("DOMContentLoaded", function () {
  const passwordField = document.querySelector(
    ".form_password input[type='password']"
  );
  const showPasswordCheckbox = document.getElementById("showPassword");

  // Add an event listener to the checkbox to toggle the password visibility
  if (passwordField && showPasswordCheckbox) {
    showPasswordCheckbox.addEventListener("change", function () {
      if (this.checked) {
        // Show the password
        passwordField.type = "text";
      } else {
        // Hide the password
        passwordField.type = "password";
      }
    });
  }
});
