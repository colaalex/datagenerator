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

function makeChart(data) {

}

function onSubmit( form ){
    var data = JSON.stringify( $(form).serializeArray() ); //  <-----------

    console.log( data );

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        function callback(responseText) {
            $('#result-plot').html('');
            var data = responseText.split(/\r?\n|\r/);
            var table_data = '<table>';
            for (var count = 0; count < data.length; count++) {
                var cell_data = data[count].split(",");
                table_data += '<tr>';
                for (var cell_count = 0; cell_count < cell_data.length; cell_count++) {
                    if (count === 0) {
                        table_data += '<th>'+cell_data[cell_count]+'</th>';
                    } else {
                        table_data += '<td>'+cell_data[cell_count]+'</td>';
                    }
                }
                table_data += '</tr>';
            }
            table_data += '</table>';
            $('#result-table').html(table_data);
            $('#result-plot').html('<img src="/static/img/plot.png" alt="plot" width="500"/>');
        }

        if (xmlHttp.readyState === 4 && xmlHttp.status === 200)
            callback(xmlHttp.responseText);
    };
    xmlHttp.open("GET", "/api/generate?data=" + data, true);
    xmlHttp.send(null);
    console.log(xmlHttp);

    return false; //don't submit
}

function selectElement(id, valueToSelect) {
    console.log("selected");
    let element = document.getElementById(id);
    element.value = valueToSelect;
}


  