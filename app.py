from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "msedit_panier_2026"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")
@app.route("/parcours")
def parcours():
    return render_template("parcours.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/panier")
def panier():
    return render_template("panier.html")

@app.route("/ajouter/<produit>")
def ajouter(produit):

    if "panier" not in session:
        session["panier"] = []

    panier = session["panier"]
    panier.append(produit)

    session["panier"] = panier

    return redirect("/panier")

if __name__ == "__main__":
    app.run(debug=True)

