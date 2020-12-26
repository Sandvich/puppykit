var search = function() {
    var e = document.querySelector("#type");
    var search_type = e.options[e.selectedIndex].value;
    var query = document.querySelector("#search_term").value;
    window.location.href = "/personal/rpgs/" + search_type + "/" + query + "/"
}

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#search_button").addEventListener("keypress", event => {
        if(event.key !== "Enter") { event.preventDefault() };
        document.querySelector("#search_button").click();
    })
});
