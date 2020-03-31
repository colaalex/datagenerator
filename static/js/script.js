moment().format();

$.fn.datetimepicker.Constructor.Default = $.extend({}, $.fn.datetimepicker.Constructor.Default, {
            icons: {
                time: 'fas fa-clock',
                date: 'fas fa-calendar',
                up: 'fas fa-arrow-up',
                down: 'fas fa-arrow-down',
                previous: 'fas fa-chevron-left',
                next: 'fas fa-chevron-right',
                today: 'fas fa-calendar-check-o',
                clear: 'fas fa-trash',
                close: 'fas fa-times'
            } });

$(document).ready(function(){
    $('.show-sensors').on('click', function(){
        $('.box').addClass('open');
    });
    $('#2').on('click', function(){
        $('.box').removeClass('open');
    });
});

$(function () {
    $('#datetimepicker3').datetimepicker({
        locale: 'ru',
        format: 'HH mm ss'
    });
    $('#datetimepicker1').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',
        locale: 'ru'
    }
    );
    $('#datetimepicker2').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',
        locale: 'ru',
        useCurrent: false
    });
    $("#datetimepicker1").on("change.datetimepicker", function (e) {
        $('#datetimepicker2').datetimepicker('minDate', e.date);
    });
    $("#datetimepicker2").on("change.datetimepicker", function (e) {
        $('#datetimepicker1').datetimepicker('maxDate', e.date);
    });
});         

/* beta(a: float, b: float)
binomial(n: int >= 0, p: float >= 0)
exponential(scale: float >= 0)
gamma(k: float >= 0, theta: float >= 0)
geometric(p: float >= 0)
hypergeometric(ngood: int >= 0, nbad: int >= 0, nall: int 1<=nall<=ngood+nbad)
laplace(mean: float, scale: float >=0)
logistic(mean: float, scale: float >= 0)
lognormal(mean: float, std: float >= 0)
logarithmic(p: float 0<p<1)
multinomial(n: int >= 0, pr_of_vals: list of float (sum of them must be 1))
negative_binomial(n: int > 0, p: float 0<=p<=1)
normal(mean: float, std: float >= 0)
poisson(lam: float > 0)
triangular(left: float, top: float >= left, right: float >= top)
uniform(left: float, right: float > left)
weibull(a: float >= 0) */

$(document).ready(function() {
    $('#inputdistribution').change(function() {
        $('#numberinput').empty();
        if ($('#inputdistribution').val() == 'exponential' || $('#inputdistribution').val() == 'geometric' || $('#inputdistribution').val() == 'poisson') {
            $('#numberinput').append("<div class='form-group'><label class='col-form-label text-muted unselectable'>Введите число:</label><input type='number' class='form-control bg-white text-dark' id='distribution-param-1' name='distribution-param-1'></div>");
            }
        else if  ($('#inputdistribution').val() == 'beta' || $('#inputdistribution').val() == 'binomial' || $('#inputdistribution').val() == 'gamma' || $('#inputdistribution').val() == 'laplace' || $('#inputdistribution').val() == 'logistic' || $('#inputdistribution').val() == 'lognormal' || $('#inputdistribution').val() == 'negative_binomial' || $('#inputdistribution').val() == 'normal' || $('#inputdistribution').val() == 'uniform') {
            for (let i = 0; i < 2; i++) {
                $('#numberinput').append("<div class='form-group'><label class='col-form-label text-muted unselectable'>Введите " + (i+1) + " число:</label><input type='number' class='form-control bg-white text-dark' id='distribution-param-" + (i+1) + "' name='distribution-param-" + (i+1) + "'></div>");
                }
            }
        else if ($('#inputdistribution').val() == 'hypergeometric' || $('#inputdistribution').val() == 'triangular') {
            for (let i = 0; i < 3; i++) {
                $('#numberinput').append("<div class='form-group'><label class='col-form-label text-muted unselectable'>Введите " + (i+1) + " число:</label><input type='number' class='form-control bg-white text-dark' id='distribution-param-" + (i+1) + "' name='distribution-param-" + (i+1) + "'></div>");
                }
            }
        else if ($('#inputdistribution').val() == 'geodata') {
            $('#numberinput').append("<div class='form-group'><label class='col-form-label text-muted unselectable'>Широта:</label><input type='number' class='form-control bg-white text-dark' id='distribution-param-1' name='distribution-param-1'></div>");
            $('#numberinput').append("<div class='form-group'><label class='col-form-label text-muted unselectable'>Долгота:</label><input type='number' class='form-control bg-white text-dark' id='distribution-param-2' name='distribution-param-2'></div>");
            $('#numberinput').append("<div class='form-group'><label class='col-form-label text-muted unselectable'>Радиус:</label><input type='number' class='form-control bg-white text-dark' id='distribution-param-3' name='distribution-param-3'></div>");
            $('#outliers-form').empty();
            }
        });
});

