from flask import Flask, render_template, request
import htmlEditor
import MapGenerator
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def ShowMap():
    name = request.form['inputName']
    if name:
        MapGenerator.generate_map('templates\\Map.html')
        htmlEditor.edit_map('templates\\Map.html', htmlEditor.header)
        return render_template('Map.html', User="@"+name)


if __name__ == "__main__":
    app.run()
