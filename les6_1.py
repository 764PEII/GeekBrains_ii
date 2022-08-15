import tkinter as tk

w = tk.Tk()
class Trafficlight():
    w.title("TrafficLight")
    w.geometry("500x500")
    w['bg'] = 'red'

    def one(self):
        w['bg'] = 'red'

    def two(self):
        w['bg'] = 'yellow'

    def three(self):
        w['bg'] = 'green'

    def run(self):
        w.after(4500, self.two)

        w.after(6000, self.three)

        w.after(9000, self.one)

light = Trafficlight()
light.run()

w.tk.mainloop()
