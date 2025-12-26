import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from constants import *
from templates.template_MRF import MRFProperties_body
from templates.template_momentumTransport import momentumTransport_body
from templates.template_physicalProperties import physicalProperties_body

class GUI_class:
    def __init__(self):
        # Hauptfenster erstellen
        self.root = tk.Tk()
        self.root.title("OpenFOAM GUI by Marc Tusenko")
        self.root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.root.configure(bg=BG_COLOR)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")
        self.frame_costant = tk.Frame(self.notebook, width=APP_WIDTH, height=APP_HEIGHT)
        self.frame_general = tk.Frame(self.notebook, width=APP_WIDTH, height=APP_HEIGHT)
        self.frame3 = tk.Frame(self.notebook, width=APP_WIDTH, height=APP_HEIGHT)

        #general setting GUI
        self.mixer_num_list = list(range(41))
        self.drop_mixer_num = ttk.Combobox(self.frame_general, width=10, values=self.mixer_num_list)
        self.drop_mixer_num.bind("<<ComboboxSelected>>", self.set_mixer_num)
        self.drop_mixer_num.pack(pady=5)

        self.mixer_labels = []
        self.mixer_entries = []

        
        self.label_mixer_name = tk.Label(self.frame_general, height = 1, width = 40, font = ("Arial", LABEL_FONT_SIZE), text="Hier Rührwerksnamen eingeben:")
        self.label_mixer_name.pack(pady = 10)
        self.entry_mixer_name = tk.Entry(self.frame_general, width=25, font=("Arial", LABEL_FONT_SIZE))
        self.entry_mixer_name.pack(pady=5)


        # MRFProperties GUI
        MRF_coordinate_label_texts = ["origin x", "origin y", "origin z", "axis x", "axis y", "axis z"]
        self.MRF_coordinate_subframe = self.build_grid_of_entries(3, 4, MRF_coordinate_label_texts, self.frame_costant)
        self.MRF_coordinate_subframe.pack(pady=10)
        

        self.MRF_rpm_label = tk.Label(self.frame_costant, height = 1, width = 20, font = ("Arial", LABEL_FONT_SIZE), text="Drehzahl:")
        self.MRF_rpm_label.pack(pady = 10)
        self.MRF_rpm_entry = tk.Entry(self.frame_costant, width=10, font=("Arial", LABEL_FONT_SIZE))
        self.MRF_rpm_entry.pack(pady=5)


        # momentumTransport GUI
        momentumTransport_label_texts = ["nu_max", "consistency factor k", "flow index n"]
        self.momentumTransport_subframe = self.build_grid_of_entries(3, 2, momentumTransport_label_texts, self.frame_costant)
        self.momentumTransport_subframe.pack(pady=10)

        self.kin_visc_label = tk.Label(self.frame_costant, height = 1, width = 30, font = ("Arial", LABEL_FONT_SIZE), text="kinematic viscosity [m/s^2]:")
        self.kin_visc_label.pack(pady = 10)
        self.kin_visc_entry = tk.Entry(self.frame_costant, width=10, font=("Arial", LABEL_FONT_SIZE))
        self.kin_visc_entry.pack(pady=5)

        self.button_MRF_entries = tk.Button(
            self.frame_costant,
            text="Daten übernehmen",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            activebackground="#505354",
            activeforeground=FG_COLOR,
            command=self.set_constant_files
        )
        self.button_MRF_entries.pack(pady=10)

        self.save_button = tk.Button(
            self.frame_costant,
            text="Speichern",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            activebackground="#505354",
            activeforeground=FG_COLOR,
            command=self.write_constant_files
        )
        self.save_button.pack(pady=10)

        self.close_button = tk.Button(
            self.frame_costant,
            text="Schließen",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            activebackground="#505354",
            activeforeground=FG_COLOR,
            command=self.root.destroy
        )
        self.close_button.pack(expand=True)
        
        self.frame_general.pack(fill="both", expand=True)
        self.frame_costant.pack(fill="both", expand=True)
        self.frame3.pack(fill="both", expand=True)
        
        self.notebook.add(self.frame_general, text="General Settings")
        self.notebook.add(self.frame_costant, text="Constant Files")
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
        
        #text entries for momentumTransport
        self.nu_max = ""
        self.consistency_faktor_k = ""
        self.flow_index = ""

        #text entries for physicalProperties
        self.kin_visc = ""

        # Ereignisschleife starten
        self.root.mainloop()

    def set_mixer_num(self, event):
        self.mixer_num = int(self.drop_mixer_num.get())
        messagebox.showinfo(
            title="New Selection",
            message=f"Number of mixers: {self.mixer_num}"
        )        
        mixer_label_texts = []
        self.mixer_def_subframe = tk.Frame(self.frame_general, width=APP_WIDTH, height="200", background=SUBCONT_COLOR, relief="raised")
        for row in range(self.mixer_num // 4):
            for col in range(4):
                if(row % 2 != 0):
                    entry = tk.Entry(
                        self.mixer_def_subframe,
                        width=10,
                        font = ("Arial", LABEL_FONT_SIZE),
                    )
                    entry.grid(row=row, column=col, pady=5)
                    self.mixer_entries.append(entry)
                else:
                    label = tk.Label(
                        self.mixer_def_subframe,
                        width=10,
                        font = ("Arial", LABEL_FONT_SIZE),
                        text=mixer_label_texts[col],
                        relief="raised"
                    )
                    label.grid(row=row, column=col, pady=5)
                    self.mixer_labels.append(label)



    def set_general_settings(self):
        self.mixer_name = self.entry_mixer_name.get()

    def write_constant_files(self):
        self.write_MRFProperties()
        self.write_momentumTransport()
        self.write_physicalProperties()

    def set_constant_files(self):
        self.set_MRFProperties()
        self.set_momentumTransport()
        self.set_physicalProperties()

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
        self.x_origin = self.MRF_coordinate_entries[0].get()
        self.y_origin = self.MRF_coordinate_entries[1].get()
        self.z_origin = self.MRF_coordinate_entries[2].get()
        self.x_axis = self.MRF_coordinate_entries[3].get()
        self.y_axis = self.MRF_coordinate_entries[4].get()
        self.z_axis = self.MRF_coordinate_entries[5].get()
        self.rpm = self.MRF_rpm_entry.get()
        return
    
    def write_momentumTransport(self):
        file_path = path_save_constant + "/momentumTransport"
        text = momentumTransport_body.format(nu_max = self.nu_max,
                                             k = self.consistency_faktor_k,
                                             n = self.flow_index)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
        return
    
    def set_momentumTransport(self):
        self.nu_max = self.momentumTransport_entries[0].get()
        self.consistency_faktor_k = self.momentumTransport_entries[1].get()
        self.flow_index = self.momentumTransport_entries[2].get()
        return
    
    def write_physicalProperties(self):
        file_path = path_save_constant + "/physicalProperties"
        text = physicalProperties_body.format(kin_visc = self.kin_visc)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
        return
    
    def set_physicalProperties(self):
        self.kin_visc = self.kin_visc_entry.get()
        return
    
    def build_grid_of_entries(self, columns: int, rows: int, label_texts: list, frame_to_buid):
        labels = []
        entries = []
        subframe = tk.Frame(frame_to_buid, width=APP_WIDTH, height="200", background=SUBCONT_COLOR, relief="raised")
        for row in range(rows):
            for col in range(columns):
                if(row % 2 != 0):
                    entry = tk.Entry(
                        subframe,
                        width=10,
                        font = ("Arial", LABEL_FONT_SIZE),
                    )
                    entry.grid(row=row, column=col, pady=5)
                    entries.append(entry)
                else:
                    label = tk.Label(
                        subframe,
                        width=20,
                        font = ("Arial", LABEL_FONT_SIZE),
                        text=label_texts[col+(row*col)],
                        relief="raised"
                    )
                    label.grid(row=row, column=col, pady=5)
                    labels.append(label)
        return subframe

