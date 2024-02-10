const swiper = new Swiper('.swiper', {
    loop: true,
    speed: 1000,
    navigation: {
      nextEl: '.btn-next',
      prevEl: '.btn-prev',
    },
    autoplay: {
        delay: 2000,
    }
  });