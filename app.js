//how to write a post request with JSON body
const url = 'https://example.com/data';
const payload = {
    name: 'John Doe',
    email: 'john@example.com'

};
fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'   // Tells the server you expect JSON back
    },
    body: JSON.stringify(payload)  // Converts JS object to JSON string
})
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();  // Parse the JSON from the response
    })
    .then(data => {
        console.log('Success:', data);  // Handle the JSON data returned from the server
    })
    .catch(error => {
        console.error('Error:', error);  // Handle any errors that occurred during the fetch
    });