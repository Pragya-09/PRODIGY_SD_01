import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        original_unit = combo_original_unit.get()
        if original_unit == "Celsius":
            celsius = temperature
            fahrenheit = celsius * 9/5 + 32
            kelvin = celsius + 273.15
        elif original_unit == "Fahrenheit":
            fahrenheit = temperature
            celsius = (fahrenheit - 32) * 5/9
            kelvin = (fahrenheit - 32) * 5/9 + 273.15
        else:  # Kelvin
            kelvin = temperature
            celsius = kelvin - 273.15
            fahrenheit = celsius * 9/5 + 32
        
        label_result.config(text=f"{celsius:.2f} °C\n{fahrenheit:.2f} °F\n{kelvin:.2f} K")
    except ValueError:
        label_result.config(text="Invalid input!")

# Create main window
window = tk.Tk()
window.title("Temperature Converter")

# Temperature entry
label_temperature = tk.Label(window, text="Enter Temperature:")
label_temperature.grid(row=0, column=0, padx=10, pady=5)
entry_temperature = tk.Entry(window)
entry_temperature.grid(row=0, column=1, padx=10, pady=5)

# Original unit selection
label_original_unit = tk.Label(window, text="Original Unit:")
label_original_unit.grid(row=1, column=0, padx=10, pady=5)
options = ["Celsius", "Fahrenheit", "Kelvin"]
combo_original_unit = tk.StringVar(window)
combo_original_unit.set(options[0])
combo_original_unit_menu = tk.OptionMenu(window, combo_original_unit, *options)
combo_original_unit_menu.grid(row=1, column=1, padx=10, pady=5)

# Convert button
button_convert = tk.Button(window, text="Convert", command=convert_temperature)
button_convert.grid(row=2, columnspan=2, padx=10, pady=5)

# Result label
label_result = tk.Label(window, text="")
label_result.grid(row=3, columnspan=2, padx=10, pady=5)

window.mainloop()
