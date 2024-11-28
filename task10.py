# Quiz on Fundamentals of Programming

def ask_question(question, options, correct_answer):
    print(question)
    for option in options:
        print(option)
    answer = input("Your answer (a/b/c/d): ").strip().lower()
    return answer == correct_answer

def main():
    score = 0
    total_questions = 20

    questions = [
        {
            "question": "1. What is the output of print(2 ** 3)?",
            "options": ["a) 6", "b) 8", "c) 9", "d) 3"],
            "answer": "b"
        },
        {
            "question": "2. Which of the following is a valid variable name?",
            "options": ["a) 1variable", "b) variable_name", "c) variable-name", "d) variable name"],
            "answer": "b"
        },
        {
            "question": "3. What keyword is used to define a function in Python?",
            "options": ["a) define", "b) function", "c) def", "d) fun"],
            "answer": "c"
        },
        {
            "question": "4. Which data type is used to store a sequence of characters?",
            "options": ["a) int", "b) list", "c) str", "d) dict"],
            "answer": "c"
        },
        {
            "question": "5. What will be the output of print(type([]))?",
            "options": ["a) <class 'list'>", "b) <class 'dict'>", "c) <class 'tuple'>", "d) <class 'set'>"],
            "answer": "a"
        },
        {
            "question": "6. How do you start a comment in Python?",
            "options": ["a) //", "b) #", "c) /*", "d) <!--"],
            "answer": "b"
        },
        {
            "question": "7. Which loop is guaranteed to execute at least once?",
            "options": ["a) for loop", "b) while loop", "c) do-while loop", "d) None of the above"],
            "answer": "c"
        },
        {
            "question": "8. What does 'len()' function do?",
            "options": ["a) Returns length of an object", 
                        "b) Converts to string",
                        "c) Returns last element",
                        "d) None of the above"],
            "answer": "a"
        },
        {
            "question": '9. How do you declare a list in Python?',
            "options": ["a) []", 
                        'b) {}', 
                        'c) ()', 
                        'd) <>'],
            "answer": 'a'
        },
        {
            "question": '10. What will be the output of print("Hello"[1])?',
            "options": ["a) H", 
                        'b) e', 
                        'c) l', 
                        'd) o'],
            "answer": 'b'
        },
        {
            'question': '11. Which of these is an immutable data type?',
            'options': ['a) List', 
                        'b) Dictionary', 
                        'c) Set', 
                        'd) Tuple'],
            'answer': 'd'
        },
        {
            'question': '12. What does the break statement do?',
            'options': ['a) Exits a loop', 
                        'b) Skips to next iteration',
                        'c) Exits a function',
                        'd) None of the above'],
            'answer': 'a'
        },
        {
            'question': '13. Which keyword is used for exception handling?',
            'options': ['a) try', 
                        'b) catch', 
                        'c) except', 
                        'd) finally'],
            'answer': 'a'
        },
        {
            'question': '14. What is the purpose of the return statement?',
            'options': ['a) To exit a loop', 
                        'b) To return a value from a function',
                        'c) To terminate a program',
                        'd) None of the above'],
            'answer': 'b'
        },
        {
            'question': '15. Which operator is used for exponentiation?',
            'options': ['a) ^', 
                        'b) **', 
                        'c) +', 
                        'd) -'],
            'answer': 'b'
        },
        {
            'question': '16. What will be the output of print(10 // 3)?',
            'options': ['a) 3.3333',
                        'b) 3',
                        'c) 4',
                        'd) 10'],
            'answer': 'b'
        },
        {
            'question': '17. How can you create a dictionary in Python?',
            'options': ['a) []', 
                        'b) {key: value}', 
                        'c) (key, value)', 
                        'd) {}'],
            'answer': 'd'
        },
        {
          	'question': 	'18. What is used to handle multiple values in Python?',
          	'options': ['a).append()', 
                      	'b).extend()', 
                      	'c).add()', 
                      	'd).insert()'],
          	'answer': 	'a'
          },
          {
          	'question': 	'19. What does JSON stand for?',
          	'options': ['a).JavaScript Object Notation', 
                      	'b).JavaScript Object Network', 
                      	'c).JavaScript Online Notation', 
                      	'd).JavaScript Object Name'],
          	'answer': 	'a'
          },
          {
          	'question': 	'20. Which method can be used to convert an integer to a string?',
          	'options': ['a).str()', 
                      	'b).int()', 
                      	'c).float()', 
                      	'd).string()'],
          	'answer': 	'a'
          }
    ]

    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Your final score: {score}/{total_questions}")

if __name__ == "__main__":
    main()


