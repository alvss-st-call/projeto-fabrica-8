from flask import Flask, render_template

app = Flask(__name__)

pacientes = [
    {
        "id": 1,
        "nome": "Maria Oliveira",
        "idade": 45,
        "condicao": "Hipertensão",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg"
    },
    {
        "id": 2,
        "nome": "Carlos Souza",
        "idade": 60,
        "condicao": "Diabetes Tipo 2",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg"
    }
]

medicos = [
    {
        "id": 1,
        "nome": "Dra. Ana Costa",
        "especialidade": "Cardiologia",
        "experiencia": 12,
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg"
    },
    {
        "id": 2,
        "nome": "Dr. João Lima",
        "especialidade": "Endocrinologia",
        "experiencia": 8,
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pacientes")
def listar_pacientes():
    return render_template("listar_pacientes.html", pacientes=pacientes)

@app.route("/paciente/<int:paciente_id>")
def detalhe_paciente(paciente_id):
    for paciente in pacientes:
        if paciente["id"] == paciente_id:
            return render_template("detalhe_paciente.html", paciente=paciente)
    return render_template("404.html"), 404

@app.route("/medicos")
def listar_medicos():
    return render_template("listar_medicos.html", medicos=medicos)

@app.route("/medico/<int:medico_id>")
def detalhe_medico(medico_id):
    for medico in medicos:
        if medico["id"] == medico_id:
            return render_template("detalhe_medico.html", medico=medico)
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
