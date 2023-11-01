$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('#hello').text('Translation of "hello": ' + data.hello);
  });
});
