$(document).ready(function() {
    //hide the all of the element with class collapsible_body
    $(".collapsible_body").hide();
    //toggle the component with class collapsible_body
    $(".collapsible_head").click(function()
    {
      $(this).next(".collapsible_body").slideToggle(600);
    });

    if($(".tab-panel").length>0) {
        $(".tab-panel:not(:first-child)").hide();
    }

    $(".tab").click(function() {
        var t = $(this);
        var link = t.attr("href");
        $(".tab-panel").hide();
        $(".tab").removeClass("m-selected");
        $(this).addClass("m-selected");
        $(link).show();
        return false;
    });

    var projectCount = $("#project-tile-grid .project-tile").length;
    var loop = (projectCount<4) ? false : true;

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
});
