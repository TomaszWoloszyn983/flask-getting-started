import os
import json
from flask import Flask, render_template

app = Flask(__name__)


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


@app.route("/contact")
    # Dodaliśmy tutaj drugi parametr którym jest zmienna.
    # Wartość tej zmiennej będzie wyświetlana jako header
    # na stronie o powyższym adresie.
    # W każdej stronie jako zawartość h2 podajemy nazwę tej zmiennej
    # w podwójnym nawiasie klamrowym.
def contact():
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