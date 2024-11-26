// scripts.js

// Wait until the DOM is loaded
document.addEventListener('DOMContentLoaded', function () {

    const form = document.querySelector('form');
    const phoneInput = document.querySelector('#Phone');
    const medicalHistoryInput = document.querySelector('#Medical_History');

    form.addEventListener('submit', function(event) {
        // Validate phone number format (10 digits only)
        const phoneRegex = /^[0-9]{10}$/;
        if (!phoneRegex.test(phoneInput.value)) {
            alert('Please enter a valid 10-digit phone number.');
            event.preventDefault();
        }

        // Validate medical history field length (at least 10 characters)
        if (medicalHistoryInput.value.length < 10) {
            alert('Medical history must be at least 10 characters long.');
            event.preventDefault();
        }
    });
});
