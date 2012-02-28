$(document).ready(function(){
    $('div.image').prependTo('div.event-details');
    $(".zebra tr").mouseover(function(){$(this).addClass("over");}).mouseout(function(){$(this).removeClass("over");});
    $(".zebra tr:even").addClass("alt");
});