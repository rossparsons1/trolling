const express = require('express')
const app = express()
const cors = require('cors')

app.use(cors({
    origin: 'https://rossparsons1.github.io'
}))
app.use(express.json());


app.post('/', async (req,res) => {
    const text = req.body.data;
    console.log(text)
    try {
        const response = await axios.post('https://accessories-speak-max-cop.trycloudflare.com/predict/', {
            text: text,
        });
        res.json(response.data);
    } catch (error) {
        res.status(500).send('Error calling FastAPI');
    }
})

app.listen(8080, () => {
    console.log('Сервер запущен')
})
