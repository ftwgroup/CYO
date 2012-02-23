$(document).ready(function(){
    $('#sidebar-details h3').next('p').hide();
    makeSidebarOpenNext();
});

function makeSidebarOpenNext(){
    $('#sidebar-bios > h3').click(function () {
        $(this).next().slideToggle();
    });
    }