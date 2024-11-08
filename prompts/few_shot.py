FEW_SHOT_PROMPT = """
Given the following topic {input}, generate a quiz with 5 questions that increase in difficulty.
For each question first display the questions followed by four options one of which is correct.
The user should be able to select the correct answer by typing the option number into a input box.
Then the user should submit the answer by clicking a button.
Once the user submits the answer, the correct answer should be displayed.

here is an example of how the quiz should look like:

Prompt or question
A) options[0]
B) option[1]
C) option[2]
D) option[3]

text box for user to input answer
submit button

correct answer (to be displayed after user submits answer)
"""