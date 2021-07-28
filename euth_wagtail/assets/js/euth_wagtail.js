import 'slick-carousel'

$(document).ready(function () {
  // hide the all of the element with class collapsible_body
  $('.collapsible_body').hide()
  // toggle the component with class collapsible_body
  $('.collapsible_head').click(function () {
    $(this).next('.collapsible_body').slideToggle(600)
  })

  if (location.hash !== '') $('a[href="' + location.hash + '"]').tab('show')
  $('a[data-bs-toggle="tab"]').on('shown.bs.tab', function (e) {
    if (history.pushState) {
      history.pushState(null, null, '#' + $(e.target).attr('href').substr(1))
    } else {
      location.hash = '#' + $(e.target).attr('href').substr(1)
    }
  })

  $('.carousel').slick({
    centerMode: false,
    slidesToShow: 4,
    slidesToScroll: 4,
    dots: false,
    arrows: true,
    centerPadding: 30,
    mobileFirst: true,
    infinite: false,
    prevArrow: '<button class="slick-prev"><i class="fa fa-chevron-left"></i></button>',
    nextArrow: '<button class="slick-next"><i class="fa fa-chevron-right"></i></button>',
    responsive: [
      {
        breakpoint: 0,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          arrows: false
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3
        }
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 4
        }
      }
    ]
  })

  $('.form-control-file').change(showFileName)

  $('.howto-carousel').slick({
    dots: true,
    infinite: false,
    arrows: false,
    cssEase: 'linear',
    autoplay: true,
    autoplaySpeed: 6000
  })

  $('.block-xs-carousel').slick({
    dots: false,
    infinite: false,
    arrows: true,
    cssEase: 'linear',
    autoplay: false,
    prevArrow: '<button class="slick-prev"><i class="fa fa-chevron-left"></i></button>',
    nextArrow: '<button class="slick-next"><i class="fa fa-chevron-right"></i></button>'
  })
})

export function showFileName () {
  const string = $(this).val().match(/[^\\/]+$/)[0]
  $(this).parent().find('.form-control-file-dummy').val(string)
}
