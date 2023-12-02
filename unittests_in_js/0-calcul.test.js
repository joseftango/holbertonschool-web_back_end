const calculateNumber = require("./0-calcul.js");
const assert = require('assert');

describe('calculateNumber', function() {
it("tests adding float integers", function() {
	assert.equal(calculateNumber(1, 3), 4, "one plus 3 = 4");
	assert.equal(calculateNumber(1, 3.7), 5,"one plus 3.7 = 5");
	assert.equal(calculateNumber(1.2, 3.7), 5,"float one plus 3.7 = 5");
	assert.equal(calculateNumber(1.5, 3.7), 6,"float  plus 3.7 = 6");
})
it("tests adding negative integers", function() {
	assert.equal(calculateNumber(1, -3), -2, "one plus -3 = -2");
	assert.equal(calculateNumber(0, 0), 0,"0 plus 0 = 0");
	assert.equal(calculateNumber(10, -5), 5,"10 one plus -5 = 5");
	assert.equal(calculateNumber(-3, -5), -8,"float  plus 3.7 = 6");
})
it("tests adding negative floats", function() {
	assert.equal(calculateNumber(1.8, -3), -1, "1.8 plus -3 = -1");
	assert.equal(calculateNumber(1, -3.7), -3,"one plus -3.7 = -3");
	assert.equal(calculateNumber(-1.2, 3.7), 3,"-1.2 one plus 3.7 = 3");
	assert.equal(calculateNumber(-1.5, 3.7), 3,"-1.5 plus 3.7 = 3");
})

});

