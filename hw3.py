import random

class DigitalBookofAnswers:

    def __init__(self, answers):
        self.book_answers_list = answers
        self.questions_asked = []
        self.answered_list = []

    def __str__(self):
        res = ''
        for val in self.book_answers_list:
            res += val
            res += "-"
        return res
    
    def check_get_answer(self, question):
        if question in self.questions_asked:
            index = self.questions_asked.index(question)
            return f"I've already answered this question. The answer is: {self.book_answers_list[index]}"
        else:
            rand_index = random.randint(0, len(self.book_answers_list))
            self.answered_list.append(rand_index)
            self.questions_asked.append(question)
            return f"{self.book_answers_list[rand_index]}"

    def open_book(self):
        while True:
            if len(self.questions_asked) == 0:
                question = input("Turn 1 - Please enter your question: ")
            else:
                question = input(f"Turn {len(self.questions_asked) + 1} - Please enter your question: ")
            if question == "Done":
                print("Goodbye! See you soon.")
                break
            else:
                answer = self.check_get_answer(question)
                print(answer)

    def answer_log(self):
        

