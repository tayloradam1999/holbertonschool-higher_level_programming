#!/usr/bin/node
/* Fetches character name from URL */

const myUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
$.get(myUrl, function(data){
    $('DIV#character').html(data.name);
});
