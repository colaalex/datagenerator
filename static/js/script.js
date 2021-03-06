/*
 * Инициализация moment.js для datetimepicker'a
 */
moment().format();

/* То, что видит пользователь */
/*
 * Иконки для datetimepicker'a
 */
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
    } 
});

/*
 * Show-sensors-box, вызывает и скрывает окно датчиков
 */
$(document).ready(function (){
    $('.show-sensors').on('click', function(){
        $('.box').addClass('open');
    });
    $('#2').on('click', function(){
        $('.box').removeClass('open');
    });
});

/*
 * datetimepicker-sensor: формат отображения даты и времени и зависимость между началом отсчета и его концом
 */
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

/*
 * Аналогичное, но уже datetimepicker-device
 */
$(function () {
    $('#datetimepicker6').datetimepicker({
        locale: 'ru',
        format: 'HH mm ss'
    });
    $('#datetimepicker4').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',
        locale: 'ru'
    }
    );
    $('#datetimepicker5').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',
        locale: 'ru',
        useCurrent: false
    });
    $("#datetimepicker4").on("change.datetimepicker", function (e) {
        $('#datetimepicker5').datetimepicker('minDate', e.date);
    });
    $("#datetimepicker5").on("change.datetimepicker", function (e) {
        $('#datetimepicker4').datetimepicker('maxDate', e.date);
    });
});

/*
 * Аналогичное, но уже datetimepicker-report
 */
$(function () {
    $('#datetimepicker7').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',
        locale: 'ru'
    });
    $('#datetimepicker8').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',
        locale: 'ru',
        useCurrent: false
    });
    $("#datetimepicker7").on("dp.change", function (e) {
        $('#datetimepicker8').data("DateTimePicker").minDate(e.date);
    });
    $("#datetimepicker8").on("dp.change", function (e) {
        $('#datetimepicker7').data("DateTimePicker").maxDate(e.date);
    });
});

/*
 * inputdistribution-picker: отображение правильного количества вводимых полей при выборе определенного типа распределения
 */
