var height = [16,18,16,21]
var width=[9, 9,10,10];

function cal(){
  
  var screen = $('#phoneScreen').val();
  var ratioIdx = $('#phoneRatio').val();
  
  var pw, ph;
  
  if(ratioIdx < 0){
	pw = $('#custRatioWidth').val();
	ph = $('#custRatioHeight').val();
  }else{
	pw = width[ratioIdx];
	ph = height[ratioIdx];
  }
  
  var res = $('#phoneResolution').val()>0? $('#phoneResolution').val() : $('#custRes').val();
   
  var r = ph/pw;
  
  var vw = Math.sqrt(screen * screen / (1 + r*r));
  
  var vh = vw * r;
  
  vw *= res;
  vh *= res;
  
   $('#vh').html(vh);
   $('#vw').html(vw);
   
   vw = Math.round(vw/10)*10;
   vh = Math.round(vh/10)*10;
   
   $('#svh').html(vh);
   $('#svw').html(vw);
}

$(document).on('change', '#phoneResolution', function(){
	if($('#phoneResolution').val()>0){
		$('#custRes').hide();
		$('#custResLabel').hide();
	}else{
		$('#custRes').show();
		$('#custResLabel').show();
	}
});

$(document).on('change', '#phoneRatio', function(){
	if($('#phoneRatio').val()>0){
		$('#custRatio').hide();
	}else{
		$('#custRatio').show();
	}
});
