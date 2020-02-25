var callback = function() {
    for (let animatedItem of document.querySelectorAll(".animated")) {
        animatedItem.parentElement.innerHTML = animatedItem.getAttribute("alt");
    }
};

document.addEventListener("DOMContentLoaded", function() {
    for (let animatedItem of document.querySelectorAll(".animated")) {
        animatedItem.addEventListener("click", callback);
        animatedItem.addEventListener("touched", callback);
    }
});