$(document).ready(function() {
    $('#inputdistribution').change(function() {
        $('#numberinput').empty();
        if ($('#inputdistribution').val() == 'exponential' || $('#inputdistribution').val() == 'geometric' || $('#inputdistribution').val() == 'poisson') {
            $('#numberinput').append("<div class='form-group'><label class='col-form-label text-muted unselectable'>Введите число:</label><input type='number' class='form-control bg-white text-dark' id='distribution-param-1' name='distribution-param-1'></div>");
            }
        else if  ($('#inputdistribution').val() == 'temperature' || $('#inputdistribution').val() == 'beta' || $('#inputdistribution').val() == 'binomial' || $('#inputdistribution').val() == 'gamma' || $('#inputdistribution').val() == 'laplace' || $('#inputdistribution').val() == 'logistic' || $('#inputdistribution').val() == 'lognormal' || $('#inputdistribution').val() == 'negative_binomial' || $('#inputdistribution').val() == 'normal' || $('#inputdistribution').val() == 'uniform') {
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

/*
 * radioinput-picker: отображание определенных полей в зависимости от выбора пользователя в радиокнопке
 */
$(document).ready(function() {
    $('input[name="Radio"]').on('click', function() {
        $('#radioinput').empty();
        if ($('input[name="Radio"]:checked').val() == 1) {
            $('#radioinput').append("<div class='form-group mt-1'><label class='col-form-label text-muted unselectable'>Количество строк:</label><input type='number' class='form-control bg-white text-dark' name='sensor-create-lines' id='sensor-create-lines'></div>");
            $('#datetime-picker').css('display', 'none');
            document.getElementById("sensor-create-time-start").required = false;
            document.getElementById("sensor-create-time-stop").required = false;
            document.getElementById("sensor-create-time-period-days").required = false;
            document.getElementById("sensor-create-time-period-time").required = false;
        }
        else if ($('input[name="Radio"]:checked').val() == 2) {
            // $('#radioinput').append('<div class="form-row mt-1"><div class="form-group col-md-4"><div class="form-group"><label class="col-form-label text-muted unselectable">Начало:</label><input type="text" class="form-control bg-white text-dark" id="name"></div></div><div class="form-group col-md-4"><div class="form-group"><label for="name" class="col-form-label text-muted unselectable">Конец:</label><input type="text" class="form-control bg-white text-dark" id="name"></div></div><div class="form-group col-md-4"><div class="form-group"><label for="name" class="col-form-label text-muted unselectable">Период:</label><input type="text" class="form-control bg-white text-dark" id="name"></div></div>');
            $('#datetime-picker').css('display', 'flex');
            document.getElementById("sensor-create-time-start").required = true;
            document.getElementById("sensor-create-time-stop").required = true;
            document.getElementById("sensor-create-time-period-days").required = true;
            document.getElementById("sensor-create-time-period-time").required = true;
        }
    });
});

/*
 * radio2input-picker: аналогично верхнему
 */
$(document).ready(function() {
    $('input[name="Radio2"]').on('click', function() {
        $('#radioinput2').empty();
        if ($('input[name="Radio2"]:checked').val() == 3) {
            $('#radioinput2').append("<div class='form-group mt-1'><label class='col-form-label text-muted unselectable'>Количество строк:</label><input type='number' class='form-control bg-white text-dark' name='sensor-create-lines' id='sensor-create-lines'></div>");
            $('#datetime-picker2').css('display', 'none');
            document.getElementById("sensor-create-time-start").required = false;
            document.getElementById("sensor-create-time-stop").required = false;
            document.getElementById("sensor-create-time-period-days").required = false;
            document.getElementById("sensor-create-time-period-time").required = false;
        }
        else if ($('input[name="Radio2"]:checked').val() == 4) {
            $('#datetime-picker2').css('display', 'flex');
            document.getElementById("sensor-create-time-start").required = true;
            document.getElementById("sensor-create-time-stop").required = true;
            document.getElementById("sensor-create-time-period-days").required = true;
            document.getElementById("sensor-create-time-period-time").required = true;
        }
    });
});

/*
 * toggle-popover: контент, который находится в знаке «popover», который меняется в зависимости от выбора пользователя
 */
$(document).ready(function () {
    $('[data-toggle="popover"]').popover()
    $('#inputdistribution').change(function() {
        if ($('#inputdistribution').val() == 'beta') { $('#distribution-popover').attr('data-content', 'a: float, b: float') }
        else if ($('#inputdistribution').val() == 'binomial') { $('#distribution-popover').attr('data-content', 'n: int >= 0, p: float >= 0') }
        else if ($('#inputdistribution').val() == 'exponential') { $('#distribution-popover').attr('data-content', 'scale: float >= 0') }
        else if ($('#inputdistribution').val() == 'gamma') { $('#distribution-popover').attr('data-content', 'k: float >= 0, theta: float >= 0') }
        else if ($('#inputdistribution').val() == 'geometric') { $('#distribution-popover').attr('data-content', 'p: float >= 0') }
        else if ($('#inputdistribution').val() == 'hypergeometric') { $('#distribution-popover').attr('data-content', 'ngood: int >= 0, nbad: int >= 0, nall: int 1<=nall<=ngood+nbad') }
        else if ($('#inputdistribution').val() == 'laplace') { $('#distribution-popover').attr('data-content', 'mean: float, scale: float >=0') }
        else if ($('#inputdistribution').val() == 'logistic') { $('#distribution-popover').attr('data-content', 'mean: float, scale: float >= 0') }
        else if ($('#inputdistribution').val() == 'lognormal') { $('#distribution-popover').attr('data-content', 'mean: float, std: float >= 0') }
        else if ($('#inputdistribution').val() == 'negative_binomial') { $('#distribution-popover').attr('data-content', 'n: int > 0, p: float 0<=p<=1') }
        else if ($('#inputdistribution').val() == 'normal') { $('#distribution-popover').attr('data-content', 'mean: float, std: float >= 0') }
        else if ($('#inputdistribution').val() == 'poisson') { $('#distribution-popover').attr('data-content', 'lam: float > 0') }
        else if ($('#inputdistribution').val() == 'triangular') { $('#distribution-popover').attr('data-content', 'left: float, top: float >= left, right: float >= top') }
        else if ($('#inputdistribution').val() == 'uniform') { $('#distribution-popover').attr('data-content', 'left: float, right: float > left') }
        else if ($('#inputdistribution').val() == 'geodata') { $('#distribution-popover').attr('data-content', 'lat: float -90≤lat≤90; long: float -180≤long≤180; radius: float radius≥0') }
        else if ($('#inputdistribution').val() == 'temperature') { $('#distribution-popover').attr('data-content', 'mean: float, scale: float >=0') }
        else $('#distribution-popover').attr('data-content', 'Выберите распределение и снова наведите на меня :)')
    });
});

/* Авторизация через Google-аккаунт */
/*
 * getCookie: получает куки-файлы
 */
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

/*
 * Авторизация при помощи Google-сервисов
 */
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

/* Взаимодействие с бэкендом */
/*
 * showSensors: при помощи GET-запроса получает данные об определенном устройстве (полученную строку переводит в объекты) для того, чтобы отображать датчики для этого устройства
 */
function showSensors(device_id, device_name) {
    var xhr = new XMLHttpRequest();
    $('#sensors-box').empty();

    xhr.open('GET', '/api/get_sensors/' + device_id);
    xhr.onload = function () {
        var data = JSON.parse(JSON.parse(xhr.response));
        var additionalHtml = "";

        for (var i = 0; i < data.length; i++) {
            additionalHtml += "<div class=\"div-sensor mr-3 mb-3 px-3 pt-4 pb-3\" style=\"overflow-y: auto;\">";
            additionalHtml += "<div>";
            additionalHtml += "<span class=\"col-form-label text-muted unselectable\">Датчик</span>";
            additionalHtml += "<div style=\"float: right\">";
            additionalHtml += "<a href=\"#\" style=\"text-decoration: none;\" onclick='deleteSensor(" + data[i]['pk'] + ", " + device_id + ", \"" + device_name + "\")'>";
            additionalHtml += "<i class=\"far fa-trash-alt text-muted\" style=\"color: #6C757D; border: 0;\"></i>";
            additionalHtml += "</a>";
            additionalHtml += "</div>";
            additionalHtml += "</div>";
            additionalHtml += "<h4 style='word-wrap: break-word;' class=\"h4 mt-1 mb-5 unselectable\"'>" + data[i]['fields']['sensor_name'] +"</h4>";
            additionalHtml += "<div class=\"text-right mt-5\">";
            additionalHtml += "<a onclick=\"generate(" + data[i]['pk'] + ")\" role=\"button\" data-toggle=\"modal\" data-target=\"#togglemodal4\" style=\"text-decoration: none;\">";
            additionalHtml += "<i class=\"fas fa-arrow-circle-right\" style=\"color: #000000; border: 0; font-size: 32px;\"></i>";
            additionalHtml += "</a>";
            additionalHtml += "</div>";
            additionalHtml += "</div>";
        }

        additionalHtml += "</div>";
        additionalHtml += "</div>";
        $('#sensors-box').append(additionalHtml);
        $('#sensor-submit').unbind('click').click(function(){addSensor(device_id, device_name);});
    };
    xhr.send();


    $('#sensors-device-name').html(device_name);


}

/*
 * deleteSensor: при нажатии на кнопку удаления, отправляет GET-запрос для удаления датчика (из базы данных в том числе)
 */
function deleteSensor(sensor_id, device_id, device_name) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/delete_sensor/'+sensor_id);
    xhr.onload = function () {
        showSensors(device_id, device_name);
    };
    xhr.send();
}

/*
 * plotGeneratedData: процедура отрисовки графика
 */
function plotGeneratedData(data) {
    var x = [];
    for (var i = 0; i < data.length; i++) {
        for (let [key, value] of Object.entries(data[i])) {
            if (!(key === 'Time')) {
                x.push(value);
            }
        }
    }
    var trace = {
        x: x,
        type: 'histogram',
    };
    Plotly.newPlot('modal-plot', [trace]);
    $('#modal-plot').css('display', 'block');
}

/*
 * generate: при нажатии на кнопку просмотра данных, отправляет GET-запрос для получения сгенерированных данных для датчика (график, возможность загрузить .csv-файл и пр.)
 */
function generate(sensor_id) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/generate/' + sensor_id);
    xhr.onload = function () {
        $("#modal-plot").css('display', 'none');
        $("#loader").fadeOut(1000, function () {
            $('#download-data-csv').removeClass('disabled').attr('href', '/static/userfiles/'+xhr.responseText+'.csv');
            Plotly.d3.csv('/static/userfiles/'+xhr.responseText+'.csv', function (data) {plotGeneratedData(data)});
        });
    };
    xhr.send();
}

/*
 * closeModalSensor: сброс форм до начального состояния
 */
function closeModalSensor() {
    console.log('a');
    $("#loader").fadeIn();
    $('#download-data-csv').addClass('disabled').attr('href', '#');
    $('#modal-plot').css('display', 'none');
}

/*
 * addSensor: отправляет POST-запрос с целью добавления датчика в базу данных, а также последующее отображение всех датчиков, привязанных к этому устройству
 */ 
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

/*
 * modalGenerateDeviceData: запрашивает с помощью POST-запроса генерацию данных для всего устройства, с последующей загрузкой
 */
function modalGenerateDeviceData(device_id) {
    $('#generate-device-data-csv').on('click', function () {
        $("#download-device-csv").text("Ждите");
        $("#generate-device-data-csv").addClass('disabled');

        var xhr = new XMLHttpRequest();
        var values = {};
        $.each($('#generator-device-form').serializeArray(), function(i, field) {
            values[field.name] = field.value;
        });
        console.log(values);
        console.log(device_id);
        xhr.open('POST', '/api/generate_device/'+device_id+'/');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function () {
            $("#download-device-csv").attr('href', '/static/userfiles/'+xhr.responseText+'.csv').removeClass('disabled').text('Загрузить файл');
        };
        xhr.send(JSON.stringify(values));
    })
}

/*
 * closeModalGenerateDeviceData: сброс форм до начального состояния
 */
function closeModalGenerateDeviceData() {
    $("#generate-device-data-csv").removeClass('disabled');
    $("#download-device-csv").addClass('disabled');
    $('#generate-device-data-csv').unbind('click');
}

/*
 * editProject: функция, реализующие изменение данных о проектах
 */
function editProject(project_id) {
    $("#staticBackdropLabel").text('Изменить проект');
    $("#project-name").val($("#project-name-label").text());
    $("#project-text").val($("#project-text-label").text());
    $("#project-sumbit").text("Изменить");
    $("#project-form").attr('action', '/api/edit_project/'+project_id+'/');
}

/*
 * closeModalEditProject: сброс форм до начального состояния
 */
function closeModalEditProject() {
    $("#staticBackdropLabel").text('Создать новый проект');
    $("#project-name").val("");
    $("#project-text").val("");
    $("#project-sumbit").text("Создать");
    $("#project-form").attr('action', '/api/create_project/');
}

/*
 * editDevice: функция, реализующие изменение данных об устройствах
 */
function editDevice(device_id) {
    $("#staticBackdropLabel2").text('Изменить устройство');
    $('#device-name').val($("#device-name-label").text());
    $('#device-text').val($('#device-text-label').text());
    $('#device-sumbit').text('Изменить');
    $('#device-form').attr('action', '/api/edit_device/'+device_id+'/');
}

/*
 * closeModalEditDevice: сброс форм до начального состояния
 */
function closeModalEditDevice(project_id) {
    $("#staticBackdropLabel2").text('Создать новое устройство');
    $('#device-name').val("");
    $('#device-text').val("");
    $('#device-sumbit').text('Создать');
    $('#device-form').attr('action', '/api/create_device/'+project_id+'/');
}