$(document).ready(function() {
    $('input[name="Radio"]').on('click', function() {
        $('.radioinput').empty();
        if ($('input[name="Radio"]:checked').val() == 1) {
            $('.radioinput').append("<div class='form-group mt-1'><label class='col-form-label text-muted unselectable'>Количество строк:</label><input type='number' class='form-control bg-white text-dark' name='sensor-create-lines' id='sensor-create-lines'></div>");
            $('.datetime-picker').css('display', 'none');
            document.getElementById("sensor-create-time-start").required = false;
            document.getElementById("sensor-create-time-stop").required = false;
            document.getElementById("sensor-create-time-period-days").required = false;
            document.getElementById("sensor-create-time-period-time").required = false;
        }
        else if ($('input[name="Radio"]:checked').val() == 2) {
            // $('#radioinput').append('<div class="form-row mt-1"><div class="form-group col-md-4"><div class="form-group"><label class="col-form-label text-muted unselectable">Начало:</label><input type="text" class="form-control bg-white text-dark" id="name"></div></div><div class="form-group col-md-4"><div class="form-group"><label for="name" class="col-form-label text-muted unselectable">Конец:</label><input type="text" class="form-control bg-white text-dark" id="name"></div></div><div class="form-group col-md-4"><div class="form-group"><label for="name" class="col-form-label text-muted unselectable">Период:</label><input type="text" class="form-control bg-white text-dark" id="name"></div></div>');
            $('.datetime-picker').css('display', 'flex');
            document.getElementById("sensor-create-time-start").required = true;
            document.getElementById("sensor-create-time-stop").required = true;
            document.getElementById("sensor-create-time-period-days").required = true;
            document.getElementById("sensor-create-time-period-time").required = true;
        }
    });
});

$(document).ready(function() {
    $('input[name="Radio2"]').on('click', function() {
        $('#radioinput2').empty();
        if ($('input[name="Radio2"]:checked').val() == 3) {
            $('#radioinput2').append("<div class='form-group mt-1'><label for='name' class='col-form-label text-muted unselectable'>Количество строк:</label><input type='text' class='form-control bg-white text-dark' id='name'></div>");
            $('.datetime-picker').css('display', 'none');
            document.getElementById("sensor-create-time-start").required = false;
            document.getElementById("sensor-create-time-stop").required = false;
            document.getElementById("sensor-create-time-period-days").required = false;
            document.getElementById("sensor-create-time-period-time").required = false;
        }
        else if ($('input[name="Radio2"]:checked').val() == 4) {
            $('.datetime-picker').css('display', 'flex');
            document.getElementById("sensor-create-time-start").required = true;
            document.getElementById("sensor-create-time-stop").required = true;
            document.getElementById("sensor-create-time-period-days").required = true;
            document.getElementById("sensor-create-time-period-time").required = true;
        }
    });
});

// $(document).ready(function() {
//     $('#project-sumbit').on("click", function() {
//         $('.project').append('<h3 class="h3 unselectable" style="display: inline-block;">' + $("#project-name").val() + '</h3>');
//         $('#project-header').append('<span class="span1 unselectable">' + $("#project-text").val() + '</span>');
//         $('#togglemodal1').modal('hide');
//         $('#togglemodal1').on('hidden.bs.modal', function () {
//             $(this).find("input,textarea").val('').end();
//         });
//         });
// });

/* + document.forms["deviceform"].elements["devicename"].value + */

// $(document).ready(function() {
//     $('#device-sumbit').on("click", function() {
//         $('.div-device').append('<h4 class="h4 mb-3 unselectable">' + $("#device-name").val() + '</h4><span class="span1 unselectable" style="display: block;">'  + $("#device-text").val() +  '</span>');
//         $('.div-device').append('<div class="text-right"><a href="#" style="text-decoration: none;"><i class="fas fa-arrow-circle-right" style="color: #FFC107; border: 0; font-size: 32px; line-height: 38px;"></i></a></div>');
//         $('#togglemodal2').modal('hide');
//         $('#togglemodal2').on('hidden.bs.modal', function () {
//             $(this).find("input,textarea").val('').end();
//         });
//         });
// });

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var clicked=false;//Global Variable

function ClickLogin()
{
    clicked=true;
}

