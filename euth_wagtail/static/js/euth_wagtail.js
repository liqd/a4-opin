$(document).ready(function () {
  //hide the all of the element with class collapsible_body
  $(".collapsible_body").hide();
  //toggle the component with class collapsible_body
  $(".collapsible_head").click(function () {
    $(this).next(".collapsible_body").slideToggle(600);
  });

  if (location.hash !== '') $('a[href="' + location.hash + '"]').tab('show');
  $('a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
    if (history.pushState)  {
      history.pushState(null, null, '#'+$(e.target).attr('href').substr(1));
    } else {
      location.hash = '#'+$(e.target).attr('href').substr(1);
    }
  });

  var projectCount = $("#project-tile-grid .project-tile").length;
  var loop = (projectCount < 4) ? false : true;

    $('.owl-carousel').owlCarousel({
        center: false,
        items: 4,
        loop: loop,
        dots: false,
        nav: true,
        margin: 20,
        navText: ['<i class="fa fa-chevron-left"></i>','<i class="fa fa-chevron-right"></i>'],
        responsive:{
            0: {
                items: 1
            },
            480: {
              items: 2
            },
            768:{
                items: 3
            },
            992: {
              items: 4
            }
        }
    });

  $(".form-control-file").change(function() {
    var string = $(this).val().match(/[^\\/]+$/)[0]
    $(this).parent().find(".form-control-file-dummy").val(string)
  });
});
