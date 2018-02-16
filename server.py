from flask import Flask, render_template, request
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def signUp():
    name = request.form['inputName']
    if name:
        with open('templates\\Map.html',"r") as file:
            lul=file.read()
        soup=BeautifulSoup(lul)
        x=soup.body.insert(0,"<h1>LUL</h1>")
        with open("templates\\Map.html",'w') as file:
            file.write(x)
        print(x)
        return render_template('Map.html')


if __name__ == "__main__":
    app.run()
