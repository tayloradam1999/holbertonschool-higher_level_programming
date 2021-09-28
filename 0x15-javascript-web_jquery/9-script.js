#!/usr/bin/node
/* Fetches value of 'hello' from URL */
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
    $('#hello').html(data.hello);
});
