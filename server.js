const express = require('express');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();
const PORT = 3000;

// Use body-parser middleware to parse JSON data
app.use(bodyParser.json());

// Store the data
let storedData = {};

// POST route to accept JSON
app.post('/store', (req, res) => {
    storedData = req.body; // Store incoming JSON in the storedData
    res.send('Data stored successfully');
});

// GET route to send stored data
app.get('/data', (req, res) => {
    res.json(storedData);
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
