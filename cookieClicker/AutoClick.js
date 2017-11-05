var autoClick = {
	freq: 20000,
	GoldenCookie: null,
	Raeindeer: null,
	state: function (flag) {
		if (flag) {
			autoClick.GoldenCookie = setInterval(function () {
					for (var h in Game.shimmers) {
						if (Game.shimmers[h].type == "golden") {
							Game.shimmers[h].pop();
						}
					}
				}, autoClick.freq);
			autoClick.Raeindeer = setInterval(function () {
					for (var h in Game.shimmers) {
						if (Game.shimmers[h].type == "reindeer") {
							Game.shimmers[h].pop();
						}
					}
				}, autoClick.freq);
		} else {
			clearInterval(autoClick.GoldenCookie);
			clearInterval(autoClick.Raeindeer);
		}
	}
};

autoClick.state(true);


