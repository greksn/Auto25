$(document).ready(function(){
    $(".search").focusin(function(){
        $(".tip").fadeIn(1500);
    });
    $(".search").focusout(function(){
        $(".tip").fadeOut(500);
    });
});