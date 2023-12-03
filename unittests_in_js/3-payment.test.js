const Utils = require("./utils");
const sendPaymentRequestToApi = require('./3-payment');
const expect = require('chai').expect;
const sinon = require('sinon');


describe('spy_calculateNumber', function() {
	it("tests SUM option for reel and float integers", function() {
		const spy_calculateNumber = sinon.spy(Utils, 'calculateNumber');
		sendPaymentRequestToApi(100, 20);
		expect(spy_calculateNumber.calledOnce).to.be.true;
		expect(spy_calculateNumber.calledWith('SUM', 100, 20)).to.be.true;
		})
});
