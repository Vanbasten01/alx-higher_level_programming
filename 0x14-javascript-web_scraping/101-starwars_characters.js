#!/usr/bin/node

const args = process.argv;
const request = require('request');

function fetchCharacters () {
  request(`https://swapi-api.alx-tools.com/api/films/${args[2]}`, { json: true }, (error, response, film) => {
    if (error) {
      console.error(error);
    } else {
      const characters = film.characters;
      fetchCharacterNames(characters, 0);
    }
  });
}

function fetchCharacterNames (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], { json: true }, (error, response, character) => {
    if (error) {
      console.error(error);
    } else {
      console.log(character.name);
      fetchCharacterNames(characters, index + 1);
    }
  });
}

fetchCharacters();
