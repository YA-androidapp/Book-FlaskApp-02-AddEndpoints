# Book-FlaskApp-02-AddEndpoints

---

## Flask のインストール

仮想環境を用意して、Flask パッケージを(ローカル)インストールします。

```ps
PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> py -m venv flaskenv
PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> flaskenv\Scripts\activate
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> py -m pip install Flask
```

## Flask で 複数のエンドポイントを持つ API を作る

[app.py](app.py) を作成し、以下のコードを書きます。 [app01.py](app01.py)

```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/hello')
def hello():
    return 'Hello'
```

環境変数 `FLASK_APP` にファイル名を設定します。

```cmd
REM コマンドプロンプトの場合
C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> set FLASK_APP=app.py
```

```ps
# PowerShellの場合
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> $env:FLASK_APP = "app.py"
```

実行します。

```ps
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> python -m flask run
```

> - Serving Flask app "app.py"
>
> - Environment: production
>
>   WARNING: This is a development server. Do not use it in a production deployment.
>
>   Use a production WSGI server instead.
>
> - Debug mode: off
>
> - Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

デバッグモードを有効化する場合は、以下のコマンドを実行します。

```ps
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> $env:FLASK_ENV = "development"
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> python -m flask run
```

ブラウザを開き、

- [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- [http://127.0.0.1:5000/hello](http://127.0.0.1:5000/hello)

にアクセスして、それぞれ `Index` `Hello` と表示されることを確認します。

## エンドポイントで受け取る型を指定する

次に、 app.py の内容を、以下に書き換えます。 [app02.py](app02.py)

```py
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/user/name/<username>')
def show_name(username):
    return 'Name %s' % escape(username)

@app.route('/user/age/<int:age>')
def show_age_int(age):
    return 'Age %d' % age

@app.route('/user/age/<float:age>')
def show_age_float(age):
    return 'Age %f' % age

@app.route('/user/height/<float:height>')
def show_height(height):
    return 'Height %f' % height

@app.route('/user/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)

@app.route('/user/id/<uuid:id>')
def show_id(id):
    return 'ID %s' % id
```

環境変数 `FLASK_APP` にファイル名を設定して、実行します。

```ps
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> $env:FLASK_APP = "app.py"
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> python -m flask run
```

ブラウザを開き、以下のエンドポイントにアクセスします。

| URL                                                                                                                         | 表示される内容                                 |
| --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| [/user/name/taro](http://127.0.0.1:5000/user/name/taro)                                                                     | `Name taro`                                    |
| [/user/name/1](http://127.0.0.1:5000/user/name/1)                                                                           | `Name 1`                                       |
| [/user/name/1.1](http://127.0.0.1:5000/user/name/1.1)                                                                       | `Name 1.1`                                     |
| [/user/name/123/456](http://127.0.0.1:5000/user/name/123/456)                                                               | **Not Found**                                  |
| [/user/name/12345678-1234-1234-1234-123456789012](http://127.0.0.1:5000/user/name/12345678-1234-1234-1234-123456789012)     | `12345678-1234-1234-1234-123456789012`         |
|                                                                                                                             |                                                |
| [/user/age/taro](http://127.0.0.1:5000/user/age/taro)                                                                       | **Not Found**                                  |
| [/user/age/1](http://127.0.0.1:5000/user/age/1)                                                                             | `Age 1`                                        |
| [/user/age/1.1](http://127.0.0.1:5000/user/age/1.1)                                                                         | `Age 1.100000`                                 |
| [/user/age/123/456](http://127.0.0.1:5000/user/age/123/456)                                                                 | **Not Found**                                  |
| [/user/age/12345678-1234-1234-1234-123456789012](http://127.0.0.1:5000/user/age/12345678-1234-1234-1234-123456789012)       | **Not Found**                                  |
|                                                                                                                             |                                                |
| [/user/height/taro](http://127.0.0.1:5000/user/height/taro)                                                                 | **Not Found**                                  |
| [/user/height/1](http://127.0.0.1:5000/user/height/1)                                                                       | **Not Found**                                  |
| [/user/height/1.1](http://127.0.0.1:5000/user/height/1.1)                                                                   | `Age 1.100000`                                 |
| [/user/height/123/456](http://127.0.0.1:5000/user/height/123/456)                                                           | **Not Found**                                  |
| [/user/height/12345678-1234-1234-1234-123456789012](http://127.0.0.1:5000/user/height/12345678-1234-1234-1234-123456789012) | **Not Found**                                  |
|                                                                                                                             |                                                |
| [/user/path/taro](http://127.0.0.1:5000/user/path/taro)                                                                     | `Subpath taro`                                 |
| [/user/path/1](http://127.0.0.1:5000/user/path/1)                                                                           | `Subpath 1`                                    |
| [/user/path/1.1](http://127.0.0.1:5000/user/path/1.1)                                                                       | `Subpath 1.1`                                  |
| [/user/path/123/456](http://127.0.0.1:5000/user/path/123/456)                                                               | `Subpath 123/456`                              |
| [/user/path/12345678-1234-1234-1234-123456789012](http://127.0.0.1:5000/user/path/12345678-1234-1234-1234-123456789012)     | `Subpath 12345678-1234-1234-1234-123456789012` |
|                                                                                                                             |                                                |
| [/user/id/taro](http://127.0.0.1:5000/user/id/taro)                                                                         | **Not Found**                                  |
| [/user/id/1](http://127.0.0.1:5000/user/id/1)                                                                               | **Not Found**                                  |
| [/user/id/1.1](http://127.0.0.1:5000/user/id/1.1)                                                                           | **Not Found**                                  |
| [/user/id/123/456](http://127.0.0.1:5000/user/id/123/456)                                                                   | **Not Found**                                  |
| [/user/id/12345678-1234-1234-1234-123456789012](http://127.0.0.1:5000/user/id/12345678-1234-1234-1234-123456789012)         | `ID 12345678-1234-1234-1234-123456789012`      |

| converter 名 | 受け入れる値                           |
| ------------ | -------------------------------------- |
| string       | （デフォルト）スラッシュなしのテキスト |
| int          | 正の整数                               |
| float        | 正の浮動小数点値                       |
| path         | string + スラッシュ                    |
| uuid         | UUID 文字列                            |

## エンドポイントの末尾にスラッシュを指定した場合のリダイレクト

次に、 app.py の内容を、以下に書き換えます。 [app03.py](app03.py)

```py
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

環境変数 `FLASK_APP` にファイル名を設定して、実行します。

```ps
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> $env:FLASK_APP = "app.py"
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> python -m flask run
```

ブラウザを開き、以下のエンドポイントにアクセスします。

| URL                                           | app.py の末尾の `/` | アクセス時の末尾の `/` | 表示される内容                                                                        |
| --------------------------------------------- | ------------------- | ---------------------- | ------------------------------------------------------------------------------------- |
| [/projects/](http://127.0.0.1:5000/projects/) | 有                  | 有                     | `The project page`                                                                    |
| [/projects](http://127.0.0.1:5000/projects)   | 有                  | 無                     | `The project page` [/projects/](http://127.0.0.1:5000/projects/) にリダイレクトされる |
| [/about/](http://127.0.0.1:5000/about/)       | 無                  | 有                     | **Not Found**                                                                         |
| [/about](http://127.0.0.1:5000/about)         | 無                  | 無                     | `The about page`                                                                      |

## 関数名を指定してリダイレクト

次に、 app.py の内容を、以下に書き換えます。 [app04.py](app04.py)

```py
from flask import abort, Flask, redirect, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('about', next='/path/to'))

@app.route('/projects/')
def projects():
    return redirect(url_for('about'))

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    abort(401)
```

環境変数 `FLASK_APP` にファイル名を設定して、実行します。

```ps
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> $env:FLASK_APP = "app.py"
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> python -m flask run
```

ブラウザを開き、以下のエンドポイントにアクセスします。

| URL                                           | 表示される内容                                                                                                  |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [/projects/](http://127.0.0.1:5000/projects/) | `The about page` [/about?next=%2Fpath%2Fto](http://127.0.0.1:5000/about?next=%2Fpath%2Fto) にリダイレクトされる |
| [/projects/](http://127.0.0.1:5000/projects/) | `The about page` [/about](http://127.0.0.1:5000/about) にリダイレクトされる                                     |
| [/about](http://127.0.0.1:5000/login)         | **Unauthorized**                                                                                                |

## HTTP メソッド

次に、 app.py の内容を、以下に書き換えます。 [app05.py](app05.py)

※method 以外のプロパティについては、 [Request](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request) を参照

```py
from flask import Flask, request, Markup

app = Flask(__name__)


@app.route('/')
def index():
    html = '''
    <form action="/show">
        <input type="text" name="name" value="taro" />
        <button type="submit" formmethod="GET">GET</button>
        <button type="submit" formmethod="POST">POST</button>
    </form>
    '''
    return Markup(html)


@app.route('/show', methods=['GET', 'POST'])
def show():
    try:
        if request.method == 'POST':
            return request.form['name']
        elif request.method == 'GET':
            return request.args.get('name', '')
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
```

環境変数 `FLASK_APP` にファイル名を設定して、実行します。

```ps
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> $env:FLASK_APP = "app.py"
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-02-AddEndpoints> python -m flask run
```

ブラウザを開き、 [http://127.0.0.1:5000/](http://127.0.0.1:5000/) にアクセスして、フォームから文字列を送信し、クエリ文字列や API 側で受け取った `name` パラメータの値が正しいことを確認します。
