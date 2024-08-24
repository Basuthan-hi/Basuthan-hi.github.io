const description = document.getElementsByClassName('description')[0];
function open_close() {
    if (description.id === 'op') {
        description.id = 'cl';
    } else {
        description.id = 'op';
    }
}