/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
//function myFunction() {
//  document.getElementById("myDropdown").classList.toggle("show");
//}
//
//// Close the dropdown if the user clicks outside of it
//window.onclick = function(e) {
//  if (!e.target.matches('.dropbtn')) {
//  var myDropdown = document.getElementById("myDropdown");
//    if (myDropdown.classList.contains('show')) {
//      myDropdown.classList.remove('show');
//    }
//  }
//}

document.addEventListener('DOMContentLoaded', () => {
    let buttons=document.querySelectorAll('.button-wave');
    for (let ind = 0; ind < buttons.length; ind++)
        buttons[ind].addEventListener('click', () => {goto(buttons[ind].id)});

});

function goto(but_name){
    switch (but_name){
    case 'morl':
        document.location.href = 'morlet.html';
        break;
    case 'haar':
        document.location.href = 'haar.html';
        break;
    }
    console.log(but_name)
//    document.location.href = 'morlet.html';
}

