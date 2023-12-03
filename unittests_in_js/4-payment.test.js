const Utils = require("./utils");
const sendPaymentRequestToApi = require('./4-payment');
const expect = require('chai').expect;
const sinon = require('sinon');


describe('spy_calculateNumber', function() {
	it("tests SUM option for reel and float integers", function() {
		const stub_calculateNumber = sinon.stub(Utils, 'calculateNumber');
		const consoleLogSpy = sinon.spy(console, 'log');
		
		sendPaymentRequestToApi(100, 20);
		
		expect(stub_calculateNumber.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
		expect(consoleLogSpy.calledOnceWithExactly('The total is: 10'));

		stub_calculateNumber.withArgs('SUM', 100, 20).returns(10);

	})
});
