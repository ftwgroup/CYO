$(document).ready(function(){
/*Concert stuff*/
    $('div.image').prependTo('div.event-details');
    $(".zebra tr").mouseover(function(){$(this).addClass("over");}).mouseout(function(){$(this).removeClass("over");});
    $(".zebra tr:even").addClass("alt");

    /*Bios Accordion Stuff
       $('#sidebar-bios h3').next('p').hide();
       makeSidebarOpenNext();
       h2afterh1removeMargins();
       addSignagetoBreadcumbs();
       $('<span>&gt;</span>').prependTo('ul.breadcrumbs > li:not(:first-child)');
       $('<a href="/liza" id="map1"></a>').prependTo('.slideover');



   function makeSidebarOpenNext(){
       $('#sidebar-bios h3').click(function () {
           $(this).next().slideToggle('fast');
       });
   }
    */

    /*Document functions*/
/*
function addSignagetoBreadcumbs(){
    if ($('ul.breadcrumbs').children().length < 2) {
        $('ul.breadcrumbs').css('display', 'none');
    }
}
*/
/*function changeTBAconcertValues(){
    $('li.concert-date').replaceWith('Date to be announced' );
    $('li.concert-time').replaceWith('');
}
*/

});/*The end*/