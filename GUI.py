import tkinter as tk
from tkinter import ttk
from constants import (BG_COLOR, 
                       BTN_COLOR, 
                       FG_COLOR,
                       path_save_constant,
                       APP_WIDTH,
                       APP_HEIGHT)
from templates.template_MRF import MRFProperties_body
from templates.template_momentumTransport import momentumTransport_body

class GUI_class:
    def __init__(self):
        # Hauptfenster erstellen
        self.root = tk.Tk()
        self.root.title("OpenFOAM GUI by Marc Tusenko")
        self.root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.root.configure(bg=BG_COLOR)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")
        self.frame_MRFProperties = tk.Frame(self.notebook, width=APP_WIDTH, height=APP_HEIGHT)
        self.frame2 = tk.Frame(self.notebook, width=APP_WIDTH, height=APP_HEIGHT)
        self.frame3 = tk.Frame(self.notebook, width=APP_WIDTH, height=APP_HEIGHT)

        self.label_mixer_name = tk.Label(self.frame_MRFProperties, height = 1, width = 40, font = ("Arial", 16), text="Hier Rührwerksnamen eingeben:")
        self.label_mixer_name.pack(pady = 10)
        self.entry_mixer_name = tk.Entry(self.frame_MRFProperties, width=25, font=("Arial", 14))
        self.entry_mixer_name.pack(pady=5)

        self.MRF_coordinate_labels = []
        self.MRF_coordinate_entries = []
        MRF_coordinate_label_texts = ["origin x", "origin y", "origin z", "axis x", "axis y", "axis z"]
        self.MRF_coordinate_subframe = tk.Frame(self.frame_MRFProperties, width=APP_WIDTH, height="200")
        for row in range(4):
            for col in range(3):
                if(row % 2 != 0):
                    entry = tk.Entry(
                        self.MRF_coordinate_subframe,
                        width=10,
                        font = ("Arial", 14),
                    )
                    entry.grid(row=row, column=col)
                    self.MRF_coordinate_entries.append(entry)
                else:
                    if(row == 0):
                        label = tk.Label(
                            self.MRF_coordinate_subframe,
                            width=10,
                            font = ("Arial", 16),
                            text=MRF_coordinate_label_texts[col]
                        )
                        label.grid(row=row, column=col)
                        self.MRF_coordinate_labels.append(label)
                    else:
                        label = tk.Label(
                            self.MRF_coordinate_subframe,
                            width=10,
                            font = ("Arial", 16),
                            text=MRF_coordinate_label_texts[col + 3]
                        )
                        label.grid(row=row, column=col)
                        self.MRF_coordinate_labels.append(label)
        self.MRF_coordinate_subframe.pack(pady=10)

        self.MRF_rpm_label = tk.Label(self.frame_MRFProperties, height = 1, width = 20, font = ("Arial", 16), text="Drehzahl:")
        self.MRF_rpm_label.pack(pady = 10)
        self.MRF_rpm_entry = tk.Entry(self.frame_MRFProperties, width=10, font=("Arial", 14))
        self.MRF_rpm_entry.pack(pady=5)

        self.button_MRF_entries = tk.Button(
            self.frame_MRFProperties,
            text="Daten übernehmen",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            activebackground="#505354",
            activeforeground=FG_COLOR,
            command=self.set_MRFProperties
        )
        self.button_MRF_entries.pack(pady=10)

        self.save_button = tk.Button(
            self.frame_MRFProperties,
            text="Speichern",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            activebackground="#505354",
            activeforeground=FG_COLOR,
            command=self.write_MRFProperties
        )
        self.save_button.pack(pady=10)

        self.close_button = tk.Button(
            self.frame_MRFProperties,
            text="Schließen",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            activebackground="#505354",
            activeforeground=FG_COLOR,
            command=self.root.destroy
        )
        self.close_button.pack(expand=True)

        self.frame_MRFProperties.pack(fill="both", expand=True)
        self.frame2.pack(fill="both", expand=True)
        self.frame3.pack(fill="both", expand=True)

        self.notebook.add(self.frame_MRFProperties, text="MRFProperties")
        self.notebook.add(self.frame2, text="Tab2")
        self.notebook.add(self.frame3, text="Tab3")

        #text entries for MRFProperties
        self.mixer_name = ""
        self.x_origin = ""
        self.y_origin = ""
        self.z_origin = ""
        self.x_axis = ""
        self.y_axis = ""
        self.z_axis = ""
        self.rpm = ""
        

        # Ereignisschleife starten
        self.root.mainloop()

    def write_MRFProperties(self):
        file_path = path_save_constant + "/MRFProperties"
        text = MRFProperties_body.format(mixer_name=self.mixer_name, 
                                         x_origin=self.x_origin, 
                                         y_origin=self.y_origin, 
                                         z_origin=self.z_origin,
                                         x_axis=self.x_axis,
                                         y_axis=self.y_axis,
                                         z_axis=self.z_axis,
                                         rpm=self.rpm)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
        return
    
    def set_MRFProperties(self):
        self.mixer_name = self.entry_mixer_name.get()
        self.x_origin = self.MRF_coordinate_entries[0].get()
        self.y_origin = self.MRF_coordinate_entries[1].get()
        self.z_origin = self.MRF_coordinate_entries[2].get()
        self.x_axis = self.MRF_coordinate_entries[3].get()
        self.y_axis = self.MRF_coordinate_entries[4].get()
        self.z_axis = self.MRF_coordinate_entries[5].get()
        self.rpm = self.MRF_rpm_entry.get()
        return

