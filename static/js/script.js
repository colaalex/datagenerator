jQuery(document).ready(function() {
    function select_changed(){
        /* $("div[id*='form-']").each(function(){
           $(this).removeClass('form-visible');
        }); */
        $("select[name='selectform']").each(function(){
            var selected = $(this).val();
            //$('#'+selected).addClass('form-visible');
            obj = $("#templates-container").find('.'+selected);
            $("#container").append($(obj).clone());
            $(this).val("");
        });
    }

    $("select[name='selectform']").change(function(){
        select_changed();
    });
});

function deleteBox(element){
    console.log($(element));
    $(element).parent('.dynamicSelect-form').remove(); 
    console.log("CLICKED");
};

jQuery(document).ready(function(){
    $(".tabs-control a:first").addClass("current");
  
    $('.tabs-control a').click(function (e) {
      e.preventDefault();
      var _href = $(this).attr("href");
      $(".tabs-control a").removeClass("current");
      $(this).addClass("current");
      $(".tabs-content > div").hide();
      $(_href).fadeIn();
    });
});

function onSubmit( form ){
    var data = JSON.stringify( $(form).serializeArray() ); //  <-----------
  
    console.log( data );
    return false; //don't submit
  }

  