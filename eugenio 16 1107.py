from flask import Flask
from flask import render_template
app = Flask(__name__)  # create application -приложение


@app.route('/')      # это два декоратора они пишутся вместе
@app.route('/index')
def index():
    param = {}
    param['username'] = 'Слушатель'
    param['title'] = 'Работа с шаблонами'

    return render_template('index.html', **param)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even', **param)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)  # указываем хост (виртуальный сервер и порт)