function onSignIn(googleUser) {
    if (clicked) {
        var csrftoken = getCookie('csrftoken');
        var id_token = googleUser.getAuthResponse().id_token;
        console.log(id_token);
        console.log(csrftoken);
        var xhr = new XMLHttpRequest();

        xhr.open('POST', '/api/tokensign/');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.setRequestHeader('x-csrf-token', csrftoken);
        xhr.onload = function () {
            console.log('Signed in as: ' + xhr.responseText);
            location.reload();
        };
        xhr.send('idtoken=' + id_token);
    }
}

function onLoad() {
      gapi.load('auth2', function() {
          gapi.auth2.init();
      });
}

function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });
    window.location.replace("/logout/");
}

function showSensors(device_id, device_name) {
    var xhr = new XMLHttpRequest();
    $('#sensors-box').empty();

    xhr.open('GET', '/api/get_sensors/' + device_id);
    xhr.onload = function () {
        var data = JSON.parse(JSON.parse(xhr.response));
        var additionalHtml = "";

        for (var i = 0; i < data.length; i++) {
            additionalHtml += "<div class=\"div-sensor mr-3 mb-3 px-3 pt-4 pb-3\">";
            additionalHtml += "<div>";
            additionalHtml += "<span class=\"col-form-label text-muted unselectable\">Датчик</span>";
            additionalHtml += "<div style=\"float: right\">";
            additionalHtml += "<a class=\"mr-1\" href=\"#\" style=\"text-decoration: none;\">";
            additionalHtml += "<i class=\"far fa-edit text-muted\" style=\"color: #6C757D; border: 0;\"></i>";
            additionalHtml += "</a>";
            additionalHtml += "<a href=\"#\" style=\"text-decoration: none;\" onclick='deleteSensor(" + data[i]['pk'] + ", " + device_id + ", \"" + device_name + "\")'>";
            additionalHtml += "<i class=\"far fa-trash-alt text-muted\" style=\"color: #6C757D; border: 0;\"></i>";
            additionalHtml += "</a>";
            additionalHtml += "</div>";
            additionalHtml += "</div>";
            additionalHtml += "<h4 class=\"h4 mt-1 mb-5 unselectable\">" + data[i]['fields']['sensor_name'] +"</h4>";
            additionalHtml += "<div class=\"text-right mt-5\">";
            additionalHtml += "<a onclick=\"generate(" + data[i]['pk'] + ")\" role=\"button\" data-toggle=\"modal\" data-target=\"#togglemodal4\" style=\"text-decoration: none;\">";
            additionalHtml += "<i class=\"fas fa-arrow-circle-right\" style=\"color: rgb(255, 255, 255); border: 0; font-size: 32px;\"></i>";
            additionalHtml += "</a>";
            additionalHtml += "</div>";
            additionalHtml += "</div>";
            // additionalHtml += "";
        }

        additionalHtml += "</div>";
        additionalHtml += "</div>";
        $('#sensors-box').append(additionalHtml);

        // $('#sensor-submit').on('click',function(){
        //     addSensor(device_id, device_name);
        // });
        $('#sensor-submit').unbind('click').click(function(){addSensor(device_id, device_name);});
    };
    xhr.send();


    $('#sensors-device-name').html(device_name);


}

function deleteSensor(sensor_id, device_id, device_name) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/delete_sensor/'+sensor_id);
    xhr.onload = function () {
        showSensors(device_id, device_name);
    };
    xhr.send();
}

function generate(sensor_id) {
    // $(".loader_inner").fadeIn();
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/generate/' + sensor_id);
    xhr.onload = function () {
        $("#modal-plot").css('display', 'none');
        $("#loader").fadeOut(1000, function () {
            $('#download-data-csv').removeClass('disabled').attr('href', '/static/userfiles/'+xhr.responseText+'.csv');
            $('#modal-plot').attr('src', '/static/img/'+xhr.responseText+'.png').css('display', 'block');
        });
        // $('#download-data-csv').href(xhr.responseText);
    };
    xhr.send();
}

function closeModalSensor() {
    console.log('a');
    $("#loader").fadeIn();
    $('#download-data-csv').addClass('disabled').attr('href', '#');
    $('#modal-plot').css('display', 'none');
}

function addSensor(device_id, device_name) {
    var xhr = new XMLHttpRequest();

    var values = {};
    $.each($('#sensor-form').serializeArray(), function(i, field) {
        values[field.name] = field.value;
    });

    console.log(JSON.stringify(values));

    xhr.open('POST', '/api/create_sensor/'+device_id+'/');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function () {
        showSensors(device_id, device_name);
        $('#togglemodal3').modal('hide');
    };
    xhr.send(JSON.stringify(values));

}

/* $(document).ready(function() {
    $('#project-edit, #device-edit').one("click", function() {; */

