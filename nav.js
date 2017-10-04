var menu = $('#menu');

var toggleMenu = function () {
  console.log("toggling menu");
  // set timeout so that the panel has a chance to roll up
  // before the menu switches states
  if (menu.hasClass('open')) {
      setTimeout(toggleHorizontal, 500);
  }
  else {
      toggleHorizontal();
  }
  menu.toggleClass('open');
  $('#toggle').toggleClass('x');
};

var toggleHorizontal = function () {
  menu.toggleClass('open');
};

var initNavBar = function() {
	var anchor = $("#page");
	console.log(anchor.html());
	$("#" + anchor.html()).addClass( "current" );
	// In future the following line will replace the identifier with an img tag, so that we have a custom banner on each page.
	anchor.html("");
	$('toggle').click(toggleMenu);
};

var setup = function() {
	$( "#nav" ).load("/nav.html", initNavBar);
};

$( document ).ready(setup);
