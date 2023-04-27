// demo 2
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

table.addEventListener('click', clicky);


// Q: When user clicks on a cell, in what order will the pop-ups appear?

// does the most inner html first (td), then the next (tr) and finally the most general
// html tag, table

// TBODY

//     TR
//         #text:
//         TD
//             #text: Yoda
//         #text:
//         TD
//             #text: Luke
//         #text:
//         TD
//             #text: Obi-Wan
//         #text: 
//     #text:
//     TR
//         #text:
//         TD
//             #text: Vader
//         #text:
//         TD
//             #text: Maul
//         #text:
//         TD
//             #text: Palpatine
//         #text: 
//     #text: 
