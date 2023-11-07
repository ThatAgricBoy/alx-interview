#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];
request(url + movieId, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    try {
      const movieData = JSON.parse(body);
      if (Array.isArray(movieData.characters)) {
        movieData.characters.forEach((character) => {
          request(character, function (error, response, body) {
            if (error) {
              console.log(error);
            } else {
              console.log(JSON.parse(body).name);
            }
          });
        });
      } else {
        console.log("No characters found in this movie.");
      }
    } catch (parseError) {
      console.log("Error parsing JSON response:", parseError);
    }
  }
});
