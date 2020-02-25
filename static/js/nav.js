var toggleMenu = function() {
    document.querySelector("#menu").classList.toggle("open");
    document.querySelector("#toggle").classList.toggle("x");
}

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#toggle").addEventListener("click", toggleMenu);
    document.querySelector("#toggle").addEventListener("touched", toggleMenu);
});
