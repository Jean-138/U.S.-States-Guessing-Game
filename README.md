# U.S. States Guessing Game

## Description
This project is a Python game where I try to guess all 50 states of the United States.  
When I enter the name of a state correctly, it is displayed on the map in its correct location.  
If I choose to exit before finishing, a CSV file is generated with the states I still need to learn.

## How it works
- The game shows a blank U.S. map.
- I enter state names in the input box.
- Correct guesses are written on the map.
- The game continues until I guess all 50 states or type "Exit".
- If I exit, a file called **`states_to_learn.csv`** is created with the missing states.

## Requirements
- Python 3
- `pandas`
- `turtle`

## How to run
1. Clone the repository.
2. Make sure the file `50_states.csv` and `blank_states_img.gif` are in the same folder.
3. Run the Python script:
   ```bash
   python main.py


    ## Credits
This project was completed as part of Dr. Angela Yu's "100 Days of Code: The Complete Python pro Bootcamp" course.
