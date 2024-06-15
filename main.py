from flask import Flask, render_template, request
import requests

#импортируем объект класса Flask
app = Flask(__name__)

#формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])

def index():
   weather = None
   news = None
   if request.method == 'POST':
       city = request.form['city']
       weather = get_weather(city)
       news = get_news()
   return render_template("index.html", weather = weather, news = news)

def get_weather(city):
   api_key = "c601cc4705ef6d9ae81861f88e68e6d1"
   #адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()


def get_news():
    api_key = "a1583b2a193b427083584f44026e2928"
    url = f" https://newsapi.org/v2/everything?q=Apple&from=2024-06-15&sortBy=popularity&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles',[])



if __name__ == '__main__':
    app.run(debug=True)
