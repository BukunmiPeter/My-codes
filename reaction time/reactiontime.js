/*
========-Have a box on the screen==========
=========-When box is clicked it disappears=========
- ===========when the box is clicked, it reappears after 3 seconds=======
========measure time between shape appearing and being clicked========
=======output that setTimeout(function () {
},========
part 2
========Random delay time==========
===========Random location on the screen===========
===========Random shape===========
===========height and width===========
curvature
Random color
;

*/

window.onload =appear();
var start;
var clicked;

function disappear(){
  document.getElementById('box').style.display ="none";
  clicked= Date.now();
  var reactiontime = (clicked-start)/1000;
  alert(reactiontime + "  seconds");
  var randomdelay = ((Math.random()*3)+1)*1000;
    setTimeout(appear,randomdelay);
}


function appear(){
  var randomtop = Math.random()*400;
  var randomleft = Math.random()*400;
  var randomheight = Math.random()*200+10;
    var randomwidth = Math.random()*200+10;
    var randomcurve = Math.random();
    var randomcolor = "#" + ((1<<24)*Math.random() | 0).toString(16);

    if (randomcurve < 0.5) {
      document.getElementById('box').style.borderRadius = 25+"px";
    } else document.getElementById('box').style.borderRadius = 0 +"px";
  document.getElementById('box').style.top=randomtop+"px";
    document.getElementById('box').style.left=randomleft+"px";
    document.getElementById('box').style.width=randomwidth+"px";
      document.getElementById('box').style.height=randomheight +"px";
    document.getElementById('box').style.display ="block";
    document.getElementById('box').style.backgroundColor = randomcolor;
    start= Date.now();
}
