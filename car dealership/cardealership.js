var cars = ["BMW", "Volvo", "Saab", "Ford", "Fiat", "Audi","Benz"];

var text = " ";

 for(i=0; i<cars.length; i++){
text +=cars[i] + "  <br>";

  document.getElementById("carmodels").innerHTML = text;
}
