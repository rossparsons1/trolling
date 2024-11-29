const express = require('express')
const app = express()
const cors = require('cors')

app.use(cors({
    origin: 'https://rossparsons1.github.io'
}))
app.use(express.json());


app.post('/', async (req,res) => {
    console.log(req.body)
    res.send("12345")
})

app.listen(8080, () => {
    console.log('Сервер запущен')
})
