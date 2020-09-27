$(document).ready(function changeRed () {
  $('DIV#toggle_header').click(function toogleHeader () {
    if ($('HEADER').attr('class') !== 'red') {
      $('HEADER').attr('class', 'red');
    } else {
      $('HEADER').attr('class', 'green');
    }
  });
});
