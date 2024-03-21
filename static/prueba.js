document.querySelector('.menu-btn').addEventListener('click',() => {
    document.querySelector('.nav-menu').classList.toggle('show');
});
document.querySelector('.nav-brand').addEventListener('click',() => {
    document.querySelector('.nav-user').classList.toggle('show');
});

ScrollReveal().reveal('.new-cards',{delay:200});
ScrollReveal().reveal('.Social', {delay:100});