#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (error, data) => {
  if (error) { console.log(error); }
  console.log(JSON.parse(data.body).title);
});
