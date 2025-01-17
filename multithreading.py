import tkinter as tk
import os, sys, time, random as r
import threading

def task(label, lb, ub, refreshTime):
    while True:
        num = r.randint(lb, ub)
        label.config(text=f"{num}\n[{lb}, {ub}]\nrefresh time = {refreshTime}")
        time.sleep(refreshTime)
    return

def create_dashboard():
    root = tk.Tk()
    root.title("Random Number Dashboard")

    ranges_and_times = [
        (10, 20, 10, "lightseagreen"),
        (-10, 10, 20, "salmon"),
        (-100, 0, 8, "gold"),
        (0, 20, 12, "cornflowerblue"),
        (-40, 40, 16, "orchid"),
        (100, 200, 14, "palegreen")
    ]
    labels = []
    for i, (lb, ub, refresh_time, color) in enumerate(ranges_and_times):
        label = tk.Label(root, text="0", font=("Helvetica", 16), width=15, height=5, bg=color)
        label.grid(row=i//2, column=i%2, padx=20, pady=20)
        labels.append((label, lb, ub, refresh_time))

    for label, lb, ub, refresh_time in labels:
        thread = threading.Thread(target=task, args=(label, lb, ub, refresh_time))
        thread.daemon = True
        thread.start()

    root.mainloop()

if __name__ == "__main__":
    create_dashboard()
