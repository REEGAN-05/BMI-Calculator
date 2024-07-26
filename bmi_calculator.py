import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        if weight <= 0 or height_cm <= 0:
            raise ValueError
        height_m = height_cm / 100  # Convert height from cm to meters
        bmi = weight / (height_m ** 2)
        category = classify_bmi(bmi)
        result_label.config(text=f"Your BMI is {bmi:.2f}. You are {category}.")
        show_image(category)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid positive numbers for weight and height.")

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def show_image(category):
    if category == "Underweight":
        image_path = "images/underweight.png"
    elif category == "Normal weight":
        image_path = "images/normal.png"
    elif category == "Overweight":
        image_path = "images/overweight.png"
    else:  # Obesity
        image_path = "images/obesity.png"

    image = Image.open(image_path)
    image = image.resize((200, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection

# Set up the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place widgets
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Height (cm):").grid(row=1, column=0, padx=10, pady=5)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

image_label = tk.Label(root)
image_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
