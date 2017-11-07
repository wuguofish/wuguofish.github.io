var autoClick = {
	period: 20000,
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
				}, autoClick.period);
			autoClick.Raeindeer = setInterval(function () {
					for (var h in Game.shimmers) {
						if (Game.shimmers[h].type == "reindeer") {
							Game.shimmers[h].pop();
						}
					}
				}, autoClick.period);
		} else {
			clearInterval(autoClick.GoldenCookie);
			clearInterval(autoClick.Raeindeer);
		}
	},
	changePeriod : function(period){
		module.state(false);
		module.period = period * 1000;
		module.state(true);
	}
};

autoClick.state(true);


