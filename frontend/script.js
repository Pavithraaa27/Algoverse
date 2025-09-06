// =======================
// Login Form Validation
// =======================
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.querySelector('.login-card form');

    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent default form submission

            const usernameInput = document.getElementById('username');
            const emailInput = document.getElementById('email');
            const passwordInput = document.getElementById('password');

            let isValid = true;

            // Simple validation example
            if (usernameInput.value.trim() === '') {
                alert('Please enter your username.');
                usernameInput.focus();
                isValid = false;
            } else if (emailInput.value.trim() === '') {
                alert('Please enter your email address.');
                emailInput.focus();
                isValid = false;
            } else if (!/\S+@\S+\.\S+/.test(emailInput.value)) { // Basic email regex
                alert('Please enter a valid email address.');
                emailInput.focus();
                isValid = false;
            } else if (passwordInput.value.trim() === '') {
                alert('Please enter your password.');
                passwordInput.focus();
                isValid = false;
            }

            if (isValid) {
                alert('Form submitted successfully! (This is a demo, no actual submission)');
                // Here you would typically send data to a server:
                // loginForm.submit();
            }
        });
    }
});

// =======================
// Landing Page - Product Search
// =======================
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector('.search-bar input');
    const products = document.getElementsByClassName('product');

    if (searchInput) {
        searchInput.addEventListener('input', (event) => {
            let input = event.target.value.toLowerCase();

            for (let i = 0; i < products.length; i++) {
                let item = products[i].innerText.toLowerCase();
                products[i].style.display = item.includes(input) ? "" : "none";
            }
        });
    }
});
