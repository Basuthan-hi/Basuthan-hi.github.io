
function open_close(id) {
    var description = document.getElementsByClassName(id)[0];
    if (description.id === 'op') {
        description.id = 'cl';
    } else {
        description.id = 'op';
    }
}