var callback = function() {
    $('.animated').each( function() {
        $(this).parent().html($(this).attr('alt'));
    });
};

var add_click = function() {
    $('.animated').click(callback);
};

$( document ).ready(add_click);