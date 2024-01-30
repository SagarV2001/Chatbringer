const passwordInput = document.querySelector('.password-input');
    const cpasswordInput = document.querySelector('.cpassword-input');
    const signupButton = document.querySelector('.signup-button');

    function validatePassword() {
        const password = passwordInput.value;
        const cpassword = cpasswordInput.value;

        if (password.length < 6 || password !== cpassword) {
            signupButton.disabled = true;
        } else {
            signupButton.disabled = false;
        }
    }

passwordInput.addEventListener('input', validatePassword);
cpasswordInput.addEventListener('input', validatePassword);