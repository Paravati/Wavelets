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
    case 'daub':
        document.location.href = 'daubechie.html';
        break;
    case 'mex':
        document.location.href = 'mexicanHat.html';
        break;
    case 'compl':
        document.location.href = 'complexWavelets.html';
        break;
    case 'transform':
        document.location.href = 'waveletTransform.html';
        break;
    }
    console.log(but_name)
}

