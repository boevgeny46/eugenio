# ('/other') -  -от корня (root)
# ('./other') -от текущей директории


#  это стартовая версия приложения FLASK каркасный вариант по правилам pycharm

from flask import Flask

app = Flask(__name__)  # create application -приложение


@app.route('/')      # это два декоратора они пишутся вместе
@app.route('/index')
def index():
    return 'Admiral<br><a href="/slogan">Слоган</a'

@app.route('/slogan')
def slogan():

    return 'ибо крепка как смерть любовь<br><a href="/">Назад/a'

@app.route('/coundown')
def countdown():
    lst = [str(x) for x in range(10,0, -1)]
    lst.append('Start!!!')
    return '<br>'.join(lst)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)  # указываем хост (виртуальный сервер и порт)

#  это стартовая версия приложения FLASK
