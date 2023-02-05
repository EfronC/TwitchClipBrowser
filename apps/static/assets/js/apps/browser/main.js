

function test() {
	var url = 'http://localhost:3333/api/login/twitch/';
	var data = {name:"Foo"};
	console.log(data);

	fetch(url, {
	    method: 'POST', // or 'PUT'
	    body: JSON.stringify(data), // data can be `string` or {object}!
	    headers:{
	    	'Content-Type': 'application/json'
	    }
	}).then(res => res.json())
	.catch(error => console.error('Error:', error))
	.then(response => {
		if (response.stat) {
			console.log(true);
		} else {
			console.log(false);
		}
	});
}