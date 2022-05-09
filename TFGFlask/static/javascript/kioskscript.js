//Idioma color change & timeout
changeColorEus = function(color) {
    setTimeout(function(){
        document.getElementById("btn2Eus").style.background = color;
        document.getElementById("btn2Eus").style.color = "#000";
    }, 2000);
}

changeColorEus('transparent');

changeColorCas = function(color) {
    setTimeout(function(){
        document.getElementById("btn2Cas").style.background = color;
        document.getElementById("btn2Cas").style.color = "#000";
    }, 2000);
}

changeColorCas('transparent');


//Aunquieres color change & timeout
changeColorAunSi = function(color) {
    setTimeout(function(){
        document.getElementById("boton3Si").style.background = color;
        document.getElementById("boton3Si").style.color = "#000";
    }, 4000);
}
  
changeColorAunSi('transparent');

changeColorAunNo = function(color) {
    setTimeout(function(){
        document.getElementById("boton3No").style.background = color;
        document.getElementById("boton3No").style.color = "#000";
    }, 4000);
}

changeColorAunNo('transparent');


//BotonContinuar (x3 htmls la usan)
changeColorCont = function(color) {
    setTimeout(function(){
        document.getElementById("btnCont").style.background = color;
        document.getElementById("btnCont").style.color = "#000";
    }, 4000);
}
  
changeColorCont('transparent');