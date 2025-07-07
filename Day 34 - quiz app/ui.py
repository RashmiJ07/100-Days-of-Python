THEME_COLOR = "#375362"
FONT = ('Arial',20,'italic')

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface():
    def __init__(self,quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("pyQuizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.quiz = quiz_brain

        self.score_label = Label(text="Score: 0",bg=THEME_COLOR,fg='White',font=('Arial',10,'normal'))
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg='White')
        self.question_text = self.canvas.create_text(
            150
            ,125
            ,text=f'text goes here'
            ,font=FONT
            ,fill=THEME_COLOR
            ,width=280
            )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        right_image = PhotoImage(file="Day 34\\images\\true.png")
        self.right_button = Button(image=right_image,highlightthickness=0,command=self.true_button_press)
        self.right_button.grid(row=2,column=0)

        wrong_image = PhotoImage(file="Day 34\\images\\false.png")
        self.wrong_button = Button(image=wrong_image,highlightthickness=0,command=self.false_button_press)
        self.wrong_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(\
                self.question_text
                ,text=f"You've reached the end of the quiz. Your final score is {self.quiz.score}/10."
                ,font=('Ariel',20,'bold'))
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_button_press(self):
        # is_right = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_press(self):
        is_false = self.quiz.check_answer("False")
        self.give_feedback(is_false)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000,self.get_next_question)
