$(document).ready(function getCharacter () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function apiName (data) {
    $('#character').text(data.name);
  });
});
