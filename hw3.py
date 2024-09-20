# Your name: 
# Your student id:
# Your email:
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code
# asked chatgpt how to capture output and enter input in a test

import random
import operator
from unittest.mock import patch
import unittest


# create a Digital Book of Answers
class DigitalBookofAnswers():

    # create the constructor (__init__) method 
    # ARGUMENTS: 
    #       self: the current object
    #       answers: a list of potential answers
    # RETURNS: None
    def __init__(self, answers):
        self.book_answer_list = answers
        self.questions_asked_list = []
        self.answered_list = []

    # Create the __str__ method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: a string
    def __str__(self):
        res = ''
        for index, val in enumerate(self.book_answer_list):
            if index == len(self.book_answer_list) - 1:
                res += val
                break
            res += val
            res += " - "
        return res

    # Creates the check_get_answer method
    # ARGUMENTS:
    #       self: the current object
    #       question: the question the user wants to ask the digital book of answers
    # RETURNS: a string
    def check_get_answer(self, question):
        if question in self.questions_asked_list:
            index = self.questions_asked_list.index(question)
            index_of_question = self.answered_list[index]
            return f"I've already answered this question. The answer is: {self.book_answer_list[index_of_question]}"
        else:
            rand_index = random.randint(0, len(self.book_answer_list) - 1)
            self.answered_list.append(rand_index)
            self.questions_asked_list.append(question)
            return f"{self.book_answer_list[rand_index]}"

    # Creates open_book method
    # ARGUMENTS:
    #   self: the current object
    # RETURNS: None
    def open_book(self):
        while True:
            if len(self.questions_asked_list) == 0:
                question = input("Turn 1 - Please enter your question: ")
            else:
                question = input(f"Turn {len(self.questions_asked_list) + 1} - Please enter your question: ")
            if question == "Done":
                print("Goodbye! See you soon.")
                break
            else:
                answer = self.check_get_answer(question)
                print(answer)
        pass


    # Create the answer_log method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: a list
    def answer_log(self):
        if len(self.answered_list) == 0:
            print("Empty")
            return []
        # res is a list of tuples where the first val is the freq of the answer and the second is the string
        tuple_list = []
        # in answer count the index is index of the answer in answer list and the value is its frequency
        answer_count = [0] * len(self.book_answer_list)
        for answer_index in self.answered_list:
            answer_count[answer_index] += 1

        for i in range(0, len(answer_count)):
            tuple_list.append((answer_count[i], (f"{answer_count[i]} - {(self.book_answer_list[i]).lower()}")))
        sorted_res = sorted(tuple_list, key=operator.itemgetter(0), reverse=True)

        res = []
        for item in sorted_res:
            res.append(item[1])

        return res


def test():
    answers_list = ['Believe in Yourself', 'Stay Open to the Future', 'Enjoy It']
    book = DigitalBookofAnswers(answers_list)

    print("Test __init__:")
    print(f"Answer History List: Expected: {[]}, Actual: {book.answered_list}")
    print(f"Question History List: Expected: {[]}, Actual: {book.questions_asked_list}")
    print(" ")

    print("Test __str__:")
    expected = "Belive in Yourself - Stay Open to the Future - Enjoy It"
    print(f"Expected: {expected}, Actual: {str(book)}")
    print(" ")
    
    empty_book = DigitalBookofAnswers([])
    print("Test __str__: when it's an empty book without possible answers")
    expected = ""
    print(f"Expected: {expected}, Actual: {str(empty_book)}")
    print(" ")

    print("Testing return value of check_get_answer:")
    res = book.check_get_answer('test question')
    print(f"Expected: {str}, Actual: {type(res)}")
    print(" ")


    print("Testing check_get_answer")
    book.book_answer_list = ['Go For It']
    print(book.questions_asked_list)
    res = book.check_get_answer('test question 2')
    print(f"Expected: {'Go For It'}, Actual: {res}")
    print(" ")

    print("Testing that check_get_answer adds answer index to answered_list:")
    # ↓ newly added - reset the questions_asked_list
    book.questions_asked_list = []
    ##############################
    book.book_answer_list = ['Go For It']
    book.answered_list = []
    book.check_get_answer('test question 2')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing that check_get_answer does not add 'I've already answered this question' part to answered_list:")
    book.book_answer_list = ['Believe In Yourself']
    book.answered_list = [0]
    book.questions_asked_list = ['test question 3']
    book.check_get_answer('test question 3')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")


    print("Testing return value answer_log")
    book.book_answer_list = ['Follow Your Inner Voice', 'Stay Positive', 'Go For It']
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log())
    print(f"Expected: {list}, Actual: {res}")
    print(" ")

    print("Testing return value answer_log elements")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log()[0])
    print(f"Expected: {str}, Actual: {res}")
    print(" ")

    print("Testing answer_log")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = book.answer_log()
    expected = ['3 - follow your inner voice', '2 - stay positive', '1 - go for it']
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing empty answer_log")
    book.answered_list = []
    res = book.answer_log()
    expected = []
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")



class TestPrintOutput(unittest.TestCase):
    # Extra Credit
    def my_test():
        # Put your test code here
        with patch('builtins.input', return_value='Done'):
            book_answer_list = ["Try again.", "Self-Reflect"]
            test = DigitalBookofAnswers(book_answer_list)



def main():
    book_answer_list = ["Try again.", "Self-Reflect"]
    sample = DigitalBookofAnswers(book_answer_list)
    sample.open_book()
    sample.answer_log()



# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test() 
    # my_test() #TODO: Uncomment if you do the extra credit
    

