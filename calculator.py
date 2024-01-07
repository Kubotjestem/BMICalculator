from tkinter import *

def calculate_bmi():
    global bmi_label
    weight = weight_entry.get()
    height = height_entry.get()

    try:
        weight = float(weight)
        height = float(height)
        your_bmi = weight / (height * height)

        if your_bmi < 0:
            result = "There is an error with your input"
        elif your_bmi < 18.5:
            result = f"Your BMI is {your_bmi:.2f} and you are underweight"
        elif your_bmi >= 18.5 and your_bmi < 25:
            result = f"Your BMI is {your_bmi:.2f} and you are normal"
        elif your_bmi >= 25 and your_bmi < 30:
            result = f"Your BMI is {your_bmi:.2f} and you are overweight"
        elif your_bmi >= 30:
            result = f"Your BMI is {your_bmi:.2f} and you are obese"
        else:
            result = "There is an error with your input"

        bmi_label.config(text=result)
    except ValueError:
        bmi_label.config(text="Please enter valid input")

# Create the main window
window = Tk()
window.title("BMI Calculator")
window.geometry("250x250")
window.resizable(False, False)

# Create the weight label and entry field
weight_label = Label(window, text="Weight (kg):")
weight_label.pack()
weight_entry = Entry(window)
weight_entry.pack()

# Create the height label and entry field
height_label = Label(window, text="Height (m ex. 1.75):")
height_label.pack()
height_entry = Entry(window)
height_entry.pack()

# Create the calculate button
calculate_button = Button(window, text="CALCULATE", command=calculate_bmi)
calculate_button.pack()
calculate_button.place(x=90, y=100)

# Create the label to display BMI information
bmi_label = Label(window, text="")
bmi_label.pack()

# Start the main loop
window.mainloop()

