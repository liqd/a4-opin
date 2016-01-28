jQuery(function($) {
    $('.carousel').sss();
});

$(document).ready(function()
    {
      //hide the all of the element with class collapsible_body
      $(".collapsible_body").hide();
      //toggle the component with class collapsible_body
      $(".collapsible_head").click(function()
      {
        $(this).next(".collapsible_body").slideToggle(600);
      });
    });
