from flask import Flask, request, redirect

app = Flask(__name__)  # create application -приложение


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        return f"""
        <form class="login_form" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="photo">Приложите фото:</label>
                <input type="file" class="from-control-file" id="photo" name="file">
            </div<>br>
            <button type="submit" class="btn btn-primary">ООтправить</button>
        </form>
        """

    elif requestr.method == 'POST':
        f = request.filles['file']
        f.save('./static/images/loaded.png')
        return '<h1>Файл у вас на сервере</h1'

#         def index():
#     return 'Admiral<br><a href="/slogan">Слоган</a'
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
