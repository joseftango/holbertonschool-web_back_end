const http = require('http');

const port = 1245;
const app = http.createServer((req, res) => {
  if (req.url === '/' || req.url === '/any_endpoint') {
    res.setHeader('Content-Type', 'text/plain');
    res.write('Hello Holberton School!');
    res.end();
  }
});

app.listen(port, () => {
  console.log('...');
});

module.exports = app;
