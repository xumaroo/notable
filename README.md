To run the code, go to the file path and run main.py. 
You will be promted to input some text to transcribe. 
If left blank, it will default toto the example given. 

Some assumptions I made:
* There can only be one "Number n" in the text. Any further occurences will be assumed to be part of a list. For example:
    4. Patient is taking drug number five several times a week
* If the user starts with a number n > 1, the list will start at that number and the list will not include any items from 1 to n.