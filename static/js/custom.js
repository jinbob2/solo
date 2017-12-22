/*********************************************************************************
                                    WOW
***********************************************************************************/
$(function() {
  // Handler for .ready() called.
    new WOW().init();
});

/*********************************************************************************
                               Magnific Popup
http://dimsemenov.com/plugins/magnific-popup/documentation.html#initializing-popup
***********************************************************************************/
$(function () {
 // Handler for .ready() called.
    $('#work').magnificPopup({
  delegate: 'a', // child items selector, by clicking on it popup will open
  type: 'image',
  gallery:{
    enabled: true
  }
  // other options
    });
});


/*

$('.gallery').each(function() { // the containers for all your galleries
    $(this).magnificPopup({
        delegate: 'a', // the selector gor gallery item
        type: 'image',
        gallery: {
            enabled:true
        }
    });
});*/

/**************************************************************
                        carousel
http://owlcarousel2.github.io/OwlCarousel2/index.html
***************************************************************/
$(function (){
    // Handler for .ready() called.
    $("#team-members").owlCarousel({
        items : 3,
        autoplay : true,
        smartSpeed : 700,
        loop: true,
        autoplayHoverPause:true
    });
});

/**************************************************************
                        testimonials
***************************************************************/
$(function (){
    // Handler for .ready() called.
    $("#customers-testimonials").owlCarousel({
        items : 1,
        autoplay : true,
        smartSpeed : 700,
        loop: true,
        autoplayHoverPause : true
    });
});
/**************************************************************
                        counterup
    https://github.com/ciromattia/jquery.counterup
***************************************************************/
$(function (){
   $('.counter').counterUp({
        delay : 10,
        time : 2000
   });
});
/**************************************************************
                        clients
***************************************************************/
$(function (){
    // Handler for .ready() called.
    $("#clients-list").owlCarousel({
        items : 3,
        autoplay : true,
        smartSpeed : 400,
        loop: true,
        autoplayHoverPause : true
    });
});
/**************************************************************
                        Contacts
***************************************************************/
