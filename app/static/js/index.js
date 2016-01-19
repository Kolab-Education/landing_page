$(function() {
    $('body').on('click', '.page-scroll a', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

$(function(){
  $('#btnSignUp').click(function() {
      $.ajax({
          url: '/signUp',
          data: $('form').serialize(),
          type: 'POST',
          success: function(res) {
            var elms = $('.signup_').empty();
            var div = $('<div>').attr('class', 'col-lg-12 text-center')
            var text = $('<img>').attr({
              'class': 'img-responsive center-block',
              'src': '../static/img/thank_you.png',
              'alt': "",
              'width': '30%'
            });
            div.append(text);
            elms.append(div);
            console.log(res);
          },
          error: function(error) {
              console.log(error);
          }
    });
  });
});


$(function() {
    $("body").on("input propertychange", ".floating-label-form-group", function(e) {
        $(this).toggleClass("floating-label-form-group-with-value", !! $(e.target).val());
    }).on("focus", ".floating-label-form-group", function() {
        $(this).addClass("floating-label-form-group-with-focus");
    }).on("blur", ".floating-label-form-group", function() {
        $(this).removeClass("floating-label-form-group-with-focus");
    });
});

$('body').scrollspy({
    target: '.navbar-fixed-top'
})

$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});
