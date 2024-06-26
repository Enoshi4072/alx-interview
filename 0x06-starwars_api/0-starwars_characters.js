#!/usr/bin/node

const request = require('request');

// Function to fetch and print Star Wars characters based on movie ID
function getStarWarsCharacters (movieId) {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Unexpected status code:', response.statusCode);
    } else {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;

      // Fetch and print character names synchronously
      fetchAndPrintCharacters(characters, 0);
    }
  });
}

// Function to fetch and print characters synchronously
function fetchAndPrintCharacters (characters, index) {
  if (index >= characters.length) {
    return; // Stop recursion if all characters are printed
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Unexpected status code:', response.statusCode);
    } else {
      const characterData = JSON.parse(body);
      console.log(characterData.name);

      // Fetch and print next character
      fetchAndPrintCharacters(characters, index + 1);
    }
  });
}

// Get movie ID from command-line argument
const movieId = process.argv[2];

// Ensure movie ID is provided
if (!movieId) {
  console.error('Please provide a movie ID.');
  process.exit(1);
}

// Call function to fetch and print characters
getStarWarsCharacters(movieId);
