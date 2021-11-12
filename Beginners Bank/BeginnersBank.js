var name = "Peter";
var password = "Peter123"
var currentbalance= 500;



function bank(){

  var inputname = document.getElementById('fname').value;
    var inputpassword = document.getElementById('fpassword').value;
 var inputamout = document.getElementById('famount').value;

var newbal = currentbalance - inputamout;


 if (inputname != name) {
 document.getElementById('Success').innerHTML= "Incorrect Name. Try again"
} else if (inputpassword!=password ) {
  document.getElementById('Success').innerHTML= "Incorrect password. Try again"

}else if (inputamout>currentbalance) {
    document.getElementById('Success').innerHTML= "insufficient funds"

}else{
    document.getElementById('Success').innerHTML= "Withdraw Successful!Your funds are now :" + newbal;
}


}
