function validateForm(event) {
  event.preventDefault();

  const Name = document.getElementById('UserName').value.trim();
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value.trim();
  const confirmPassword = document.getElementById('confirmPassword').value.trim();
  const errorMessage = document.getElementById('error-message');
  const formContainer = document.getElementById('registrationContainer');

  if (Name === '' || email === '' || password === '' || confirmPassword === '') {
      errorMessage.textContent = 'All fields are required';
      return;
  }

  if (password !== confirmPassword) {
      errorMessage.textContent = 'Passwords do not match';
      return;
  }

  // Perform further validation (e.g., email format)

  // If all validations pass, you can proceed with form submission or other actions
  errorMessage.textContent = 'Registration successful!';
  errorMessage.style.color = "green";
}
//   // Add slide animation
//   formContainer.classList.add('slide-out');

//   // Additional animation (fadeInOut)
//   errorMessage.style.animation = 'fadeInOut 1s ease';

//   // Here you might add code to submit the form data to a server, etc.
// }

// // Add an event listener for form submission
// document.getElementById('registrationForm').addEventListener('submit', validateForm);

// // Add click event listener to trigger slide-out animation on container click
// document.getElementById('registrationContainer').addEventListener('click', function() {
//   this.classList.toggle('slide-out');
// })
