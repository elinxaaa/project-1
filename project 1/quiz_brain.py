class QuizBrain:
    def __init__(self, qlist):
        self.number = 0
        self.list = qlist
        self.score = 0

    def next_question(self):
        current_q = self.list[self.number]
        self.number += 1
        user_ans = input(f"Q{self.number}: {current_q.text} (True/False) ")
        self.check_ans(user_ans, current_q.answer)

    def more_questions(self):
        if self.number == len(self.list):
            return False
        else:
            return True

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it!")
            self.score += 1
        else:
            print("Incorrect.")
        print(f"The correct answer is {correct_ans}.")
        print(f"Current Score: {self.score}/{self.number}")
