#!/usr/bin/node
exports.esrever = function (list) {
    const myList = [];
    for (let x = list.length - 1; x >= 0; x--) {
        myList.push(list[x]);
    }
    return myList;
}
