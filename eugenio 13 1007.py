# ('/other') -  -от корня (root)
# ('./other') -от текущей директории


#  это стартовая версия приложения FLASK каркасный вариант по правилам pycharm

from flask import Flask, url_for

app = Flask(__name__)  # create application -приложение


@app.route('/')      # это два декоратора они пишутся вместе
@app.route('/index')
def index():
    return 'Admiral<br><a href="/slogan">Слоган</a'
@app.route('/poster')
def poster():
  <!DOCTYPE html>
  <html lang="en">
  <head>
<meta charset="UTF-8">
<title>poster</title>
</head>
<body>
<h1> Постер к фильму</h1>
<img src="{url_for('static', filename='images/admiral.png)}"
</body>
</html>

#     rel = "stylesheet"
#     href = "https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
#     integrity = "sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N"
#     crossorigin = "anonymous" >
#
#     < script
#     src = "https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"
#     integrity = "sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
#     crossorigin = "anonymous" > < / script >
#     < script
#     src = "https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"
#     integrity = "sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct"
#     crossorigin = "anonymous" > < / script >
#
#
#
# @app.route('/slogan')
# def slogan():
#
#     return 'ибо крепка как смерть любовь<br><a href="/">Назад/a'
#
# @app.route('/coundown')
# def countdown():
#     lst = [str(x) for x in range(10,0, -1)]
#     lst.append('Start!!!')
#     return '<br>'.join(lst)
#
#
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000)  # указываем хост (виртуальный сервер и порт)
#
# #  это стартовая версия приложения FLASK
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


