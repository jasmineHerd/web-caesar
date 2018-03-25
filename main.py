from flask import Flask,request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form =""" 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding:20px;
                margin: 0 auto;
                width 540px;
                font: 16px sans-serif;
            }
            textarea {
                margin: 10px 0;
                width:540px;
                height:120px;
            }
        </style>
    </head>
    <body>
    <!-- create your form here -->

        <form method ="post">
        <label for="rot">Rotated by:</label>
        <input id = "rot" type ="text" name ="rot" value="0"/><br>
        <textarea name ="text"></textarea><br>
        <input type = "submit"/>

</form>






    </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/",methods=["POST"])
def encrypt():
    text = request.form["text"]
    rot = request.form["rot"]
    rotInt = int(rot)
    return rotate_string(text,rotInt)

app.run()