const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;
const hostname = '127.0.0.1';
const filePath = process.argv[2];
const promise = countStudents(filePath);

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  promise.then((data) => {
    res.send(`This is the list of our students\n${data}`);
  }).catch(() => { res.send('This is the list of students is not available'); });
});

module.exports = app.listen(port, hostname);
