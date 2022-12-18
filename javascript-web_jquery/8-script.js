$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, status) => {
    const titles = data.results.map(movie => movie.title);
    titles.forEach(title => $('ul#list_movies').append(`<li>${title}</li>`));
    console.log(titles);
  });
});
