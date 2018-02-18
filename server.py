from flask import Flask, render_template, request
import htmlEditor
import MapGenerator
app = Flask(__name__)
name=''

@app.route("/")
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def ShowMap():
    global name
    name = request.form['inputName']
    print(name)
    if name:
        # MapGenerator.generate_map('templates\\Map.html', name)
        # htmlEditor.edit_map('templates\\Map.html', htmlEditor.header)
        # return render_template('Map.html', User="@"+name)
        return render_template('submit.html', maximum=str(100))


@app.route('/', methods=['POST'])
def ShowMap2():
    global name
    number = request.form['inputName']
    print(number)
    if number:
        # MapGenerator.generate_map('templates\\Map.html', name)
        # htmlEditor.edit_map('templates\\Map.html', htmlEditor.header)
        # return render_template('Map.html', User="@"+name)
        return render_template('Map.html')


if __name__ == "__main__":
    app.run()
