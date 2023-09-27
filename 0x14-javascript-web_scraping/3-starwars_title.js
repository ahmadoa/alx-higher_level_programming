#!/usr/bin/node

const request = require('request');
const epNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + epNum, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
