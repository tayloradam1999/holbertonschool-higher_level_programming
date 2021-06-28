#!/usr/bin/node
/* Fetches value of 'hello' from URL DIV#hello */
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
    $('DIV#hello').html(data.hello);
});
