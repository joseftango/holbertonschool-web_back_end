const http = require('http');
const process = require('process');
const countStudents = require('./3-read_file_async');

const port = 1245;
const filePath = process.argv[2];

const promise = countStudents(filePath);

const app = http.createServer((req, res) => {
  if (req.url === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    promise.then((data) => {
      res.end(`This is the list of our students\n${data}`);
    }).catch(() => { res.end('the list of our students is not available'); });
  } else if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  }
});

app.listen(port, () => {
  console.log('...');
});

module.exports = app;
