
var value= 0;
var colourart= ["#C75D50","#C78350","#C7C150","#8DC750","#50C761","#50C781"]
function addone(){
  value= value+1;
  document.getElementById('valuepara').innerHTML= ("Count: "+value);
document.body.style.backgroundColor= colourart[value];
}
function minusone(){
  value = value-1;
  document.getElementById('valuepara').innerHTML= ("Count: "+value);
document.body.style.backgroundColor= colourart[value];
}
