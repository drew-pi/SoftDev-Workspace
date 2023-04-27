// demo 1
// JS event propagation

var tds = document.getElementsByTagName('td');

var clicky = function(e) {
  alert( this.innerHTML ); // this is an alert, it gives a pop up prompt
  // in this case something that says "file:// and then the innerHTML"
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}
