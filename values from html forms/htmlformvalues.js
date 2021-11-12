var correctname = "Peter Olu";
var correctpassword = "Peter123";

function formaction(){
  var inputname = document.getElementById('fName').value;
  var inputpass = document.getElementById('password').value;

  if (inputname == correctname && inputpass == correctpassword){
    document.body.style.backgroundColor= "green";
    alert("Access granted! Welcome");
  } else {
  document.body.style.backgroundColor= "red";
  alert("Access denied!")
  }
}

function calculate(){
  var numone = document.getElementById('firstno').value;
  var numtwo = document.getElementById('secondno').value;

  var numthree = numone * numtwo;
alert ("Your result is:    " + numthree)


}
