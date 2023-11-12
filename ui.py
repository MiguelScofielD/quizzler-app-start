from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50,pady=50,bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg= "white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text=" Questions ",
            font=("Arial",20,"italic"))
        self.canvas.grid(column=0, row=1,columnspan = 2,padx= 20, pady = 20)
        #Score
        self.score_label = Label(text=f"Score: 0", fg= "white",bg= THEME_COLOR,font=("Arial",15,"bold"))
        self.score_label.grid(column=1, row=0)
        #button right
        self.image_true = PhotoImage(file="images/true.png")
        self.button_right = Button(image=self.image_true,command=self.get_check_answer, highlightthickness=0)
        self.button_right.grid(column=0, row=2)
        # button wrong
        self.image_false = PhotoImage(file="images/false.png")
        self.button_wrong = Button(image=self.image_false,command=self.get_check_answer_wrong, highlightthickness=0)
        self.button_wrong.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(
                text=f"Score: {self.quiz.score}",
                fg="white", bg=THEME_COLOR,
                font=("Arial", 15, "bold"))
            self.canvas.itemconfig(self.question_text,text= q_text)
        else:
            self.canvas.itemconfig(self.question_text,text= "Não há mais questões para responder!!!")
            self.button_wrong.config(state="disabled")
            self.button_right.config(state="disabled")

    def get_check_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

        # self.score_label.config(
        #     text=f"Score: {self.quiz.score}",
        #     fg= "white",
        #     bg= THEME_COLOR,
        #     font=("Arial",15,"bold"))

    def get_check_answer_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)



    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)
