$(document).ready(function(){
    var icons = {
        header: "ui-icon-circle-arrow-e",
        headerSelected: "ui-icon-circle-arrow-s"
    };
    $('#sidebar-bios h3').next('p').hide();
    makeSidebarOpenNext();
    $('.concert_leftCol div.image').prependTo('div.event-details');
    $(".zebra tr").mouseover(function(){$(this).addClass("over");}).mouseout(function(){$(this).removeClass("over");});
    $(".zebra tr:even").addClass("alt");
});

function makeSidebarOpenNext(){
    $('#sidebar-bios h3').click(function () {
        $(this).next().slideToggle('fast');
    });
    }
