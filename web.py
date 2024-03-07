from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='main.css') }}">
    <script src="{{url_for('static', filename='index.js')}}"></script>
</head>
<body>
    <div id="container">
        <input type="file" id="csvFileInput" accept=".csv">
        <button id="submitButton">Submit</button>
        <div id="dataDisplay"></div>
    </div>

</body>
</html>
"""

if __name__ == "__main__":
    
    app.run(port=7777, debug=True)