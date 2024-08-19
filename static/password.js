const eye = document.querySelector('.eye');
const eyebutton = document.querySelector('#eye')
eye.addEventListener('click', function() {
    const passwordInput = document.querySelector('#password');
    if(passwordInput.type === 'password') {
        passwordInput.type = 'text';
        eyebutton.setAttribute('name', 'eye');
    } else {
        passwordInput.type = 'password';
        eyebutton.setAttribute("name", "eye-off");
    }
});