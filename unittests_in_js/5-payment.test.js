const sendPaymentRequestToApi = require('./4-payment');
const expect = require('chai').expect;
const sinon = require('sinon');


describe('spy_calculateNumber', function() {
	beforeEach(function() {
		console.log('start testing ===============');
	})
	afterEach(function() {
		console.log('end testing ===============');
	})

	it("tests sendPaymentRequestToApi function", function() {
		const consoleLogSpy = sinon.spy(console, 'log');

		sendPaymentRequestToApi(100, 20);
		expect(consoleLogSpy.calledOnceWithExactly('The total is: 120'));
		expect(consoleLogSpy.calledOnce).to.be.true;		
		consoleLogSpy.restore();
	})

	it("tests sendPaymentRequestToApi function", function() {
		const consoleLogSpy = sinon.spy(console, 'log');

		sendPaymentRequestToApi(10, 10);
		expect(consoleLogSpy.calledOnceWithExactly('The total is: 20'));
		expect(consoleLogSpy.calledOnce).to.be.true;
	})

});
