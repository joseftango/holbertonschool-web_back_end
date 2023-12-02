const calculateNumber = require("./1-calcul.js");
const expect = require('chai').expect;

describe('calculateNumber', function() {
	it("tests SUM option for reel and float integers", function() {
		expect(calculateNumber('SUM', 1, 3)).to.equal(4);
		expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
		expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
		expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
		expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
	})
	it("tests SUBTRACT option for reel and float integers", function() {
		expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
		expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
		expect(calculateNumber('SUBTRACT', 10, -5)).to.equal(15);
		expect(calculateNumber('SUBTRACT', -3.2, -5.5)).to.equal(2);
	})
	it("tests DIVIDE option for reel and float integers", function() {
		expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal('0.2');
		expect(calculateNumber('DIVIDE', 1.8, 3.2)).to.equal('0.7');
		expect(calculateNumber('DIVIDE', 1, 3.7)).to.equal('0.3');
		expect(calculateNumber('DIVIDE', 1.2, 3.7)).to.equal('0.3');
		expect(calculateNumber('DIVIDE', 5, 0)).to.equal('Error');
	})
});
