# ('/other') -  -от корня (root)
# ('./other') -от текущей директории
from flask import Flask
app = Flask(__name__)  # create application -приложение

@app.route('/')
@app.route('/index')
def index():
    return "Hello"

if  __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)  # указываем хост  и порт

#  это стартовая версия приложения FLASK


