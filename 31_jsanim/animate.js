var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "turqoise";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 0;
var growing = true;

var drawDot = () => {

    console.log("drawDot invoked")
    // if (growing == true) {
    // clear();
    ctx.beginPath();
    ctx.arc(c.width/2,c.height/2,radius,0,Math.PI*2);
    ctx.fill()

    requestID = window.requestAnimationFrame(drawDot);
    window.cancelAnimationFrame(requestID);

    radius += 1;
    // };
};


var stopIt = () => {
    console.log("stopIT invoked...");
    console.log( requestID );

    growing = false;
    window.cancelAnimationFrame();
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt );