import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# --- 4.1: Demonstração de Encriptação Simétrica (AES-GCM) ---
print("--- 4.1: Encriptação Simétrica (AES-GCM) ---")
dados_simetricos = b"dados confidenciais AES para um grande volume de dados."

# 1. Gerar Chave e Nonce
[cite_start]key_aes = AESGCM.generate_key(bit_length=256) # Chave de 256 bits [cite: 162]
aes = AESGCM(key_aes)
[cite_start]nonce = os.urandom(12) # Vetor de inicialização (IV) [cite: 164]

# 2. Encriptação
[cite_start]ct_aes = aes.encrypt(nonce, dados_simetricos, b"metadados") # [cite: 165]
print(f"Chave AES (256-bit): {key_aes.hex()[:16]}...")
print(f"Dados originais: {dados_simetricos.decode()}")
print(f"Ciphertext (ct): {ct_aes.hex()[:30]}...")

# 3. Decifração
[cite_start]pt_aes = aes.decrypt(nonce, ct_aes, b"metadatos") # [cite: 166]
print(f"Dados decifrados: {pt_aes.decode()}")
print("-------------------------------------------\n")


# --- 4.2: Demonstração de Encriptação Assimétrica (RSA-OAEP) ---
print("--- 4.2: Encriptação Assimétrica (RSA-OAEP) ---")
msg_rsa = b"chave de sessao AES"

# 1. Gerar Par de Chaves (2048-bit)
[cite_start]priv = rsa.generate_private_key(public_exponent=65537, key_size=2048) # [cite: 180]
[cite_start]pub = priv.public_key() # Chave pública para encriptar [cite: 181]

# 2. Encriptação (Usando Chave Pública)
# [cite_start]OAEP é o padding recomendado para RSA [cite: 183]
ct_rsa = pub.encrypt(
    msg_rsa, 
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()), 
        algorithm=hashes.SHA256(), 
        label=None
    )
)
print(f"Chave Privada Gerada (hash): {hash(priv)}")
print(f"Mensagem original (chave): {msg_rsa.decode()}")
print(f"Ciphertext (ct): {ct_rsa.hex()[:30]}...")

# 3. Decifração (Usando Chave Privada)
pt_rsa = priv.decrypt(
    ct_rsa, 
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()), 
        algorithm=hashes.SHA256(), 
        label=None
    )
[cite_start]) # [cite: 185]
print(f"Mensagem decifrada: {pt_rsa.decode()}")
print("-------------------------------------------\n")


# --- 4.3: Demonstração da Solução Híbrida (AES + RSA) ---
print("--- 4.3: Solução Híbrida (AES + RSA) ---")
dados_hibridos = b"mensagem secreta do esquema hibrido"

# 1. Gerar Chaves (RSA para troca, AES para dados)
[cite_start]rsa_priv = rsa.generate_private_key(public_exponent=65537, key_size=2048) # [cite: 200]
rsa_pub = rsa_priv.public_key()
[cite_start]session_key = AESGCM.generate_key(bit_length=256) # Chave de sessão para AES [cite: 202]

# 2. Encriptar Dados (Sender/Client)
[cite_start]aes_sender = AESGCM(session_key) # [cite: 204]
[cite_start]nonce_hibrido = os.urandom(12) # [cite: 205]
[cite_start]ct_dados = aes_sender.encrypt(nonce_hibrido, dados_hibridos, None) # [cite: 206]

# 3. Encriptar Chave de Sessão (AES) com Chave Pública (RSA)
# A chave de sessão AES é o 'segredo' que precisa de ser trocado em segurança.
enc_key = rsa_pub.encrypt(
    session_key,
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()), 
        algorithm=hashes.SHA256(), 
        label=None
    )
[cite_start]) # [cite: 207, 208]
print(f"Dados AES encriptados: {ct_dados.hex()[:30]}...")
print(f"Chave AES encriptada por RSA (enc_key): {enc_key.hex()[:30]}...")

# 4. Decifrar Chave de Sessão (Receiver/Server)
# O servidor usa a sua Chave Privada (RSA) para obter a Chave AES.
dec_key = rsa_priv.decrypt(
    enc_key, 
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()), 
        algorithm=hashes.SHA256(), 
        label=None
    )
[cite_start]) # [cite: 211]

# 5. Decifrar Dados (Receiver/Server)
# O servidor usa a chave AES decifrada para obter os dados.
[cite_start]pt_dados = AESGCM(dec_key).decrypt(nonce_hibrido, ct_dados, None) # [cite: 212]

print(f"Dados originais: {dados_hibridos.decode()}")
print(f"Dados decifrados (pt): {pt_dados.decode()}")
print("-------------------------------------------\n")