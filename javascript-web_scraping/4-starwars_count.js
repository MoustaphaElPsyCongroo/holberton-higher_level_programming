#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url, (error, response, body) => {
  if (error) throw error;

  const films = JSON.parse(body).results;
  const wedgeFilms = films.filter(film => film.characters.some(characters => characters.includes('/18')));
  console.log(wedgeFilms.length);
});
