function trigger(){
    var imagepath="images/";
    var dice="dice";
    var random1=Math.floor(Math.random()*(6))+1;
    var path1=imagepath+dice+random1+".png";
    
    var random2=Math.floor(Math.random()*(6))+1;
    var path2=imagepath+dice+random2+".png";
    var image=document.querySelectorAll("img");
    
    image[0].setAttribute("src",path1);
    image[1].setAttribute("src",path2);
    if(random1<random2)
    {
        var h1=document.querySelector("h1").innerHTML="Player 2 wins!⛳";
    
        console.log(random1+" " +random2);
    }
    else if(random1==random2)
    {
        var h1=document.querySelector("h1").innerHTML="Draw!";
        console.log(random1+" " +random2);
    }
    else{
        h1=document.querySelector("h1").innerHTML="⛳Player 1 wins!";
        console.log(random1+" " +random2);
    }
}
 var btn = document.querySelector(".btn");
// add event listener for the button, for action "click"
btn.addEventListener("click", trigger);