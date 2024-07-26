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
## Images

The GUI version of the BMI Calculator includes graphical representations of the BMI categories. To ensure these images are displayed correctly, follow these instructions:

### Images Required
The following images are used to visually represent the different BMI categories:

- `underweight.png` – Represents the underweight category.
- `normal.png` – Represents the normal weight category.
- `overweight.png` – Represents the overweight category.
- `obesity.png` – Represents the obesity category.

## Usage

### Command-Line and GUI Version

Both the command-line and GUI versions can be run using the same script. The application will open with a graphical interface.

To run the BMI calculator:

```sh

python bmi_calculator.py

```
## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/REEGAN-05/BMI-Calculator/blob/main/LICENSE) file for details.

## Acknowledgements

- Inspired by the need for a simple yet effective BMI calculator.
- Developed using Python and the Tkinter library for the GUI.
- Images used to represent BMI categories should be credited appropriately if sourced from online resources.
