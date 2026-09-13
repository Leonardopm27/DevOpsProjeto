from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Criação da página</h1>
    <h2>Pequena Lista<h2>

    <ul>
        <li>Estudar Python</li>
        <li>Estudar Git</li>
        <li>Aprender Docker</li>
    </ul>
    """


if __name__ == "__main__":
    app.run(debug=True)