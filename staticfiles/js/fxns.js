$(document).ready(function(){
/*Concert stuff*/
    $('div.image').prependTo('div.event-details');
    $(".zebra tr").mouseover(function(){$(this).addClass("over");}).mouseout(function(){$(this).removeClass("over");});
    $(".zebra tr:even").addClass("alt");

/*Bios Accordion Stuff*/
    $('#sidebar-bios h3').next('p').hide();
    makeSidebarOpenNext();
    h2afterh1removeMargins();
    addSignagetoBreadcumbs();
    $('<span>&gt;</span>').prependTo('ul.breadcrumbs > li:not(:first-child)');

/*Document functions*/

function h2afterh1removeMargins(){
    $('.whitebox h1').next('h2').css('margin','0');
    $('.whitebox .image-wrapped').next('h2').css('margin','0');
}
function makeSidebarOpenNext(){
    $('#sidebar-bios h3').click(function () {
        $(this).next().slideToggle('fast');
    });
}
function addSignagetoBreadcumbs(){
    if ($('ul.breadcrumbs').children().length < 2) {
        $('ul.breadcrumbs').css('display', 'none');
    }
}
    $("a.image_wrapped").fancybox({
        openEffect: 'elastic',
        closeEffect: 'elastic',
        prevEffect	: 'none',
        nextEffect	: 'none',
        maxWidth : 640,
        maxHeight : 480,
        closeBtn		: true,
        helpers	: {
            title	: {
                type: 'inside'
            },
            overlay	: {
                opacity : 0.8,
                css : {
                    'background-color' : '#000'
                }
            },
            thumbs	: {
                width	: 50,
                height	: 50
            }
        }
    });

/*function changeTBAconcertValues(){
    $('li.concert-date').replaceWith('Date to be announced' );
    $('li.concert-time').replaceWith('');
}
*/

});/*The end*/