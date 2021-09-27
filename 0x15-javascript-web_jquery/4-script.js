#!/usr/bin/node
/* toggles header element between red and green on click */

$('#toggle_header').click(function () {
	$("header").toggleClass("red");
	$("header").toggleClass("green");
});
