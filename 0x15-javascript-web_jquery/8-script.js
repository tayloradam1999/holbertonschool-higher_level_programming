#!/usr/bin/node
/* Fetches and lists titles of all moves from specified URL */
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
    $.each(data.results, function(title, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
    });
});
