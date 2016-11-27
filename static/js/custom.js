/*=============================================================
    Authour URL: www.designbootstrap.com

    http://www.designbootstrap.com/

    License: MIT

    http://opensource.org/licenses/MIT

    100% Free To use For Personal And Commercial Use.

    IN EXCHANGE JUST TELL PEOPLE ABOUT THIS WEBSITE

========================================================  */

$(document).ready(function () {

/*====================================
SCROLLING SCRIPTS
======================================*/

$('.scroll-me a').bind('click', function (event) { //just pass scroll-me in design and start scrolling
var $anchor = $(this);
$('html, body').stop().animate({
scrollTop: $($anchor.attr('href')).offset().top
}, 1200, 'easeInOutExpo');
event.preventDefault();
});


/*====================================
SLIDER SCRIPTS
======================================*/


$('#carousel-slider').carousel({
interval: 2000 //TIME IN MILLI SECONDS
});


/*====================================
VAGAS SLIDESHOW SCRIPTS
======================================*/
//$.vegas('slideshow', {
//backgrounds: [
//{ src: '../static/img/2.jpg', fade: 1000},
//]
//})('overlay', {
///** SLIDESHOW OVERLAY IMAGE **/
//src: '../static/js/vegas/overlays/06.png' // (06, THERE ARE TOTAL 01 TO 15 .png IMAGES AT THE PATH GIVEN, WHICH YOU CAN USE HERE
//});
//

/*====================================
POPUP IMAGE SCRIPTS
======================================*/
$('.fancybox-media').fancybox({
openEffect: 'elastic',
closeEffect: 'elastic',
helpers: {
title: {
type: 'inside'
}
}
});


/*====================================
FILTER FUNCTIONALITY SCRIPTS
======================================*/
$(window).load(function () {
var $container = $('#gallery-div');
$container.isotope({
filter: '*',
animationOptions: {
duration: 750,
easing: 'linear',
queue: false
}
});
$('.categories a').click(function () {
$('.categories .active').removeClass('active');
$(this).addClass('active');
var selector = $(this).attr('data-filter');
$container.isotope({
filter: selector,
animationOptions: {
duration: 750,
easing: 'linear',
queue: false
}
});
return false;
});

});



/*====================================
WRITE YOUR CUSTOM SCRIPTS BELOW
======================================*/

window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove();
    });
}, 4000);

//Guild rank from wowprogress
function Get(yourUrl){
    var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET",yourUrl,false);
    Httpreq.send(null);
    return Httpreq.responseText;
}
var obj = JSON.parse(Get("http://www.wowprogress.com/guild/eu/twisting-nether/Undivine/json_rank"));
document.getElementById("guildrank").innerHTML =
"Twisting Nether " +
obj.realm_rank +
", World "+
obj.world_rank;

});