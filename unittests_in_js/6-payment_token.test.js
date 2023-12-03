const getPaymentTokenFromAPI = require('./6-payment_token');
const expect = require('chai').expect;


describe('getPaymentTokenFromAPI', function() {
    it('async testing Promise', (done) => {
        getPaymentTokenFromAPI(true)
            .then((res) => {
                expect(res).to.eql({ data: 'Successful response from the API' })
				done();
            })
			.catch((error) => {
				done(error);
			  });		
    })
})
