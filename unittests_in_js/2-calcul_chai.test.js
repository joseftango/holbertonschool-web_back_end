const calculateNumber = require("./2-calcul_chai");
const expect = require('chai').expect;


describe('calculateNumber', function() {
	it("tests SUM option for reel and float integers", function() {
		expect(4).to.equal(calculateNumber('SUM', 1, 3));
		expect(5).to.equal(calculateNumber('SUM', 1, 3.7));
		expect(5).to.equal(calculateNumber('SUM', 1.2, 3.7));
		expect(6).to.equal(calculateNumber('SUM', 1.5, 3.7));
		expect(6).to.equal(calculateNumber('SUM', 1.4, 4.5));
	})
	it("tests SUBTRACT option for reel and float integers", function() {
		expect(-4).to.equal(calculateNumber('SUBTRACT', 1.4, 4.5));
		expect(0).to.equal(calculateNumber('SUBTRACT', 0, 0));
		expect(15).to.equal(calculateNumber('SUBTRACT', 10, -5));
		expect(2).to.equal(calculateNumber('SUBTRACT', -3.2, -5.5));
	})
	it("tests DIVIDE option for reel and float integers", function() {
		expect('0.2').to.equal(calculateNumber('DIVIDE', 1.4, 4.5));
		expect('0.7').to.equal(calculateNumber('DIVIDE', 1.8, 3.2));
		expect('0.3').to.equal(calculateNumber('DIVIDE', 1, 3.7));
		expect('0.3').to.equal(calculateNumber('DIVIDE', 1.2, 3.7));
		expect('Error').to.equal(calculateNumber('DIVIDE', 5, 0));
	})
});
