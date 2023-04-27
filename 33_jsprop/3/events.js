// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  e.stopPropagation(); // this one stops it in its tracks, no other promps pop up
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

//Predict, then test...
//Q: What effect does the boolean arg have?
//   (Leave exactly 1 version uncommented to test...)

table.addEventListener('click', clicky, true); // the true boolean arg will completely change it and have this return first completely reversing the default order
// table.addEventListener('click', clicky, false); //  the basic behavior

// Q: When user clicks on a cell, in what order will the pop-ups appear?
