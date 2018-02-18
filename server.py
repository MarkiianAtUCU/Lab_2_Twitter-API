from flask import Flask, render_template, request, redirect, url_for,\
    send_file, Response
import htmlEditor
import MapGenerator
import twitterAPI
import folium
app = Flask(__name__)
name = ''
x = False
f_map = folium.Map()


@app.route("/")
def main_render():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def main_post():
    global name
    name = request.form['inputName']
    return redirect(url_for("submit_render"))


@app.route("/submit")
def submit_render():
    global name
    global user_coords
    global js
    global f_map
    global x
    if not x:
        # find user
        friend_num, user_coords, js = MapGenerator.create_user_marker(name)
        MapGenerator.add_marker(f_map, user_coords, js, status="POINT")
        x = True
    return render_template('submit.html', maximum=str(friend_num),
                           Num=str(friend_num), User="@"+name)


@app.route('/submit', methods=['POST'])
def submit():
    global name
    global user_coords
    global js
    global number
    number = request.form['inputName']
    return redirect(url_for("loading"))


@app.route('/loading')
def loading():
    global f_map
    global user_coords
    x = 0
    friends = twitterAPI.json_get_user_friend_info(name, int(number))
    for i in friends:
        x += 1
        # find all friends
        print(x, "of", number)
        friend_coord, js, status = MapGenerator.create_friend_marker(i)

        MapGenerator.add_marker(f_map, friend_coord, js, status=status)
        MapGenerator.add_line(f_map, [user_coords, friend_coord])

    f_map.save('templates\\Map.html')
    htmlEditor.edit_map('templates\\Map.html', htmlEditor.header)
    return render_template("Map.html", User="@"+name)


if __name__ == "__main__":
    app.run()
