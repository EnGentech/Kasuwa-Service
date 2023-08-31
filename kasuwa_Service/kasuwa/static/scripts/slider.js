$(document).ready(function(){
    let slider = $('.image_slider')
    let images = $('.image_slider img')

    let counter = 0;
    let direction = 1;

    function slide(){
        counter += direction;

        if (counter === images.length - 1 || counter === 0){
            direction *= -1;
        }
        slider.css('transform', `translate(-${counter * 100}%)`);
    }
    setInterval(slide, 3000)
})
