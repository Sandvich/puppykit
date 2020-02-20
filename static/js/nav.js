var toggleMenu = function () {
    $('#menu').toggleClass('open');
    $('#toggle').toggleClass('x');
};

$( document ).ready($('#toggle').click(toggleMenu));
