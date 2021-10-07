const c = document.getElementById('canvas');
const ctx = c.getContext('2d');

let slider = document.getElementById('snowflakes');
let snowflakeCount = document.getElementById('numOfFlakes');

snowflakeCount.innerText = slider.value;
let maxFlakes = slider.value; // max number of snowflakes on screen
let flakes = [];

slider.addEventListener('change', () => {
	snowflakeCount.innerText = slider.value;
	maxFlakes = slider.value;
	flakes = [];
});

// Canvas Dimensions
let width = window.innerWidth;
let height = window.innerHeight;

c.width = width;
c.height = height;

const flakePos = (maxFlakes) => {
	for (let i = 0; i < maxFlakes; i++) {
		flakes.push({
			x: Math.random() * width, // x-coord
			y: Math.random() * height, // y-coord
			r: Math.random() * 5 + 2, // radius
			d: Math.random() * maxFlakes, // density
		});
	}
};

/* let maxFlakes = 55; // max number of snowflakes on screen
let flakes = []; */

/* for (let i = 0; i < maxFlakes; i++) {
	flakes.push({
		x: Math.random() * width, // x-coord
		y: Math.random() * height, // y-coord
		r: Math.random() * 5 + 2, // radius
		d: Math.random() * maxFlakes, // density
	});
} */

// Function that will draw snowflakes on canvas
const drawFlakes = () => {
	flakePos(maxFlakes);
	ctx.clearRect(0, 0, width, height);

	ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
	ctx.beginPath();

	for (let j = 0; j < maxFlakes; j++) {
		let flake = flakes[j];
		ctx.moveTo(flake.x, flake.y);
		ctx.arc(flake.x, flake.y, flake.r, 0, Math.PI * 2, true);
	}
	ctx.fill();
	update();
};

let angle = 0;

// Moving the snowflakes
const update = () => {
	angle += 0.01;

	for (let h = 0; h < maxFlakes; h++) {
		let flake = flakes[h];
		flake.y += Math.cos(angle + flake.d) + 1 + flake.r / 2;
		flake.x += Math.sin(angle) * 2;

		if (flake.x > width + 5 || flake.x < -5 || flake.y > height) {
			if (h % 3 > 0) {
				flakes[h] = {
					x: Math.random() * width,
					y: -10,
					r: flake.r,
					d: flake.d,
				};
			} else {
				if (Math.sin(angle) > 0) {
					flakes[h] = {
						x: -5,
						y: Math.random() * height,
						r: flake.r,
						d: flake.d,
					};
				} else {
					flakes[h] = {
						x: width + 5,
						y: Math.random() * height,
						r: flake.r,
						d: flake.d,
					};
				}
			}
		}
	}
};

setInterval(drawFlakes, 40);
