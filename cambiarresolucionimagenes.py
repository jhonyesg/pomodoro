from PIL import Image
import os

# Directorio donde están las imágenes
input_folder = r"C:\Users\jhony\Downloads\canal8 Sucre"
output_folder = r"C:\Users\jhony\Downloads\canal8 Sucre\resized"

# Crear el directorio de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Dimensiones deseadas
new_width = 1024
new_height = 500

# Redimensionar imágenes
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        img.save(os.path.join(output_folder, filename))
        print(f"{filename} redimensionada y guardada.")

print("Todas las imágenes han sido redimensionadas.")
