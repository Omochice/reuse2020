$(document).ready(function() {
    $(".dropdown-trigger").dropdown();
});

$(document).ready(function() {
    $(".sidenav").sidenav();
});

function ChangeImage(imgid) {
    newimg = event.target;
    document.getElementById(imgid).src = newimg.src;
    console.log(newimg);
}

function change_text() {
    p_tag = document.getElementById("text-kun");
    console.log(p_tag);
    p_tag.innerHTML = "いち";
}

function go_forward() {}
