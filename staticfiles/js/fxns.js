$(document).ready(function(){
/*Concert stuff*/
    $('div.image').prependTo('div.event-details');
    $(".zebra tr").mouseover(function(){$(this).addClass("over");}).mouseout(function(){$(this).removeClass("over");});
    $(".zebra tr:even").addClass("alt");

/*Bios Accordion Stuff*/
    $('#sidebar-bios h3').next('p').hide();
    makeSidebarOpenNext();
    h2afterh1removeMargins()
    addSignagetoBreadcumbs()

/*Document functions*/
function h2afterh1removeMargins(){
    $('.whitebox h1').next('h2').css('margin','0');
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
    $('<span>&gt;</span>').prependTo('ul.breadcrumbs > li:not(:first-child)');
}
});/*The end*/