from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    mi_variable_1 = 100 * 100
    return render_template("index.html",
                           lista_proyectos=["Proyecto 1" ,  "Proyecto 2"],
                           resultado=mi_variable_1)


if __name__ == "__main__":
    app.run(debug=True)
