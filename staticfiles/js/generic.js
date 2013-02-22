$(document).ready(function(){

        //        Make 'search' vanish
        $("input[name='q']").focus(function(){
            if (this.value=='Search') this.value='';

        }).blur(function(){
                if (this.value=='') this.value='Search';
            });

        //Fancybox does not exist on the homepage so any functions placed after
        //this will not work on the home page
        $("a.image_wrapped, a.image_downloadable").fancybox({
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
    }
);