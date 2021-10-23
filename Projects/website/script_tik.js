console.log("Welcome to Tik Tak toe ")
let turn ="X"
let gameover=false

//Function to change the Turn
const changeTurn =()=>{
    return turn==="X"?"0":"X"
}

//Function to check win
const checkwin=()=>{
    let boxtext=document.getElementsByClassName('boxtext');
    let wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6],
    ]
  wins.forEach(e=>{
      if((boxtext[e[0]].innerText===boxtext[e[1]].innerText) && (boxtext[e[2]].innerText===boxtext[e[1]].innerText) && (boxtext[e[0]].innerText!=="")){
          document.querySelector('.info').innerText=boxtext[e[0]].innerText+ " WON"
          gameover=true
          document.querySelector('.imgbox').getElementsByTagName('img')[0].style.width='300px';
      }

  })

}

//Game Logic
let boxes=document.getElementsByClassName("box");
Array.from(boxes).forEach(element=>{
    let boxtext=element.querySelector('.boxtext');
    element.addEventListener('click',()=>{
        if(boxtext.innerText===''){
            boxtext.innerText=turn;
            turn= changeTurn();
            checkwin();
            if(!gameover){
                document.getElementsByClassName('info')[0].innerText=' Turn For '+turn;
            }
            
        }
    })
})

//Add onclick listner to reset button
reset.addEventListener('click',()=>{
    let boxtexts=document.querySelectorAll('.boxtext');
    Array.from(boxtexts).forEach(element=>{
        element.innerText=" ";
    });
    turn="X";
    gameover=false
    document.getElementsByClassName("info")[0].innerText="Turn for "+turn;
    document.querySelector('.imgbox').getElementsByTagName('img')[0].style.width='0px';
})

function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("aboutttt").innerHTML =
        this.responseText;
      }
    };
    xhttp.open("GET", "about ttt.txt", true);
    xhttp.send();
  }

  