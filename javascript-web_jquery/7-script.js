$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data, status) => {
    $('div#character').text(JSON.parse(data));
  });
});
