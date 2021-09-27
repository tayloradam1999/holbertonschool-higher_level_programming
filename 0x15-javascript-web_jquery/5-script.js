#!/usr/bin/node
/* adds item to list on click */

$('#add_item').click(function () {
	$('.my_list').append("<li>Item</li>");
});
