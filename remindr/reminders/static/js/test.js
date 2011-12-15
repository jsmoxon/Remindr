$(document).ready(function() {
	$("#datepicker").datepicker({
		dateFormat: 'yy-mm-dd',
		onSelect: function (dateText, inst) {
		    //    $(this).parent('form').submit(); no longer working but illustrative
		}//closes onselect function
	    });//closes datepicker
    });

//var date = $('#datepicker').datepicker({ dateFormat: 'yy-mm-dd'});