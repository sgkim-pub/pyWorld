const express = require('express');
const app = express();
const port = 8000;

app.use('/static', express.static(__dirname + '/static'));

app.listen(port, () => {
    console.log('Connected to 8000 port.');
});

app.get('/', (req, res) => {
    let options = {
        root: __dirname
    };
    res.sendFile('templates/index.html', options);
});

app.get('/api/message/get', (req, res) => {
    res.send('Hello, world!');
});
