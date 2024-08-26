// Handle the form submission using AJAX
document.getElementById("loginForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent the default form submission

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  // Perform an AJAX POST request
  fetch("/api/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username: username, password: password }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Display the response message
      const responseMessage = document.getElementById("responseMessage");
      responseMessage.textContent = data.message;

      // Optionally, clear the form inputs
      document.getElementById("loginForm").reset();
    })
    .catch((error) => {
      console.error("Error:", error);
      document.getElementById("responseMessage").textContent =
        "An error occurred. Please try again.";
    });
});
