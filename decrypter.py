import os
import pyaes

def decrypt_file(encrypted_file: str, decryption_key: bytes, output_file: str) -> None:
    """
    Descriptografa um arquivo criptografado usando AES (CTR Mode).

    :param encrypted_file: Caminho do arquivo criptografado.
    :param decryption_key: Chave de descriptografia (16 bytes recomendados).
    :param output_file: Caminho do arquivo descriptografado a ser criado.
    """
    try:
        # Abrir o arquivo criptografado
        with open(encrypted_file, "rb") as file:
            encrypted_data = file.read()

        # Descriptografar os dados
        aes = pyaes.AESModeOfOperationCTR(decryption_key)
        decrypted_data = aes.decrypt(encrypted_data)

        # Remover o arquivo criptografado
        os.remove(encrypted_file)

        # Criar o arquivo descriptografado
        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print(f"Arquivo '{output_file}' criado com sucesso.")
    
    except FileNotFoundError:
        print(f"Erro: Arquivo '{encrypted_file}' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Parâmetros
file_name = "teste.txt.ransomwaretroll"
key = b"testeransomwares"
output_file = "teste.txt"

# Descriptografar o arquivo
decrypt_file(file_name, key, output_file)
