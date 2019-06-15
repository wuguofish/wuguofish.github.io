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
		
		var _pid = "-1";
		var pid = pid.split("&");
		console.debug(pid);
		for(var i = 0;i<pid.length;i++){
			if(pid[i].indexOf("pid=")>0){
				var tmp = pid[i].split("=");
				_pid = tmp[1];
				break;
			}
		}
		
		
		pid = _pid;		
		
	}
	console.debug(pid);
	if(parseInt(pid) > 0){
		
		$('#tail').css("background-image", "url(./img/player/"+pid+".png)");  
		
	}
	
});

