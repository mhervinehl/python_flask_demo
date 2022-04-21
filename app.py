# tutorial from https://davemccollough.com/2020/12/05/deploy-your-first-python-flask-application-to-azure-app-service/

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
        