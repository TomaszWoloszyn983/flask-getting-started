import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # ##app jest chyba jakąś Flask'ow adnotacją (route decorator) oznaczającą aplikację
    # Funkcja zwraca plik index.html, któtrego Flask domyślnie szuka 
    # w folderze templates.
    return render_template("index.html")


@app.route("/about")
    # /about oznacza rozszerzenie gównego adresu strony (Home Page)
    # pod tym rozszerzonym adresem będzie wyświetlana poniższa
    # funkcja.
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )