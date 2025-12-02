# --- 1. DATA STRUCTURE SETUP ---
# This is a LIST (like a numbered shopping list) named 'ethiopia_quiz'.
# Each item in the list is a DICTIONARY (a key-value pair container).
# Dictionaries are perfect for grouping related information, like a question and its answer.
ethiopia_quiz = [
    {
        "question": "1. How many volcanoes (active or dormant) are generally estimated to be in Ethiopia?",
        "answer": "58"
    },
    {
        "question": "2. In which region of Ethiopia is the oldest mosque in Africa, Al-Negashi, located?",
        "answer": "tigray"
    },
    { 
        "question": "3. What is the Zagwe dynasty most known for building? ",
        "answer": "Lalibela"
    },
    {
        "question": "4. What was the first major kingdom in Ethiopia?",
        "answer": "Axum"
    },
    # ... (more question dictionaries follow)
    {
        "question": "8. What is the name of the traditional, ancient calendar used by the Oromo people in southern Ethiopia?",
        "answer": "borana calendar"
    }
]

# --- 2. INITIALIZE VARIABLES (Trackers) ---
# 'score' is a simple INTEGER variable set to 0 to track correct answers.
score = 0
# 'incorrect_answers' is an empty LIST where we'll store details of wrong answers later.
incorrect_answers = [] 

# --- 3. START THE PROGRAM (User Interface) ---
# Print the welcome message (A STRING).
print("Welcome to the Ethiopian Knowledge Quiz!")
# Print a separator line (using the multiplication operator * to repeat the string).
print("-" * 30)

# --- 4. THE MAIN LOGIC LOOP ---
# FOR Loop: This is an ITERATION loop. It runs exactly once for every item in the 'ethiopia_quiz' list.
# In each turn, the current question dictionary is stored in the 'quiz_item' variable.
for quiz_item in ethiopia_quiz:
    
    # DICTIONARY ACCESS: Pull the data out of the current dictionary item.
    question = quiz_item["question"]
    correct_answer = quiz_item["answer"]

    # INPUT: Asks the user the question. The answer is stored in 'user_answer'.
    # F-STRING: The 'f' lets us embed the 'question' variable directly into the printed text.
    # .strip(): Removes any accidental spaces from the beginning/end of the user's input.
    # .lower(): Converts the input to all lowercase letters for easy comparison.
    user_answer = input(f"{question}\nYour Answer: ").strip().lower()

    # --- 5. CONDITIONAL STATEMENT (Decision Making) ---
    # IF/ELSE: Checks the condition: Does the user's answer EXACTLY match the correct answer?
    if user_answer == correct_answer:
        print("Correct!\n")
        # ARITHMETIC: Increments the 'score' variable by 1 (shorthand for score = score + 1).
        score += 1
    else:
        # If the answer was wrong, print the correct answer.
        print(f"Incorrect. The correct answer was: {correct_answer}\n")
        
        # LIST METHOD: .append() adds a new dictionary item to the 'incorrect_answers' list.
        # This new dictionary stores all the details needed for the final review.
        incorrect_answers.append({
            "question": question,
            "correct": correct_answer,
            "user_input": user_answer
        })

# --- 6. FINAL RESULTS & SUMMARY ---
# FUNCTION CALL: len() returns the total number of items in the list.
total_questions = len(ethiopia_quiz)

print("-" * 30)
print("QUIZ COMPLETE!")
# Final score is displayed using F-STRING formatting.
print(f"Your final score is: {score}/{total_questions}")

# CONDITIONAL: Checks if the 'incorrect_answers' list is NOT empty.
if incorrect_answers:
    print("\nHere are the questions you got wrong:")
    # FOR Loop: Iterates only through the wrong answers collected.
    for item in incorrect_answers:
        # Prints the stored question, what the user typed, and the correct answer.
        print(f"  Q: {item['question']}")
        print(f"  > You answered: {item['user_input']}")
        print(f"  > Correct answer: {item['correct']}\n")
else:
    # If the list was empty (score was perfect), this message is displayed.
    print("Perfect score! Well done!")
