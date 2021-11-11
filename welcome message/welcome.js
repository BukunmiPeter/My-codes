var hour = 14;

 //var hour = new Date().getHours();
/*morning 4am - 11am
day 12pm - 6pm
evening 7pm -10pm
Night 11pm  - 3am */

  if (hour >= 4 && hour <= 11){
    document.getElementById('dayperiod').innerHTML= "Good morning!!";
    document.body.style.backgroundColor="Yellow";
document.getElementById('welcomeimg').src = "morning.jpg";

  }
  else if (hour>=12 && hour <=18) {
    document.getElementById('dayperiod').innerHTML= "Good day!!";
      document.body.style.backgroundColor="#E3682B";
    document.getElementById('welcomeimg').src = "daytime.jpg";

  }

  else if (hour>=19 && hour <=22) {
    document.getElementById('dayperiod').innerHTML= "Good Evening!!";
    document.body.style.backgroundColor="#6F7078";
    document.getElementById('welcomeimg').src = "evening.jpg";

  }

  else {
    document.getElementById('dayperiod').innerHTML= "Good Night!!";
      document.body.style.backgroundColor="#6D7A77";
    document.getElementById('welcomeimg').src = "night.jpg";

  }
