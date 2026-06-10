import base64

# Ler a imagem
with open(r"c:\Users\USER\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1781060791713-pzq8s9wk.png", "rb") as img_file:
    img_data = base64.b64encode(img_file.read()).decode()

# Criar string data URI
data_uri = f"data:image/png;base64,{img_data}"

# Salvar num arquivo para referência
with open("logo_data_uri.txt", "w") as f:
    f.write(data_uri)

print("✓ Data URI gerado! Salvo em logo_data_uri.txt")
print(f"Tamanho: {len(data_uri)} caracteres")
