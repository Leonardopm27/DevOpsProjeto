from flask import Flask, request
import os

app = Flask(__name__)

PASTA_UPLOAD = "uploads"

if not os.path.exists(PASTA_UPLOAD):
    os.makedirs(PASTA_UPLOAD)


@app.route("/", methods=["GET", "POST"])
def inicio():

    mensagem = ""

    if request.method == "POST":
        arquivo = request.files["arquivo"]

        if arquivo.filename != "":

            if arquivo.filename.lower().endswith(".exe"):
                mensagem = "Arquivos executáveis não são permitidos."

            else:
                caminho = os.path.join(PASTA_UPLOAD, arquivo.filename)
                arquivo.save(caminho)

                mensagem = "Arquivo enviado com sucesso!"

    return f"""
    <h1>Início de um servidor de arquivos teste, admito que utilizei auxilio externo para fazer esse backup</h1>

    <p>{mensagem}</p>

    <form method="POST" enctype="multipart/form-data">

        <input type="file" name="arquivo">

        <button type="submit">
            Enviar arquivo
        </button>

    </form>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)