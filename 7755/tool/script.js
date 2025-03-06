
function cal(){
	
  $('#lth').html($('#ct').val().length+'');
  
}

$(document).on('change', '#ct', function(){
	
	cal();

});

