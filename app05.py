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