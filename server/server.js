const express = require('express')
const app = express()
const cors = require('cors')

const corsOptions = {
    origin: 'https://rossparsons1.github.io', // Разрешите ваш фронтенд
    methods: ['GET', 'POST', 'OPTIONS'], // Разрешите необходимые методы
    allowedHeaders: ['Content-Type', 'Authorization'], // Разрешенные заголовки
};

app.use(cors(corsOptions));
app.use(express.json());


app.post('/', async (req,res) => {
    const text = req.body.data;
    console.log(text)
    try {
        const response = await axios.post('https://trollingbot.onrender.com/predict/', {
            text: text,
        });
        res.json(response.data);
    } catch (error) {
        res.status(500).send(error);
    }
})

app.listen(8080, () => {
    console.log('Сервер запущен')
})
