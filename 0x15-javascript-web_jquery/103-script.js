document.addEventListener('DOMContentLoaded', function () {
  $(function () {
    $.ajax({
      type: 'GET',
      url: 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:city_name%22)&format=json',
      success: function (data) {
        $('INPUT#btn_search').click(function () {
          let input = $('INPUT#city_search').val();
          if (input) {
            $('DIV#wind_speed').text(data.query.results.channel.wind.speed);
          }
        });

        $('INPUT#city_search').keypress(function (e) {
          if (e.which == 13) {
            $('INPUT#btn_search').click();
          }
        });
      }
    });
  });
});
