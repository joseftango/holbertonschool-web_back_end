export default function handleResponseFromAPI(promise) {
	return promise.then((resolveVal) => ({status: 200 ,body: success}))
	.catch((rejectVal) => Error())
	.finally(console.log('Got a response from the API'))
}
