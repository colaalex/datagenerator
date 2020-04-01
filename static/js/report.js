$(window).on('load', function () {
    $("#loader-bg").fadeOut("200");
    // $("#loader").fadeOut("slow");
});

function buildPlot(report_id) {
    var sid = $('#inputState').val();
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/plot_data/'+report_id+'/'+sid+'/');
    xhr.onload = function () {
        var data = xhr.responseText;
        console.log(data);
        console.log(typeof data);
        Plotly.newPlot('report-plot', JSON.parse(data));
    };
    xhr.send();
}