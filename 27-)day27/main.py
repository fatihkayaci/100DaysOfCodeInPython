from tkinter import *

def calculate_km():
    km = round(float(miles_input.get()) * 1.609)
    result_label.config(text = km)

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx= 20, pady= 20)

# input
miles_input = Entry(width=7)
miles_input.grid(column = 1, row = 2)

# label
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column = 2, row = 2)

equal_label = Label(text="is equal to", font=("Arial", 10))
equal_label.grid(column=0, row=3)

result_label = Label(text=0, font=("Arial", 10))
result_label.grid(column=1, row=3)

km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(column=2, row=3)

calculate_button = Button(text="Calculate", command = calculate_km)
calculate_button.grid(column=1, row=4)
window.mainloop()