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
        <form method="post">
            <label for="Rotate by:">Rotate by:</label>
            <input type="text" name="rot" value="0">
            <textarea name="text"></textarea>
            <input type="submit" value="Submit Query">
        </form>
    </body>
</html>

"""
@app.route("/", methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    words = request.form['text']
    encrypted = rotate_string(words, rotate)
    content = "<h1>" + encrypted + "</h1>" 
    return content


@app.route("/")
def index():
    return form

app.run()