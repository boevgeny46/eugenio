from flask import Flask
from flask import render_template
import json

app = Flask(__name__)  # create application -приложение


@app.route('/')  # это два декоратора они пишутся вместе
@app.route('/index')
def index():
    param = {}
    param['username'] = 'Слушатель'
    param['title'] = 'Работа с шаблонами'

    return render_template('index.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even', **param)


@app.route('/news')
def news():
    with open('news.json', 'rt', encoding='utf-8') as f:
        news_list = json.loads(f.read())
        return render_template('news.html', title='Новости', news=news_list)
        print(news_list)

    lst = ['ANN', 'TOM', 'BOB']
    return render_template('news.html', title="FOR", news=lst)

@app.route('/vartest')
def vartest():
    return render_template('var_test.html', title='Переменные в HTML')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)  # указываем хост (виртуальный сервер и порт)
