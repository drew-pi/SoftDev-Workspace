var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");

var ctx = c.getContext("2d");

ctx.fillStyle = "turqoise";

var requestID;

var clear = (e) => {
    console.log(typeof e);
    e.preventDefault();
    ctx.clearRect(0, 0, c.width, c.height);
};

var dvdLogoSetup = function(e) {

    window.cancelAnimationFrame(requestID);
    var rectWidth = 50;
    var rectHeight = 50;

    var rectX = Math.random() * (c.width-50);
    // var rectX = 450;
    var rectY = Math.random() * (c.height-50);
    // var rectY = 450;
    console.log(rectX + " , " + rectY );

    var xVel = 1;
    var yVel = 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function(e) {
        // clear(e);
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.drawImage( logo, rectX, rectY, rectWidth,rectHeight);

        if ( rectX > c.width-50 || rectX < 0) {
            xVel = -xVel;
        }
        if ( rectY > c.height-50 || rectY < 0) {
            yVel = -yVel;
        }
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    };
    dvdLogo(e);
};

var radius = 0;
var growing = true;

var drawDot = (e) => {
    console.log("drawDot invoked")
    window.cancelAnimationFrame(requestID);
    // clear(e);
    ctx.clearRect(0, 0, c.width, c.height);

    ctx.beginPath();
    ctx.arc(c.width/2,c.height/2,radius,0,Math.PI*2);
    ctx.fill()
    requestID = window.requestAnimationFrame(drawDot);
    // a bunch of if statements to make sure that it does not grow to crazy
    if (radius > c.height/2 || radius > c.width/2) {
        growing = false;
        console.log("reached border");
    }
    if (radius < 1) {
        growing = true;
        console.log("reached dot");
    }

    if (growing == true) {
        radius += 1;
    }
    else {
        radius -= 1;
    }
};


var stopIt = () => {
    console.log("stopIT invoked...");
    console.log( requestID );

    // growing = false;
    window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt );
dvdButton.addEventListener("click",dvdLogoSetup);


