$(function () {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', (data, status) => {
    $('div#hello').text(data.hello);
  });
});
