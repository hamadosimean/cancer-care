document.addEventListener("DOMContentLoaded", function () {
  console.log("App initialized");

  // get current year
  const yearSpan = document.getElementById("current-year");
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }

  const firstName = document.getElementById("first_name");
  const lastName = document.getElementById("last_name");
  const username = document.getElementById("username");

  function updateUsername() {
    if (firstName && lastName && username) {
      username.value = (
        firstName.value.trim() + lastName.value.trim()
      ).toLowerCase();
    }
  }

  if (firstName) firstName.addEventListener("input", updateUsername);
  if (lastName) lastName.addEventListener("input", updateUsername);
});
