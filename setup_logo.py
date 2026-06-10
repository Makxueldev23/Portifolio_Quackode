import base64
import os

# Caminho da imagem do pato
src = r"c:\Users\USER\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1781060791713-pzq8s9wk.png"
dst = r"c:\Users\USER\OneDrive\Desktop\Quackode\logo.png"

# Copiar a imagem para a pasta do projeto
if os.path.exists(src):
    with open(src, 'rb') as f_src:
        with open(dst, 'wb') as f_dst:
            f_dst.write(f_src.read())
    print(f"✓ Imagem copiada para: {dst}")
    print("✓ Agora o HTML está pronto para deploy!")
else:
    print(f"✗ Arquivo não encontrado: {src}")

