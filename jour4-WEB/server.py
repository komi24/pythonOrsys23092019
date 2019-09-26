from flask import Flask, render_template

app = Flask(__name__,
            static_folder="public",
            static_url_path="/public")


liste_personnes = [
    {"nom": "Dupont", "prenom": "Mylenne", "age": 42},
    {"nom": "Durand", "prenom": "Mathias", "age": 24},
    {"nom": "Dumont", "prenom": "Melanie", "age": 36},
    {"nom": "Dulard", "prenom": "Maud", "age": 38},
    {"nom": "Dulay", "prenom": "Romain", "age": 31}
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        liste_eleves=liste_personnes)


app.run(port=8080, debug=True)
