[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FJiO-WNb)
# Signal Processor (for periodic signals)

This program allows you to calculate Rectangular Fourier Coefficients in use for signal analysis. The coefficients are integrated from 0 to T for some periodic signal.

The a<sub>0</sub> coefficient, a<sub>1</sub> - a<sub>5</sub> coefficients and b<sub>1</sub> - b<sub>5</sub> coefficients are printed as both an expression and a numerical value.

All calculations are done through the Python library SymPy. The variables that may be used in expressions are A, T, and t.

## Usage

The program is started by invoking `python3 main.py`

Functions can be entered as a mathematical formula, with variables being allowed. Piecewise functions may also be entered (see Test Cases). The function must follow SymPy's syntax for expressions (which, for the most part, is just Python's syntax). You are then prompted to enter your choice of A and T. Afterwards, your coefficients will be calculated.

Multiple functions may be calculated in one session. When you are ready to stop, enter "X"

## Test Cases

### Test Case 1
![Graph of a periodic signal](images/image-1.png)

For this function, which is f(t) = -2At/T + A, we will use A = 5 and T = 4.

This is entered into the program as follows:

![Example input](images/image-2.png)

Which gives us the resulting output:

![Example output](images/image-3.png)

