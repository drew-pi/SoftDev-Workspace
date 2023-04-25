/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};


var addP = function( text ) { // function add paragraph

  let body = document.getElementsByTagName("body"); // gets the entire body tag but in list format
  let div = document.createElement("div"); // creates a new div element (nothing inside)
  let p = document.createElement("p"); // creates a new paragraph element (nothing inside)
  p.innerHTML = text; // adds some text from input into newly created paragraph element
  div.append(p); // adds the paragraph element into the the div element
  // looks like this
  // <div>
  //   <p></p>
  // </div>
  body[0].append(div); // adds the div at the end of the body (body[0] bc it is in list form)
  // looks like this
  // <body>
  //   ...stuff...
  //   <div>
  //     <p></p>
  //   </div>
  // </body>
}

var modP = function ( text ) { // function modify paragraph
  let p = document.getElementById("output");
  p.innerHTML = text;
}

var getInput = function() {
  let form = document.getElementsByTagName("form")[0]
  let inputs = form.elements
  let output = [];
  for (let i = 0; i < inputs.length; i++) {
    output.push(inputs[i].value);
  }
  // if (!((output[0] == null) || (output[1] == null)))
    console.log(output)
    return output;
}

// fact
function fact(a) {
  if (a == "") {
    return "input null"
  }

  if (a == 1) {
      return a;
  }
  return (a*fact(a-1));
}

// fib
function fib(a) {
  if (a == "") {
    return "input null"
  }

  if (a < 2) {
      return a;
  }
  return (fib(a-1)+fib(a-2));
}

// GCD 
function gcd(a,b) {
  if (a == "" || b == "") {
    return "input(s) null"
  }

  if ((a % b) == 0) {
    return b;
  }
  return gcd (b, a % b);
}


const myFxn = ( text ) => {
  // body
  let y = "woo this is text: " + text;
  modP(y);
};




// document.getElementById("fact").addEventListener("click",modP(fact(getInput()[0]))); 
// document.getElementById("fact").addEventListener("click",modP("hello"));
document.getElementById("fact").addEventListener("click",myFxn);



// document.getElementById("fib").addEventListener("click",modP(fib(getInput()[0])));
document.getElementById("fib").addEventListener("click",modP(fib(getInput()[0])));

// document.getElementById("gcd").addEventListener("click",modP(gcd(getInput()[0],getInput()[1])));
document.getElementById("gcd").addEventListener("click",modP((fib(getInput()[0]),getInput()[1])));

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.

