# BeRealRecap

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Terminal](https://img.shields.io/badge/Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white)

## Table of Contents / Índice

- [BeRealRecap](#berealrecap)
    - [English](#english)
    - [Español](#español)
- [Tutorial](#tutorial)
    - [How to Use (English)](#how-to-use-english)
    - [Cómo Usar (Español)](#cómo-usar-español)

# Project description

## English

**BeRealRecap** is a Python tool that helps you create a video recap of your BeReal memories. The process involves using **[BeUnblurred](https://github.com/macedonga/beunblurred)** to communicate with BeReal and fetch images from your account, then processing them to create a personalized video.

This tool automates the task of generating a video recap of your BeReal memories by processing the images and adding effects like rounded corners, borders, and a date overlay.

## Español

**BeRealRecap** es una herramienta en Python que te ayuda a crear un video resumen de tus recuerdos de BeReal. El proceso implica usar **[BeUnblurred](https://github.com/macedonga/beunblurred)** para comunicarse con BeReal y obtener las imágenes de tu cuenta, luego procesarlas para crear un video personalizado.

Esta herramienta automatiza la tarea de generar un video resumen de tus recuerdos de BeReal procesando las imágenes y agregando efectos como esquinas redondeadas, bordes y una superposición de fecha.

# Tutorial

## How to Use (English)

### Prerequisites

- Python installed on your system
- A BeReal account (for obtaining images)
- [BeUnblurred - by: @macedonga](https://github.com/macedonga/beunblurred)

### Installation

1. **Clone this repository to your local machine:**
    ```bash
    git clone https://github.com/emlopezr/BeRealRecap.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd BeRealRecap
    ```

### Virtual Environment Setup

1. **Install virtualenv:**
    ```bash
    pip install virtualenv
    ```

2. **Create the Virtual Environment:** Use any of these commands
    ```bash
    python -m venv .venv
    python3 -m venv .venv
    py -m venv .venv
    ```
    This will create a directory named `.venv` in your project folder containing all the necessary files for your virtual environment.

3. **Activate the Virtual Environment:**
    - Windows: ```.venv\Scripts\activate```
    - Linux / MacOS: ```source .venv/bin/activate```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Download and set up BeUnblurred repository** to fetch BeReal images from your account and store them in a folder named `images` in the root of this project.
    - Follow README instructions of [macedonga/beunblurred](https://github.com/macedonga/beunblurred)

2. **Authenticate and fetch your BeReal images** using the BeUnblurred tool. This step involves authenticating with your BeReal account to download the images.
    - Go to Memories Feed (Wait for all images to load, the first time may take a few minutes)
    ![Memories Feed](/tutorial/image.png)
    - Right-click -> Inspect Element or press Ctrl + Shift + C
    ![Inspect Element](/tutorial/image-1.png)
    - Go to Console and paste the content of [`scrap.js`](https://github.com/emlopezr/BeRealRecap/blob/main/scrap.js) and press Enter
    ![Scrap](/tutorial/image-2.png)
    - Download the resulting `.zip` file and extract it in the project folder
    ![Zip File](/tutorial/image-3.png)

3. **Run the Python program:**
    - Execute the script [`recap.py`](https://github.com/emlopezr/BeRealRecap/blob/main/recap.py) to generate your recap video (Use any of the following commands)
    ```bash
    python recap.py
    python3 recap.py
    py recap.py
    ```

The tool will process the images, add the necessary effects, and create a video output with rounded edges, a border around the front image, and a date overlay.

## Cómo Usar (Español)

### Requisitos Previos

- Python instalado en tu sistema
- Una cuenta de BeReal (para obtener imágenes)
- Repositorio **BeUnblurred** (para comunicarse con BeReal y obtener las imágenes) - [Enlace al repositorio BeUnblurred](https://github.com/macedonga/beunblurred)

### Instalación

1. **Clona este repositorio en tu máquina local:**
    ```bash
    git clone https://github.com/emlopezr/BeRealRecap.git
    ```

2. **Navega al directorio del proyecto:**
    ```bash
    cd BeRealRecap
    ```

### Configuración del Entorno Virtual

1. **Instala virtualenv:**
    ```bash
    pip install virtualenv
    ```

2. **Crea el Entorno Virtual:** Utiliza alguno de estos comandos
    ```bash
    python -m venv .venv
    python3 -m venv .venv
    py -m venv .venv
    ```
    Esto creará un directorio llamado `.venv` en la carpeta de tu proyecto que contendrá todos los archivos necesarios para tu entorno virtual.

3. **Activa el Entorno Virtual:**
    - Windows: ```.venv\Scripts\activate```
    - Linux / MacOS: ```source .venv/bin/activate```

4. **Instala las Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### Uso

1. **Descarga y configura el repositorio BeUnblurred** para comunicarte con BeReal y obtener las imágenes de tu cuenta, almacenándolas en una carpeta llamada `images` en la raíz de este proyecto.
    - Sigue las instrucciones del README de [macedonga/beunblurred](https://github.com/macedonga/beunblurred)

2. **Autentica tu cuenta BeReal** para descargar las imágenes utilizando la herramienta BeUnblurred.
    - Ve a Memories Feed (Espera a que todas las imágenes carguen, la primera vez puede demorar algunos minutos)
    ![Memories Feed](/tutorial/image.png)
    - Da clic derecho -> Inspeccionar Elemento o presiona Ctrl + Shift + C
    ![Inspeccionar Elemento](/tutorial/image-1.png)
    - Ve a la Consola y pega el contenido de [`scrap.js`](https://github.com/emlopezr/BeRealRecap/blob/main/scrap.js) y presiona Enter
    ![Scrap](/tutorial/image-2.png)
    - Descarga el archivo .zip resultante y descomprímelo en la carpeta del proyecto
    ![Zip File](/tutorial/image-3.png)

3. **Ejecuta el programa Python:**
    - Ejecuta el script [`recap.py`](https://github.com/emlopezr/BeRealRecap/blob/main/recap.py) para generar el video resumen:
    ```bash
    python recap.py
    python3 recap.py
    py recap.py
    ```

La herramienta procesará las imágenes, les añadirá los efectos necesarios y creará un video de salida con bordes redondeados, un borde alrededor de la imagen frontal y una superposición de la fecha.
