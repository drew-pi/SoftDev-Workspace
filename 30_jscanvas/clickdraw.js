
//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    var text = document.getElementById("buttonToggle");
    if (mode === "rect") {
        mode = "circ";
        text.innerHTML = "circle";
    }
    else {
        mode = "rect";
        text.innerHTML = "rectangle"
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY; //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "blue";
    ctx.fillRect(mouseX, mouseY, 100, 50);
}

var drawCircle = function(e) {
    var mouseX = e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY; //gets Y-coor of mouse when event is fired
    console.log("cirlce: mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "green";
    ctx.arc(mouseX,mouseY,10,0,Math.PI*2);
    ctx.fill();
}

var draw = function(e) {
    if (mode == "rect") {
        drawRect(e);
    }
    else {
        ctx.beginPath()
        drawCircle(e);
    }
}

var clear = function(e) {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw); //passes the mouse event as parameter for the function

var toggle = document.getElementById("buttonToggle");
toggle.addEventListener("click",toggleMode);

var wipe = document.getElementById("buttonClear");
wipe.addEventListener("click",clear);
