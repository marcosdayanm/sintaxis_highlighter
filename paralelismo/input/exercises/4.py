import tkinter as tk

def convert_to_euros(dollars):
    return dollars * 0.88

def convert_to_dollars(euros):
    return euros / 0.88

def on_convert():
    amount = float(entry.get())
    if var.get() == 'Dollars to Euros':
        result = convert_to_euros(amount)
    else:
        result = convert_to_dollars(amount)
    label_result.config(text=f"Result: {result:.2f}")

root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount:").grid(row=0, column=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

var = tk.StringVar(root)
var.set("Dollars to Euros")
choices = ['Dollars to Euros', 'Euros to Dollars']
option = tk.OptionMenu(root, var, *choices)
option.grid(row=1, column=0, columnspan=2)

button_convert = tk.Button(root, text="Convert", command=on_convert)
button_convert.grid(row=2, column=0, columnspan=2)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=3, column=0, columnspan=2)

root.mainloop()
