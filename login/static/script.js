

const form = document.getElementById('signupForm')
form.addEventListener('submit', function (e) {
    e.preventDefault();

    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('cpassword').value;
    var errorMessages = [];

    if (password.length < 8) {
        errorMessages.push("Password must be at least 8 characters long.");
    }

    if (!/[A-Z]/.test(password)) {
        errorMessages.push("Password must contain at least one uppercase letter.");
    }

    if (!/[!@#$%^&*(),.?\":{}|<>]/.test(password)) {
        errorMessages.push("Password must contain at least one special character.");
    }

    if (!/\d/.test(password)) {
        errorMessages.push("Password must contain at least one number.");
    }

    if (password !== confirmPassword) {
        errorMessages.push("Passwords do not match.");
    }

    var errorDiv = document.getElementById('errorMessages');
    if (errorMessages.length > 0) {
        errorDiv.innerHTML = errorMessages.join('<br>');
    } else {
        errorDiv.innerHTML = '';
        this.submit();
    }
});