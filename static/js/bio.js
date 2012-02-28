$(document).ready(function(){
    var icons = {
        header: "ui-icon-circle-arrow-e",
        headerSelected: "ui-icon-circle-arrow-s"
    };
    $('#sidebar-bios h3').next('p').hide();
    makeSidebarOpenNext();
});



function makeSidebarOpenNext(){
    $('#sidebar-bios h3').click(function () {
        $(this).next().slideToggle('fast');
    });
    }