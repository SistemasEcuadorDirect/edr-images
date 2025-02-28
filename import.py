import os

dir_path = "C:/Users/diseno/Desktop/ROSES"  # Reemplaza con tu ruta

for file in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file)):
        name, ext = os.path.splitext(file)
        print(f"{name}{ext}") 