var toggleMenu = function () {
    $('#menu').toggleClass('open');
    $('#toggle').toggleClass('x');
};

var initNavBar = function() {
	var anchor = $("#page");
	console.log(anchor.html());
	$("#" + anchor.html()).addClass( "current" );
	// In future the following line will replace the identifier with an img tag, so that we have a custom banner on each page.
	anchor.html("");
	$('#toggle').click(toggleMenu);
};

$( document ).ready(initNavBar);
