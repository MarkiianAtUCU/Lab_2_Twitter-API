from flask import Flask, render_template, request, redirect, url_for
import htmlEditor
import MapGenerator
app = Flask(__name__)
name = ''


@app.route("/")
def main_render():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def main_post():
    global name
    name = request.form['inputName']
    # MapGenerator.generate_map('templates\\Map.html', name)
    # htmlEditor.edit_map('templates\\Map.html', htmlEditor.header)
    # return render_template('Map.html', User="@"+name)
    return redirect(url_for("submit_render"))


@app.route("/submit")
def submit_render():
    global name
    return render_template('submit.html', maximum=str(100), Num=str(100), User="@"+name)


@app.route('/submit', methods=['POST'])
def submit_post():
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
