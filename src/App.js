import './App.css';
import axios from "axios";

function App() {
    const handleLogin = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8080/',
            {
                data: document.querySelector('.data').value,
            })
            .then(res => {
                const response = res.data
                console.log(response)
                alert(`Вероятность токсичности ${res.data.prediction}`)
            })
            .catch(err => {
                console.log(err)
            })
    }
  return (
    <div className="App">
        <form onSubmit={(e) => handleLogin(e)}>
            <div className="input_box">
                <div className="text_input">Ваш коментарий</div>
                <input className="data" type="text"/>
            </div>
            <button type="submit">Отправить</button>
        </form>
    </div>
  );
}

export default App;
