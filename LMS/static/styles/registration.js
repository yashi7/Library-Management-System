function validateForm(event) {
    


    const Name = document.getElementById('UserName').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const confirmPassword = document.getElementById('confirmPassword').value.trim();
    const errorMessage = document.getElementById('error-message');
     
    if (UserName === ''|| email === '' || password === '' || confirmPassword === '') {
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
    errorMessage.style.color="green";
    // Here you might add code to submit the form data to a server, etc.
  }
  