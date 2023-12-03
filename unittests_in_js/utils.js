const Utils = {
	calculateNumber: (type, a, b) => {
		const x = Math.round(a);
		const y = Math.round(b);
		let res;
		switch (type) {
			case "SUM":
				res = x + y;
				break;
			case "SUBTRACT":
				res = x - y;
				break;
			case "DIVIDE":
				if (y === 0) {
					res = 'Error';
				}
				else {
				res = (x / y).toFixed(1);
				}
				break;
		}
		return res;
	}	
};

module.exports = Utils;
