import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    # @app jest chyba jakąś Flask'ow adnotacją (route decorator) oznaczającą aplikację
    # Funkcja zwraca plik index.html, któtrego Flask domyślnie szuka 
    # w folderze templates.
    return render_template("index.html")


@app.route("/about")
    # /about oznacza rozszerzenie gównego adresu strony (Home Page)
    # pod tym rozszerzonym adresem będzie wyświetlana poniższa
    # funkcja.
    # 
    # Dalej do zmiennej data przypisujemy zawartość pobraną z pliku 
    # company.json. "r" oznacza że otwieramy ten plik jako: tylko do 
    # odczytu.
    # render_template dodajemy nowy parametr company i przypisujemy 
    # do niego zawartość data aby wyświetlić je na stronie.
    # 
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company = data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
    # Dodaliśmy tutaj drugi parametr którym jest zmienna.
    # Wartość tej zmiennej będzie wyświetlana jako header
    # na stronie o powyższym adresie.
    # W każdej stronie jako zawartość h2 podajemy nazwę tej zmiennej
    # w podwójnym nawiasie klamrowym.
    # 
    # Wewnątrz funkcji definiujemy metodę POST, która będzie wysyłać dane wpisane
    # w formularzu w dziale contact do serwera.
    # Ważne jest aby zapamiętać o zaimportowaniu klasy request.
def contact():
    if request.method == "POST":
        # print(request.form) to wyświetli wszystkie wpisane przez nas dane z formularza.
        # print(request.form.get("name"))
        # print(request.form.get("email"))
        flash("Thanks {}, we have received your message!".format(request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )