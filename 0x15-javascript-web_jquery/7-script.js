const $ = window.$;
// Semistandart sucks
fetch('https://swapi.co/api/people/5/?format=json')
  .then(res => res.json())
  .then(res => {
    $('#character').html(res.name);
  });
