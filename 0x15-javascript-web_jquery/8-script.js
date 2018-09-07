$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/films/?format=json',
    success: function (data) {
      // console.log('success', data.results);
      $.each(data.results, function (i, movie) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
