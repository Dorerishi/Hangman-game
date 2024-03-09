function display_hangman(){
    let wrongs=document.getElementById("wrongs").innerText;
    let image=document.getElementById("img");
    if(wrongs==1){
        image.src="hangmanstart.png";
    }
    else if(wrongs==2){
        image.src="hangman2.png";
    }
    else if(wrongs==3){
        image.src="hangmanfinal.png";
        play_again()        
    }
    else{
        image.src="hangmanbank.png";
    }
}

function check_letter(){
    let hword=document.getElementById("word");
    eel.Win_or_loss(hword.innerText)().then(checkwin);
    let wrongs=document.getElementById("wrongs").innerText;
    let letter=document.getElementById("inp");
    eel.play_hangman(wrongs,letter.value)().then(setop);
    
}

function setop(value){
    let op=document.getElementById("op");
    let wrong=document.getElementById("wrongs");
    let word=document.getElementById("word");
    let val=value.split(",");
    wrong.innerText=val[0];
    op.innerText=val[1];
    word.innerText=val[2];
    display_hangman();
}

function play_again(){
    if (confirm("Do you want to play again?")) {
        eel.init();
        let wrong=document.getElementById("wrongs");
        wrong.innerText="0";
        let word=document.getElementById("word");
        word.innerText="type # to restart";
      } else {
        window.close()
      }
}

function checkwin(value){
    let val=value;
    console.log(val);
    if (val=="True"){
        play_again();
    }
}


