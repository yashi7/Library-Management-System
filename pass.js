function recoverCredentials(event) {
    event.preventDefault();

    const email = document.getElementById('email').value.trim();
    const errorMessage = document.getElementById('error-message');
    const successMessage = document.getElementById('success-message');

    // Perform validation (e.g., check if the email exists in the database)
    if (email === '') {
        errorMessage.textContent = 'Please enter your email.';
        successMessage.textContent = '';
        return;
    }

    // Simulating a successful recovery message with a delay
    setTimeout(() => {
        successMessage.textContent = `An email with instructions has been sent to ${email}.`;
        errorMessage.textContent = '';
    }, 1500);
}
