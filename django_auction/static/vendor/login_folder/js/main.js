(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	$(".toggle-password").click(function() {

	  $(this).toggleClass("fa-eye fa-eye-slash");
	  var input = $('#password-field');

	  if(input.attr("type") == "password") {
		input.attr("type", "text");
	  }
	  else {
		input.attr("type", "password");
	  }
	});

	$(".toggle-password1").click(function() {

	  $(this).toggleClass("fa-eye fa-eye-slash");
	  var input = $('#password-field1');

	  if(input.attr("type") == "password") {
		input.attr("type", "text");
	  }
	  else {
		input.attr("type", "password");
	  }
	});

	$(".toggle-password2").click(function() {

	  $(this).toggleClass("fa-eye fa-eye-slash");
	  var input = $('#password-field2');

	  if(input.attr("type") == "password") {
		input.attr("type", "text");
	  }
	  else {
		input.attr("type", "password");
	  }
	});

})(jQuery);
