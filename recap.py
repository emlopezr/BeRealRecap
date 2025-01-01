import cv2
import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta

IMAGES_DIR = 'images'
VIDEO_OUTPUT_PATH = 'recap.avi'
FPS = 3

def format_date(date_str):
    # Suma un día a la fecha y la convierte a un formato más legible
    date_str = date_str.replace("_", "/")
    date_obj = datetime.strptime(date_str, "%Y/%m/%d") + timedelta(days=1)
    return date_obj.strftime("%d/%B/%Y")

def get_images_from_folder(directory):
    images = [ filename for filename in os.listdir(directory) ]

    # Organiza por fecha (año, mes, día) ascendente y por índice de imagen (0, 1, 2, ...) descendente
    images.sort(key=lambda x: (x.split("_")[0:3], int(x.split("_")[-1].replace(".png", ""))))
    return images

def add_rounded_border_to_front_image(image, border_radius, border_thickness=12):
    # Asegurarse de que la imagen sea en formato RGBA (con canal alfa)
    image = image.convert("RGBA")

    # Crear una máscara redondeada para la imagen frontal
    width, height = image.size
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, width, height], radius=border_radius, fill=255)

    # Crear una imagen transparente con el borde negro
    bordered_img = Image.new('RGBA', (width + 2 * border_thickness, height + 2 * border_thickness), (0, 0, 0, 255))

    # Redondear la imagen y pegarla sobre la nueva imagen (con borde negro)
    rounded_image = Image.new('RGBA', (width, height), (0, 0, 0, 0))  # Imagen transparente
    rounded_image.paste(image, (0, 0), mask)  # Pega la imagen con bordes redondeados

    bordered_img.paste(rounded_image, (border_thickness, border_thickness), mask=mask)

    return bordered_img

def draw_text_with_shadow_and_border(draw, text, position, font, text_color=(255, 255, 255), shadow_color=(0, 0, 0), border_color=(0, 0, 0), border_width=3):
    # Sombra: dibujar el texto desplazado ligeramente
    x, y = position
    for offset in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
        draw.text((x + offset[0], y + offset[1]), text, font=font, fill=shadow_color)

    # Borde: dibujar el texto varias veces con un desplazamiento pequeño
    for offset in range(-border_width, border_width + 1):
        if offset != 0:
            draw.text((x + offset, y), text, font=font, fill=border_color)
            draw.text((x, y + offset), text, font=font, fill=border_color)

    # Texto principal (sobre sombra y borde)
    draw.text((x, y), text, font=font, fill=text_color)

def generate_dates_with_images(start_date, end_date):
    # Convierte las fechas de inicio y fin a objetos datetime
    start = datetime.strptime(start_date, "%Y_%m_%d")
    end = datetime.strptime(end_date, "%Y_%m_%d")

    # Generar una lista de fechas desde start_date hasta end_date
    current_date = start
    while current_date <= end:
        # Generar la fecha en formato YYYY_MM_DD
        formatted_date = current_date.strftime("%Y_%m_%d")

        # Iterar sobre los índices de imagen (_0, _1, _2, ...) al revés (de 2 a 0)
        for i in range(2, -1, -1):
            yield f"{formatted_date}_{i}"  # Genera el nombre de la imagen con el índice

        # Incrementar un día
        current_date += timedelta(days=1)

def print_progress_bar(iterable, total, prefix='', length=40):
    iteration = 0
    for item in iterable:
        iteration += 1
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = '█' * filled_length + '-' * (length - filled_length)
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% Complete')
        sys.stdout.flush()
        yield item
    sys.stdout.write('\n')  # Nueva línea al final

start_date = "2023_12_31"
end_date = "2025_12_31"

total_elements = sum(1 for _ in generate_dates_with_images(start_date, end_date))

# Crear el video a partir de las imágenes
def create_video_from_images(images):
    first_image = Image.open(os.path.join(IMAGES_DIR, images[0]))
    width, height = first_image.size
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(VIDEO_OUTPUT_PATH, fourcc, FPS, (width, height))

    # Agregar imágenes al video - Muestra un progreso en la consola
    for image_name in print_progress_bar(generate_dates_with_images(start_date, end_date), total_elements, prefix="Procesando imágenes"):
        splitted = image_name.split("_")

        date_str = splitted[0:3]
        iterator = splitted[-1]
        formatted_date = format_date("_".join(date_str))

        # Cargar las imágenes de fondo y front
        back_image_path = os.path.join(IMAGES_DIR, f"{'_'.join(date_str)}_back_{iterator}.png")
        front_image_path = os.path.join(IMAGES_DIR, f"{'_'.join(date_str)}_front_{iterator}.png")

        # Imagenes por defecto
        back_img = Image.new('RGBA', (width, height), color=(0, 0, 0, 1))  # Imagen negra
        front_img = Image.new('RGBA', (width, height), color=(1, 1, 1, 1))  # Imagen blanca

        # Cambiar las imágenes por las reales si existen, sino saltar a la siguiente iteración
        if os.path.exists(back_image_path):
            back_img = Image.open(back_image_path)
            back_img = back_img.convert("RGBA")
        else:
            continue

        if os.path.exists(front_image_path):
            front_img = Image.open(front_image_path)
            front_img = front_img.convert("RGBA")
        else:
            continue


        # Crear una imagen con la imagen de fondo
        frame = back_img.copy()

        # Poner la imagen front sobre la de fondo (en la esquina superior derecha)
        front_img = add_rounded_border_to_front_image(front_img, 0)  # Añadir un borde redondeado
        front_img = front_img.resize((int(width * 0.25), int(height * 0.25)))  # Redimensionar la imagen front

        frame = frame.convert("RGBA")
        frame.paste(front_img, (50, 50), front_img)  # Pega en la esquina superior izquierda

        # Añadir el texto con la fecha en la parte inferior izquierda
        draw = ImageDraw.Draw(frame)
        font = ImageFont.truetype("font/Roboto-Medium.ttf", 60)
        bbox = draw.textbbox((60, 60), formatted_date, font=font)  # Obtiene las coordenadas del texto
        text_height = bbox[3] - bbox[1]  # Alto del texto
        draw_text_with_shadow_and_border(draw, formatted_date, (50, height - text_height - 50), font, text_color=(255, 255, 255), shadow_color=(0, 0, 0), border_color=(0, 0, 0))


        # Convertir la imagen de PIL a un formato que OpenCV pueda usar
        frame_cv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

        # Añadir la imagen al video
        out.write(frame_cv)

    # Finaliza el video
    out.release()
    print(f"Video guardado como {VIDEO_OUTPUT_PATH}")

# Main
if __name__ == "__main__":
    images = get_images_from_folder(IMAGES_DIR)
    create_video_from_images(images)