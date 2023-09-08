const slider = document.getElementById('slider');
const slides = document.getElementById('slides');
const slide1 = document.querySelector('.details1');
const slide2 = document.querySelector('.details2');
const slide3 = document.querySelector('.details3');

const slideElements = [slide1, slide2, slide3];
const totalSlides = slideElements.length;

let currentSlide = 0; // Start from the first slide
let direction = 1; // 1 for forward, -1 for backward

const slideWidth = 910; // Width of each slide
const transitionDuration = 500; // Transition duration in milliseconds
const delay = 5000; // Delay between slide transitions

function transitionSlide() {
    // Calculate the index of the next slide
    const nextSlide = (currentSlide + direction + totalSlides) % totalSlides;

    // Move the current slide out and the next slide in
    slideElements[currentSlide].style.marginRight = `-${slideWidth}px`;
    slideElements[nextSlide].style.marginRight = '0px';

    // Update currentSlide
    currentSlide = nextSlide;

    // Wait for the transition to complete before transitioning to the next slide
    setTimeout(transitionSlide, transitionDuration + delay);
}

// Set initial slide positions
slideElements.forEach((slide, index) => {
    slide.style.marginRight = index === 0 ? '0px' : `-${slideWidth}px`;
});

// Start the slide show
setTimeout(transitionSlide, delay);