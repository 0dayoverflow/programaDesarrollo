import tkinter as tk

window = tk.Tk()

price_label = tk.Label(text="Precio por kWh")
watts_label = tk.Label(text="Watts")
hours_label = tk.Label(text="Horas (encendido)")
cost_label = tk.Label(text="Costo Final")

price_entry = tk.Entry()
watts_entry = tk.Entry()
hours_entry = tk.Entry()

calculate_button = tk.Button(text="Calcular")

price_label.grid(row=0, column=0)
price_entry.grid(row=0, column=1)
watts_label.grid(row=1, column=0)
watts_entry.grid(row=1, column=1)
hours_label.grid(row=2, column=0)
hours_entry.grid(row=2, column=1)
calculate_button.grid(row=3, column=0)
cost_label.grid(row=3, column=1)

def calculate():
    price = float(price_entry.get())
    watts = float(watts_entry.get())
    hours = float(hours_entry.get())
    cost = price * watts * hours / 1000
    cost_label.config(text="Costo: $" + str(cost))

calculate_button.config(command=calculate)

window.mainloop()