from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Criação da página</h1>
    <h2>Pequena Lista<h2>
     <p>Projeto desenvolvido para praticar conceitos de DevOps.</p>

    <ul>
        <li>Estudar Python</li>
        <li>Estudar Git</li>
        <li>Aprender Docker</li>
    </ul>
    <p>Total de tarefas: 3</p>
    <p>Ultimo commit da semana 2<p>
    """


if __name__ == "__main__":
    app.run(debug=True)