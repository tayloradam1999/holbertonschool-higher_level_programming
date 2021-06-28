#!/usr/bin/node
/* adds class <red> to header element on click */

$("DIV#red_header").click(function(){
    $('header').addClass('red');
});
