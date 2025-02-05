import tkinter as tk
from tkinter import messagebox
import tools as tl


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ski Jumping analysis app")
        self.root.geometry("500x500")

        self.label = tk.Label(self.root, text="Enter the name of the ski jumper", font=("Arial", 12))
        self.label.pack()

        self.myentry = tk.Entry(self.root, font=("Arial", 12))
        self.myentry.pack(pady=5)

        self.button = tk.Button(self.root, text="Submit", font=("Arial", 12), command=self.show_stats)
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
      self.name_label.config(text=f"Statystyki dla skoczka: {name}")

    def show_stats(self):
      name = self.myentry.get()
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


    def on_closing(self):
        if messagebox.askyesno("Quit", "Do you want to quit?"):
          self.root.destroy()


MyGUI()