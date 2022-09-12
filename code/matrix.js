//get canvas node and the drawing context
const canvas = document.getElementById('canv');
const ctx = canvas.getContext("2d");

//set the width and height of the canvas
const w = canvas.width = document.body.offsetWidth;
const h = canvas.height = document.body.offsetHeight;

//draw a balck rectangle the same size of the canvas
ctx.fillStyle = "#000";
ctx.fillRect = (0, 0, w, h);

