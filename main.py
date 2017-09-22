from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form action='/new' method="post">
        <label for="rot">Rotate by:
            <input type="text" name="rot" value="0"/>
        </label>
        <br>
            <textarea name="text"></textarea>
        <br>
        <input type="submit" />
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form


@app.route("/new", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text']
    newtext = rotate_string(text, rot)
    return '<h1>' + newtext + '</h1>'


app.run()