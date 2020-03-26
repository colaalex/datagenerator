$(document).ready(function(){
    $('#show-sensors').on('click', function(){
        $('.box').addClass('open');
    });
    $('#2').on('click', function(){
        $('.box').removeClass('open');
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
        if ($('#inputdistribution').val() == 'exponential' || $('#inputdistribution').val() == 'geometric' || $('#inputdistribution').val() == 'logarithmic' || $('#inputdistribution').val() == 'poisson' || $('#inputdistribution').val() == 'weibull') {
            $('#numberinput').append("<div class='form-group'><label for='name' class='col-form-label text-muted unselectable'>Введите число:</label><input type='text' class='form-control bg-white text-dark' id='name'></div>");
            }
        else if  ($('#inputdistribution').val() == 'beta' || $('#inputdistribution').val() == 'binomial' || $('#inputdistribution').val() == 'gamma' || $('#inputdistribution').val() == 'laplace' || $('#inputdistribution').val() == 'logistic' || $('#inputdistribution').val() == 'lognormal' || $('#inputdistribution').val() == 'multinomial' || $('#inputdistribution').val() == 'negative_binomial' || $('#inputdistribution').val() == 'normal' || $('#inputdistribution').val() == 'uniform') {
            for (let i = 0; i < 2; i++) {
                $('#numberinput').append("<div class='form-group'><label for='name' class='col-form-label text-muted unselectable'>Введите " + (i+1) + " число:</label><input type='text' class='form-control bg-white text-dark' id='name'></div>");
                }
            }
        else if ($('#inputdistribution').val() == 'hypergeometric' || $('#inputdistribution').val() == 'triangular') {
            for (let i = 0; i < 3; i++) {
                $('#numberinput').append("<div class='form-group'><label for='name' class='col-form-label text-muted unselectable'>Введите " + (i+1) + " число:</label><input type='text' class='form-control bg-white text-dark' id='name'></div>");
                }
            }
        });
});

$(document).ready(function() {
    $('input[name="Radio"]').on('click', function() {
        $('#radioinput').empty();
        if ($('input[name="Radio"]:checked').val() == 1) {
            $('#radioinput').append("<div class='form-group mt-1'><label for='name' class='col-form-label text-muted unselectable'>Количество строк:</label><input type='text' class='form-control bg-white text-dark' id='name'></div>");
        }
        else if ($('input[name="Radio"]:checked').val() == 2) {
            $('#radioinput').append('<div class="form-row mt-1"><div class="form-group col-md-4"><div class="form-group"><label for="name" class="col-form-label text-muted unselectable">Начало:</label><input type="text" class="form-control bg-white text-dark" id="name"></div></div><div class="form-group col-md-4"><div class="form-group"><label for="name" class="col-form-label text-muted unselectable">Конец:</label><input type="text" class="form-control bg-white text-dark" id="name"></div></div><div class="form-group col-md-4"><div class="form-group"><label for="name" class="col-form-label text-muted unselectable">Период:</label><input type="text" class="form-control bg-white text-dark" id="name"></div></div>');
        }
    });
});

$(document).ready(function() {
    $('#project-sumbit').on("click", function() {
        $('.project').append('<h3 class="h3 unselectable" style="display: inline-block;">' + $("#project-name").val() + '</h3>');
        $('#project-header').append('<span class="span1 unselectable">' + $("#project-text").val() + '</span>');
        $('#togglemodal1').modal('hide');
        $('#togglemodal1').on('hidden.bs.modal', function () {
            $(this).find("input,textarea").val('').end();
        });
        });
});

/* + document.forms["deviceform"].elements["devicename"].value + */

$(document).ready(function() {
    $('#device-sumbit').on("click", function() {
        $('.div-device').append('<h4 class="h4 mb-3 unselectable">' + $("#device-name").val() + '</h4><span class="span1 unselectable" style="display: block;">'  + $("#device-text").val() +  '</span>');
        $('.div-device').append('<div class="text-right"><a href="#" style="text-decoration: none;"><i class="fas fa-arrow-circle-right" style="color: #FFC107; border: 0; font-size: 32px; line-height: 38px;"></i></a></div>');
        $('#togglemodal2').modal('hide');
        $('#togglemodal2').on('hidden.bs.modal', function () {
            $(this).find("input,textarea").val('').end();
        });
        });
});

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

        xhr.open('POST', 'http://localhost:1337/api/tokensign/');
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

/* $(document).ready(function() {
    $('#project-edit, #device-edit').one("click", function() {; */
