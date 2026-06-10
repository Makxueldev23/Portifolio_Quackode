import shutil
import os

src = r"c:\Users\USER\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1781060791713-pzq8s9wk.png"
dst = r"c:\Users\USER\OneDrive\Desktop\Quackode\logo-quackode.png"

if os.path.exists(src):
    shutil.copy2(src, dst)
    print(f"✓ Imagem copiada com sucesso!")
else:
    print(f"✗ Arquivo de origem não encontrado: {src}")
