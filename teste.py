import unittest
import io

from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # Teste 1-verificar se a pagina abre
    def test_pagina_abre(self):
        resposta = self.app.get("/")
        self.assertEqual(resposta.status_code, 200)

    # Teste 2-verificar se existe formulario
    def test_formulario(self):
        resposta = self.app.get("/")
        self.assertIn(b"<form", resposta.data)

    # Teste 3-verificar se existe botao
    def test_botao(self):
        resposta = self.app.get("/")
        self.assertIn(b"button", resposta.data)

    # Teste 4-verificar envio de arquivo txt
    def test_arquivo_txt(self):
        arquivo = {
            "arquivo": (io.BytesIO(b"teste"), "teste.txt")
        }

        resposta = self.app.post(
            "/",
            data=arquivo,
            content_type="multipart/form-data"
        )

        self.assertIn(b"Arquivo enviado com sucesso!", resposta.data)

    # Teste 5-verificar bloqueio de arquivo exe
    def test_arquivo_exe(self):
        arquivo = {
            "arquivo": (io.BytesIO(b"teste"), "teste.exe")
        }

        resposta = self.app.post(
            "/",
            data=arquivo,
            content_type="multipart/form-data"
        )

        self.assertIn(b"Arquivos execut", resposta.data)


if __name__ == "__main__":
    unittest.main()