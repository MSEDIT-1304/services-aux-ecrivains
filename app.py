from flask import Flask, render_template

app = Flask(__name__)

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
    
if __name__ == "__main__":
    app.run(debug=True)

