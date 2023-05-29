$(document).ready(function() {
    // Sticky Navbar
    $(window).scroll(function() {
      if ($(window).scrollTop() > 0) {
        $('.navbar').addClass('sticky');
      } else {
        $('.navbar').removeClass('sticky');
      }
    });
  });
  

  $(window).on('scroll', function() {
    if ($(window).scrollTop() > 50) {
      $('.navbar').addClass('scrolled');
    } else {
      $('.navbar').removeClass('scrolled');
    }
  });