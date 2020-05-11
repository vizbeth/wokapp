const navSlide = ()=>{
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    burger.addEventListener('click', ()=>{
        nav.classList.toggle('nav-active')

        navLinks.forEach((link, index)=>{
            if(link.style.animation){
                link.style.animation = ''
            }else{
                link.style.animation = `navLinksFade 0.5s ease forwards ${index / 7 + 1.5}s`
            }
        });

        burger.classList.toggle('change');
    });
}
navSlide()

const mainSlide = ()=>{
    const arrowLeft = document.querySelector('#arrow1');
    const arrowRight = document.querySelector('#arrow2');
    const sliderImages = document.querySelectorAll('.slides');
    let current = 0;

    function reset(){
        for(let i = 0; i<sliderImages.length; i++){
            sliderImages[i].style.display = 'None'
        };
    }
    
    function startSlide(){
        reset();
        sliderImages[0].style.display = 'block'
    }
    startSlide()

    function slideLeft(){
        reset();
        sliderImages[current - 1].style.display = 'block';
        current--;
    }

    function slideRight(){
        reset();
        sliderImages[current + 1].style.display = 'block';
        current++;
    }

    arrowLeft.addEventListener('click', ()=>{
        if(current === 0){
            current = sliderImages.length;
        }
        slideLeft();
    });

    arrowRight.addEventListener('click', ()=>{
        if(current === sliderImages.length - 1){
            current = -1;
        }
        slideRight();
    });

}
mainSlide()

