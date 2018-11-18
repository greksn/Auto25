$(document).ready(function(){
    $(".mainsearch").focusin(function(){
        $(".tip").fadeIn(1500);
    });
    $(".mainsearch").focusout(function(){
        $(".tip").fadeOut(500);
    });
    $("#newThreadButton").click(function(){
        $(".new-thread").fadeIn(1000);
    });
});
if (typeof jQuery == 'undefined') {
    document.write(unescape("%3Cscript src='./js/jquery-3.3.1.js' type='text/javascript'%3E%3C/script%3E"));
}
