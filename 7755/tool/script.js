
function cal(){
	
  $('#lth').html($('#ct').val().length+'');
  
}

function indent(){
	var content = ' - '+$('#mk').val().replaceAll('\n', '\n - ');
	$('#mk').val(content);
}

function addNo(){
	var lines = $('#mk').val().split('\n');
	var content = '';
	for(var i=0;i<lines.length;i++){
		var j = i+1;
		content += j+'. '+lines[i]+'\n';
	}
	
	$('#mk').val(content);
}

$(document).on('change', '#ct', function(){
	
	cal();

});

