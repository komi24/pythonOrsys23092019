from flask import Flask, render_template, request, redirect

app = Flask(__name__,
            static_folder="public",
            static_url_path="/public")


liste_personnes = [
    {"nom": "Dupont", "prenom": "Mylenne", "age": 42, "pic": "pers1.jpg"},
    {"nom": "Durand", "prenom": "Mathias", "age": 24, "pic": "pers2.jpg"},
    {"nom": "Dumont", "prenom": "Melanie", "age": 36, "pic": "pers1.jpg"},
    {"nom": "Dulard", "prenom": "Maud", "age": 38, "pic": "pers2.jpg"},
    {"nom": "Dulay", "prenom": "Romain", "age": 31, "pic": "pers1.jpg"}
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        liste_eleves=liste_personnes)


@app.route("/ajoute_eleve")
def add_student():
    return render_template(
        "form.html")


@app.route("/api/personne", methods=["POST"])
def add_student_post():
    liste_personnes.append({
        "nom": request.form.get("nom"),
        "prenom": request.form.get("prenom"),
        "age": 32,
        "pic": "pers1.jpg"
    })
    return redirect("/")


app.run(port=8080, debug=True)
