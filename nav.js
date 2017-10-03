var initNavBar = function() {
	var anchor = $("#page");
	console.log(anchor.html());
	$("#" + anchor.html()).addClass( "current" );
	// In future the following line will replace the identifier with an img tag, so that we have a custom banner on each page.
	anchor.html("");
};

var setup = function() {
	$( "#nav" ).load("/nav.html", initNavBar);
};

$( document ).ready(setup);
