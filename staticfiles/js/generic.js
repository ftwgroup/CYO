$(document).ready(function(){
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
});