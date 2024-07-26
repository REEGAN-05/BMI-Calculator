# BMI Calculator

A simple BMI(Body Mass Index) calculator application with both command-line and graphical user interface (GUI) versions using Python.

## Features

### Command-Line Version

- **User Input:** Prompt users to enter their weight (in kilograms) and height (in centimeters).
+ **BMI Calculation:** Calculate the BMI using the formula BMI = weight / (height in meters * height in meters), converting height from centimeters to meters.
- **Classification:** Classify the BMI into categories such as underweight, normal weight, overweight, or obesity.
- **Output:** Display the calculated BMI and its category to the user.

### GUI Version
- **User-Friendly Interface:** Developed using Tkinter for an intuitive and interactive user experience.
- **Input Fields:** Allow users to enter their weight and height.
- **BMI Calculation:** Compute and display the BMI within the GUI.
- **Categorization:** Show the BMI category based on predefined ranges.
- **Graphical Representation:** Display an image representing the BMI category (underweight, normal weight, overweight, or obesity).

## Requirements
- Python 3.x
- Tkinter (for the GUI version)
- Pillow library (for image handling): Install using
 ```sh
  pip install pillow
```
## Usage

### Command-Line Version
Run the script sh `bmi_calculator.py to start the command-line BMI calculator.

### GUI Version
Run the script `bmi_calculator.py` to start the GUI BMI calculator.

```sh
python bmi_calculator.py
