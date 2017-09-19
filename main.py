from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

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
      <form method=['POST']>
        <label for="rot">Rotate by
            <input type="text" name="rot" value="0"/>
        </label>
            <input type=textarea name="text"/>
        <input type="submit" />
    </body>
</html>
"""

@app.route("/")
def index():
    return page_header + form + page_footer

app.run()