function zoom(high_res_url, width, height, low_res_url) {
    // Draw placeholder image
    var lightbox_img = document.getElementById('lightbox_img');
    lightbox_img.src = low_res_url ? low_res_url : 'empty.gif';
    lightbox_src.style.width = width + 'px';
    lightbox_src.style.height = height + 'px';

    show_lightbox();

    // Load high-res image
    var high_res_img = new Image();
    high_res_img.onload = function(){
        lightbox_img.src = this.src;
    };
    high_res_img.src = high_res_url;
}
