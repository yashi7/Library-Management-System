function validateForm(event) {
    event.preventDefault();
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
    

    errorMessage.textContent = 'Registration successful!';
    errorMessage.style.color="green";

  }
  