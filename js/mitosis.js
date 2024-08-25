const popup = document.querySelector('.pop') 
const active = document.querySelector('.Virchow')
active.addEventListener('click', () => {
    if (popup.style.display === 'none') {
        popup.style.display = 'block';
    }else {
        popup.style.display = 'none';
    }
})
