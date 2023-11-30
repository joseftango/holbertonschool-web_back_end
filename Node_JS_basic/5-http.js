const http = require('http');
const process = require('process');
const countStudents = require('./3-read_file_async');

const port = 1245;
const filePath = process.argv[2];
const promise = countStudents(filePath);

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/students') {
    promise.then((data) => {
      res.write(`This is the list of our students\n${data}`);
      res.end();
    }).catch(() => { res.end('the list of our students is not available'); });
  } else if (req.url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  }
});

app.listen(port, () => {
  console.log('...');
});

module.exports = app;
