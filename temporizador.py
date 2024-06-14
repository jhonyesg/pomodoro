import tkinter as tk
from PIL import Image, ImageTk
import pygame


class PomodoroApp:
    def __init__(self, root):
        self.root = root
        # Hacer la ventana sin barra de título
        self.root.overrideredirect(True)

        # Establecer el ícono de la ventana
        self.root.iconbitmap(r"C:\Users\jhony\Music\pomodoro\tomato.ico")

        # Inicializar pygame mixer para el sonido
        pygame.mixer.init()
        self.sound_path = r"C:\Users\jhony\Music\pomodoro\sonido.mp3"

        # Ruta de la imagen de tomate
        self.image_path = r"C:\Users\jhony\Music\pomodoro\tomato.png"

        # Cargar imagen de tomate
        self.load_image()

        # Crear un canvas para la imagen
        self.canvas = tk.Canvas(root, width=self.tomato_img.width,
                                height=self.tomato_img.height, highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tomato_photo)

        # Crear un label para el temporizador
        self.timer_label = tk.Label(
            root, text="", font=("Helvetica", 24), bg="white")
        self.timer_label.place(x=self.tomato_img.width//2,
                               y=self.tomato_img.height//2 - 30, anchor=tk.CENTER)

        # Botón para iniciar el temporizador
        self.start_button = tk.Button(
            root, text="Iniciar", command=self.start_timer, bg="#FF6347", fg="white", font=("Helvetica", 12))
        self.start_button.place(
            x=self.tomato_img.width//2, y=self.tomato_img.height//2 + 30, anchor=tk.CENTER)

        # Botón para reiniciar el temporizador
        self.reset_button = tk.Button(
            root, text="Reiniciar", command=self.reset_timer, bg="#FF6347", fg="white", font=("Helvetica", 12))
        self.reset_button.place(
            x=self.tomato_img.width//2, y=self.tomato_img.height//2 + 70, anchor=tk.CENTER)

        # Botón para ampliar la interfaz
        self.enlarge_button = tk.Button(
            root, text="Ampliar", command=self.enlarge_interface, bg="#FF6347", fg="white", font=("Helvetica", 12))
        self.enlarge_button.place(
            x=self.tomato_img.width//2 - 30, y=self.tomato_img.height - 30, anchor=tk.CENTER)

        # Botón para reducir la interfaz
        self.reduce_button = tk.Button(
            root, text="Reducir", command=self.reduce_interface, bg="#FF6347", fg="white", font=("Helvetica", 12))
        self.reduce_button.place(
            x=self.tomato_img.width//2 + 30, y=self.tomato_img.height - 30, anchor=tk.CENTER)

        # Variables para el temporizador
        self.work_duration = 25 * 60
        self.short_break = 5 * 60
        self.long_break = 10 * 60
        self.cycles = 4
        self.current_cycle = 0
        self.is_running = False
        self.timer_id = None

        # Hacer la ventana transparente excepto la imagen
        self.root.wm_attributes('-transparentcolor', self.root['bg'])
        self.root.config(bg='white')  # Color de fondo que se hará transparente

        # Permitir mover la ventana
        self.canvas.bind("<ButtonPress-1>", self.start_move)
        self.canvas.bind("<ButtonRelease-1>", self.stop_move)
        self.canvas.bind("<B1-Motion>", self.do_move)

        # Agregar funcionalidad para traer la ventana al frente
        self.root.bind("<Unmap>", self.on_minimize)
        self.root.bind("<Map>", self.on_restore)

    def load_image(self):
        self.tomato_img = Image.open(self.image_path)
        self.tomato_photo = ImageTk.PhotoImage(self.tomato_img)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.run_pomodoro()

    def run_pomodoro(self):
        if self.current_cycle < self.cycles:
            self.current_cycle += 1
            self.update_timer(self.work_duration, "¡Es hora de trabajar!")
            self.countdown(self.work_duration, self.start_break)
        else:
            self.update_timer(self.long_break, "¡Descanso largo!")
            self.countdown(self.long_break, self.reset_timer)

    def start_break(self):
        if self.current_cycle < self.cycles:
            self.update_timer(self.short_break, "¡Descanso corto!")
            self.countdown(self.short_break, self.run_pomodoro)
        else:
            self.update_timer(self.long_break, "¡Descanso largo!")
            self.countdown(self.long_break, self.reset_timer)

    def update_timer(self, duration, message):
        mins, secs = divmod(duration, 60)
        time_format = f'{mins:02}:{secs:02}'
        self.timer_label.config(text=f"{message}\n{time_format}")

    def countdown(self, remaining, next_step):
        if remaining >= 0:
            mins, secs = divmod(remaining, 60)
            time_format = f'{mins:02}:{secs:02}'
            self.timer_label.config(text=time_format)
            self.timer_id = self.root.after(
                1000, self.countdown, remaining - 1, next_step)
        else:
            self.play_sound()
            next_step()

    def play_sound(self):
        pygame.mixer.music.load(self.sound_path)
        pygame.mixer.music.play()

    def reset_timer(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
        self.is_running = False
        self.current_cycle = 0
        self.timer_label.config(text="")

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        x = self.root.winfo_pointerx() - self.x
        y = self.root.winfo_pointery() - self.y
        self.root.geometry(f"+{x}+{y}")

    def enlarge_interface(self):
        new_width = self.tomato_img.width + 50
        new_height = self.tomato_img.height + 50
        self.resize_image(new_width, new_height)

    def reduce_interface(self):
        new_width = self.tomato_img.width - 50
        new_height = self.tomato_img.height - 50
        self.resize_image(new_width, new_height)

    def resize_image(self, new_width, new_height):
        self.tomato_img = self.tomato_img.resize(
            (new_width, new_height), Image.LANCZOS)
        self.tomato_photo = ImageTk.PhotoImage(self.tomato_img)
        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tomato_photo)
        self.timer_label.place(x=new_width//2, y=new_height//2 - 30)
        self.start_button.place(x=new_width//2, y=new_height//2 + 30)
        self.reset_button.place(x=new_width//2, y=new_height//2 + 70)
        self.enlarge_button.place(x=new_width//2 - 30, y=new_height - 30)
        self.reduce_button.place(x=new_width//2 + 30, y=new_height - 30)

    def on_minimize(self, event):
        self.root.iconify()

    def on_restore(self, event):
        self.root.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
