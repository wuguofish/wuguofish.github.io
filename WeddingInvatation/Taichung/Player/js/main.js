var flipTime = 350;
var ff = false;

$('.card-content ').on('click', function () {
  $('#head').removeClass('roll-in-blurred-left');
  $('.card').toggleClass('flipped');
  $('#buttons').toggle(1000);
});

$(function() {
  // 在這撰寫javascript程式碼
});


$(document).ready(function(){
		console.debug("ready");
	var pid = location.search;
	
	if(pid.length>0){
		
		var pid = pid.split("=");
		console.debug(pid);
		if(pid[0]=="?pid"){
			pid = pid[1];
		}else{
			pid = -1;
		}
		console.debug(pid);
	}
	console.debug(pid);
	if(parseInt(pid) > 0){
		
		$('#tail').css("background-image", "url(./img/player/"+pid+".png)");  
		
	}
	
});

