import tkinter

window=tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=200,height=200)
window.config(padx=20,pady=20)

label=tkinter.Label()
label.config(text="Enter Your Weight (kg)")
label.pack()

entry=tkinter.Entry()
entry.config(width=15)
entry.pack()

label1=tkinter.Label()
label1.config(text="Enter Your Height (cm)")
label1.pack(pady=5)

entry1=tkinter.Entry()
entry1.config(width=15)
entry1.pack()

def click_button():
    if entry.get() == "" or entry1.get() == "":
        text = "Enter both weight and height."
    else:
        try:
            weight = float(entry.get())
            height = float(entry1.get()) / 100
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                text = f"Your BMI is {bmi:.2f}. You are UNDERWEIGHT"
            elif 18.5 <= bmi <= 24.9:
                text = f"Your BMI is {bmi:.2f}. You are NORMAL WEIGHT"
            elif 25.0 <= bmi <= 29.9:
                text = f"Your BMI is {bmi:.2f}. You are OVERWEIGHT"
            elif 30.0 <= bmi <= 34.9:
                text = f"Your BMI is {bmi:.2f}. You are OBESITY CLASS |"
            elif 35.0 <= bmi <= 39.9:
                text = f"Your BMI is {bmi:.2f}. You are OBESITY CLASS ||"
            elif bmi >= 40:
                text = f"Your BMI is {bmi:.2f}. You are OBESITY CLASS |||"
        except ValueError:
            text = "Please enter valid number!"
    result_label.option_clear()
    result_label.config(text=text)
    result_label.pack()

button=tkinter.Button(text="Calculate",command=click_button)
button.pack(pady=10)

result_label=tkinter.Label()

window.mainloop()