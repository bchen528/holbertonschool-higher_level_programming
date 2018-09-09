document.addEventListener('DOMContentLoaded', function () {
  $(function () {
    $('INPUT#btn_search').click(function () {
      $.ajax({
        type: 'GET',
        url: 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22' + $('INPUT#city_search').val() + '%22)&format=json',
        success: function (data) {
          let input = $('INPUT#city_search').val();
          if (input) {
            $('DIV#wind_speed').text(data.query.results.channel.wind.speed);
          }
        }
      });
    });
  });
});
