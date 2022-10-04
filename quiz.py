import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []
    
    def __init__(self):
        question_types = (Add, Multiply)
        # generate 10 random questions with numbers from 1 to 10
        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1,num2)
            self.questions.append(question)
        # add these questions into self.questions
        
    def take_quiz(self):
        self.start_time = datetime.datetime.now()
        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()
        return self.summary()
        # log the start time
        # ask all of the questions
        # log if they got the question right
        # log the end time
        # show a summary
        
    def ask(self, question):
        
        # log the start time
        # capture the answer
        # check the answer
        # log the end time
        # if the answer's right, send back True
        # otherwise, send back False
        # send back the elapsed time, too
        correct = False
        question_start =  datetime.datetime.now()
        answer = input(question.text + " = ")
        if answer == str(question.answer):
            correct = True
        question_end = datetime.datetime.now()
        return correct, question_end - question_start
            
    def total_correct(self):
        total = 0
        for answer in self.answers:
            if answer [0]:
                total += 1
        return total        
        
    def summary(self):
        # print how many you got right and the total # of questions. 5/10
        print ("you got {} out of {} right".format(
                self.total_correct(),len(self.questions)))
        # print the total time for the quiz: 30 seconds!
        print("it took you {} seconds total.".format((self.end_time - self.start_time).seconds))
              
Quiz().take_quiz()
             