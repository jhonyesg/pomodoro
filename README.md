# Pomodoro Timer App

Una aplicación de temporizador Pomodoro desarrollada con `tkinter` para la interfaz gráfica, `Pillow` para la manipulación de imágenes, y `pygame` para la reproducción de sonidos.

## Descripción

Esta aplicación permite a los usuarios seguir la técnica Pomodoro, que consiste en trabajar durante 25 minutos y luego tomar un descanso corto de 5 minutos. Después de cuatro ciclos de trabajo/descanso, se toma un descanso largo de 10 minutos. La interfaz gráfica incluye una imagen de un tomate, botones para iniciar y reiniciar el temporizador, y la funcionalidad para ampliar o reducir la interfaz.

![image](https://github.com/jhonyesg/pomodoro/assets/29180546/29e6fff0-ffa1-4aab-a783-5f50bbb943a7)


## Características

- Temporizador Pomodoro con ciclos de trabajo y descanso.
- Sonido de alarma al finalizar cada intervalo.
- Interfaz gráfica sin barra de título, con una imagen de tomate.
- Opciones para mover la ventana, y ampliar/reducir la interfaz.

## Requisitos

- Python 3.x
- tkinter
- Pillow
- pygame

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/pomodoro-timer.git
    cd pomodoro-timer
    ```

2. Instala las dependencias:
    ```bash
    pip install pillow pygame
    ```

3. Asegúrate de tener los archivos necesarios en los directorios correctos:
   - `tomato.ico`: ícono de la ventana.
   - `tomato.png`: imagen del tomate.
   - `sonido.mp3`: archivo de sonido para la alarma.

## Uso

1. Ejecuta el script:
    ```bash
    python pomodoro.py
    ```

2. Usa los botones para iniciar, reiniciar, ampliar o reducir la interfaz.

## Código

### Estructura

El código está organizado en una clase `PomodoroApp` que maneja la interfaz y la lógica del temporizador.

### Descripción de la Clase `PomodoroApp`

- **Inicialización y Configuración de la Ventana**:
  ```python
  self.root.overrideredirect(True)
  self.root.iconbitmap(r"C:\Users\jhony\Music\pomodoro\tomato.ico")
  pygame.mixer.init()
  self.sound_path = r"C:\Users\jhony\Music\pomodoro\sonido.mp3"
  self.image_path = r"C:\Users\jhony\Music\pomodoro\tomato.png"
  self.load_image()
 
 
