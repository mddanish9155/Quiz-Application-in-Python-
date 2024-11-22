import random

py_q = {
    "DSA": {
        1: ["What does DSA stand for?", "Data Science Analysis", "Data Structure and Algorithms", "Data Security Administration", "Data System Analysis", 2],
        2: ["Which of the following is not a data structure?", "Array", "Stack", "Queue", "Function", 4],
        3: ["What is the time complexity of binary search?", "O(n)", "O(log n)", "O(n log n)", "O(1)", 2],
        4: ["What is the worst-case time complexity of bubble sort?", "O(n)", "O(n^2)", "O(log n)", "O(n log n)", 2],
        5: ["Which data structure uses LIFO?", "Queue", "Stack", "Array", "Linked List", 2]
    },
    "DBMS": {
        1: ["What does DBMS stand for?", "Database Management System", "Data Backup Management System", "Database Maintenance System", "Data Management System", 1],
        2: ["Which of the following is a type of database?", "Relational", "Flat File", "Hierarchical", "All of the above", 4],
        3: ["What is SQL used for?", "Data Manipulation", "Data Definition", "Data Control", "All of the above", 4],
        4: ["What does ACID stand for?", "Atomicity, Consistency, Isolation, Durability", "Accuracy, Consistency, Isolation, Durability", "Atomicity, Consistency, Isolation, Delivery", "Atomicity, Consistency, Integrity, Durability", 1],
        5: ["Which SQL statement is used to retrieve data?", "GET", "SELECT", "PICK", "RETRIEVE", 2]
    },
    "Python": {
        1: ["What is the output of print(2 ** 3)?", "6", "8", "9", "4", 2],
        2: ["Which keyword is used to define a function in Python?", "function", "def", "func", "define", 2],
        3: ["What data type is the result of 3 / 2?", "Integer", "Float", "String", "Complex", 2],
        4: ["What is a lambda function?", "A type of loop", "A small anonymous function", "A built-in function", "A type of error", 2],
        5: ["Which of the following is a mutable type?", "Tuple", "List", "String", "Dictionary", 2]
    }
}

def shuffle_questions(questions):
    question_ids = list(questions.keys())
    random.shuffle(question_ids)
    shuffled_questions = {new_id: questions[old_id] for new_id, old_id in enumerate(question_ids, start=1)}
    return shuffled_questions

def attempt_quiz(selected_topic):
    questions = shuffle_questions(py_q[selected_topic])
    score = 0
    for q_id, question_data in questions.items():
        print(f"\nQ{q_id}: {question_data[0]}")
        for idx, option in enumerate(question_data[1:5], start=1):
            print(f"{idx}. {option}")
        answer = input("Select your answer (1-4): ")
        if int(answer) == question_data[5]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {question_data[5]}: {question_data[question_data[5]]}")
    print(f"\nYour total score: {score}/{len(questions)}")

def main():
    print("Select a topic for the quiz:")
    print("1. DSA")
    print("2. DBMS")
    print("3. Python")
    topics = ["DSA", "DBMS", "Python"]
    choice = int(input("Enter your choice (1-3): "))
    if choice in [1, 2, 3]:
        attempt_quiz(topics[choice - 1])
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
