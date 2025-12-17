import tkinter as tk
from constants import (BG_COLOR, 
                       BTN_COLOR, 
                       FG_COLOR,
                       path_save)

class GUI_class:
    def __init__(self):
        # Hauptfenster erstellen
        self.root = tk.Tk()
        self.root.title("OpenFOAM GUI by Marc Tusenko")
        self.root.geometry("1300x800")

        self.root.configure(bg=BG_COLOR)

        self.label_file_name = tk.Label(self.root, height = 1, width = 20, font = ("Arial", 16), text="Hier Dateinamen eingeben:")
        self.label_file_name.pack(pady = 10)

        self.entry_file_name = tk.Entry(self.root, width=25, font=("Arial", 14))
        self.entry_file_name.pack(pady=5)

        self.label_info = tk.Label(self.root, height = 1, width = 20, font = ("Arial", 16), text="Hier Dateiinhalt eingeben:")
        self.label_info.pack(pady = 10)

        self.textbox = tk.Text(self.root, height=3, width=50)
        self.textbox.pack(pady=5)

        self.save_button = tk.Button(
            self.root,
            text="Speichern",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            activebackground="#505354",
            activeforeground=FG_COLOR,
            command=self.write_file
        )
        self.save_button.pack(pady=10)

        self.close_button = tk.Button(
            self.root,
            text="Schließen",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            activebackground="#505354",
            activeforeground=FG_COLOR,
            command=self.root.destroy
        )
        self.close_button.pack(expand=True)

        # Ereignisschleife starten
        self.root.mainloop()

    def write_file(self):
        file_name = self.entry_file_name.get()
        file_path = path_save + "/" + file_name
        text = self.textbox.get('1.0', tk.END)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
        return

