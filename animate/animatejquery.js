$(".box").animate({height:"250px", width:"500px", opacity:1}, 3000);



//$(".box").click(function(){$(this).css("left","350px")})

$(".box").click(function(){$(this).animate({
  "left":"1000px",
  "top":"500px",
  "height":"30px",
  "width":"80px"
},3000)})


//$(".box").hover(function(){$(this).animate({"top":"500px"},3000)})
