document.body.style.backgroundColor="green";


function calculateTip(){

  var totalamount = document.getElementById('billamount').value;
  var qualityofservice=document.getElementById('qualityservice').value;
  var numofPeople = document.getElementById('numPeople').value;
 var tipperson = Math.round((totalamount*qualityofservice/numofPeople));
  if (totalamount== ""){
      document.getElementById('result').innerHTML= "Please enter the total bill";

  }else if (numofPeople == "") {
      document.getElementById('result').innerHTML= "Please enter the number of people";
  }else{
    //alert(tipperson)
    document.getElementById('result').innerHTML= " TIP AMOUNT: <br>" +tipperson + "<br>per person";

  }


}
