const calculateNumber = require("./1-calcul.js");
const assert = require('assert');

describe('calculateNumber', function() {
	it("tests SUM option for reel and float integers", function() {
		assert.equal(calculateNumber('SUM', 1, 3), 4);
		assert.equal(calculateNumber('SUM', 1, 3.7), 5);
		assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
		assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
		assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
	})
	it("tests SUBTRACT option for reel and float integers", function() {
		assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
		assert.equal(calculateNumber('SUBTRACT', 0, 0), 0);
		assert.equal(calculateNumber('SUBTRACT', 10, -5), 15);
		assert.equal(calculateNumber('SUBTRACT', -3.2, -5.5), 2);
	})
	it("tests DIVIDE option for reel and float integers", function() {
		assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
		assert.equal(calculateNumber('DIVIDE', 1.8, 3.2), 0.7);
		assert.equal(calculateNumber('DIVIDE', 1, 3.7), 0.3);
		assert.equal(calculateNumber('DIVIDE', 1.2, 3.7), 0.3);
		assert.equal(calculateNumber('DIVIDE', 5, 0), 'Error');
	})

});
