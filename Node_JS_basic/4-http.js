const http = require('http');

const port = 1245;

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.write('Hello Holberton School!');
  res.end();
});

app.listen(port, () => {
  console.log('...');
});

module.exports = app;
