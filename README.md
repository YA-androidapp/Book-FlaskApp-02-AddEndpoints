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

[app.py](app.py) を作成し、以下のコードを書きます。

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
