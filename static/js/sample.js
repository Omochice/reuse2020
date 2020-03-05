$(document).ready(function() {
    $(".dropdown-trigger").dropdown();
});

$(document).ready(function() {
    $(".sidenav").sidenav();
});

function ChangeImage(imgid, newimg) {
    console.log("hello");
    document.getElementById(imgid).src = newimg;
    console.log(newimg);
}

function change_text() {
    p_tag = document.getElementById("text-kun");
    console.log(p_tag);
    p_tag.innerHTML = "いち";
}

function go_forward() {}

document.addEventListener("DOMContentLoaded", function() {
    var elems = document.querySelectorAll(".slider");
    var instances = M.Slider.init(elems, options);
});
