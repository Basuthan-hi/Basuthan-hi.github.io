const side_bar  = document.querySelector('aside')
let side_bar_status = false
function open_sidebar(){
    if (side_bar_status){
        side_bar.setAttribute('class','hide')
        side_bar_status = false
    }else{
        side_bar.setAttribute('class','show')
        side_bar_status = true
    }
}