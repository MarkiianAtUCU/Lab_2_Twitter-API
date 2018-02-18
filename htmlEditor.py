from bs4 import BeautifulSoup
header = """
    <div class="container-fluid" style="padding: 0">
        <div class="rows">
            <div class="col-md-11">
                <h3 class="text-muted">User: 
                    <span style="color:black;font-weight: bold">{{User}}</span>

                </h3>
            </div>

            <div class="col-md-1" style="padding: 0">
                <a href="http://markiian.pythonanywhere.com/" style="float: right;">
                    <button id="btnSignUp" class="btn btn-lg btn-primary btn-block" type="submit" style="height: 57px">Back!</button>
                </a>

            </div>
        </div>
    </div>"""


def edit_map(path, header):
    """
    (str, str) -> None

    Function adds header to Html file
    """
    with open(path, "r") as file:
        lul = file.read()

    soup = BeautifulSoup(lul)
    soup.body.insert(0, BeautifulSoup(header))
    with open("templates\\Map.html", 'w') as file:
        file.write(str(soup))
