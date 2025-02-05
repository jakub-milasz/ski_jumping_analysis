import tkinter as tk
from tkinter import messagebox, Button
import tools as tl
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ski Jumping analysis app")
        self.root.geometry("800x500")
        self.canvas = None

        self.label = tk.Label(self.root, text="Wpisz nazwisko i imię skoczka narciarskiego", font=("Arial", 12))
        self.label.pack()

        self.myentry = tk.Entry(self.root, font=("Arial", 12))
        self.myentry.pack(pady=5)

        self.button = tk.Button(self.root, text="Zatwierdź", font=("Arial", 12), command=self.show_stats)
        self.button.pack(pady=5)

        self.name_label = tk.Label(self.root, font=("Arial", 12))
        self.name_label.pack()

        stats_frame = tk.Frame(self.root)
        stats_frame.columnconfigure(0, weight=1)
        stats_frame.columnconfigure(1, weight=1)

        self.title1 = tk.Label(stats_frame, text="Ulubiona skocznia normalna", font=("Arial", 12))
        self.title1.grid(row=0, column=0)

        self.title2 = tk.Label(stats_frame, text="Ulubiona skocznia duża", font=("Arial", 12))
        self.title2.grid(row=0, column=1)

        self.value1 = tk.Label(stats_frame, font=("Arial", 12))
        self.value1.grid(row=1, column=0, )

        self.value2 = tk.Label(stats_frame, font=("Arial", 12))
        self.value2.grid(row=1, column=1)

        self.title3 = tk.Label(stats_frame, text="Ulubiona skocznia mamucia", font=("Arial", 12))
        self.title3.grid(row=2, column=0)

        self.title4 = tk.Label(stats_frame, text="Ilość skoków za HS", font=("Arial", 12))
        self.title4.grid(row=2, column=1)

        self.value3 = tk.Label(stats_frame, font=("Arial", 12))
        self.value3.grid(row=3, column=0)

        self.value4 = tk.Label(stats_frame, font=("Arial", 12))
        self.value4.grid(row=3, column=1)

        self.title5 = tk.Label(stats_frame, text="Średnia ocena za styl", font=("Arial", 12))
        self.title5.grid(row=4, column=0)

        self.title6 = tk.Label(stats_frame, text="Średnia rekompensata za wiatr", font=("Arial", 12))
        self.title6.grid(row=4, column=1)

        self.value5 = tk.Label(stats_frame, font=("Arial", 12))
        self.value5.grid(row=5, column=0)

        self.value6 = tk.Label(stats_frame, font=("Arial", 12))
        self.value6.grid(row=5, column=1)

        stats_frame.pack(expand=True, fill="both")

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self, name):
      self.name_label.config(text=f"Statystyki dla skoczka: {name} (2008 - 2022)")

    def show_stats(self):
      name = self.myentry.get().lower()
      if name not in tl.names['name'].str.lower().values:
        messagebox.showerror("Error", "Nie ma takiego skoczka w bazie danych")
        return
      self.show_message(name)
      fav_normal = tl.analyse_skijumper('normalne', name)
      fav_large = tl.analyse_skijumper('duże', name)
      fav_flying = tl.analyse_skijumper('mamucie', name)
      self.value1.config(text=fav_normal)
      self.value2.config(text=fav_large)
      self.value3.config(text=fav_flying)
      stats = tl.analyse_overall_stats(name)
      self.value4.config(text=stats[0])
      self.value5.config(text=stats[1].round(1))
      self.value6.config(text=stats[2].round(2))
      self.hist(name)

    def hist(self, name):
      res = tl.merged[tl.merged['codex_x'] == tl.find_codex(name)]
      fig = Figure(figsize = (10, 10), dpi = 100) 
      plot = fig.add_subplot(111) 
      plot.hist(res['dist'], bins=100)
      plot.set_title(f"Rozkład odległości uzyskanych przez skoczka {name}")
      if self.canvas:
        self.canvas.get_tk_widget().destroy()
      self.canvas = FigureCanvasTkAgg(fig, master = self.root)   
      self.canvas.draw() 
      self.canvas.get_tk_widget().pack() 

    def on_closing(self):
      if messagebox.askyesno("Quit", "Do you want to quit?"):
        self.root.destroy()


MyGUI()