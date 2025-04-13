from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiz")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)

        self.canvas=Canvas(highlightthickness=0,width=300,height=250)
        self.question_text=self.canvas.create_text(150,125,
                                                   fill=THEME_COLOR,
                                                   font=("Arial",20,"italic"),width=280)
        self.canvas.config(background="white")
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

        right_image=PhotoImage(file="images/true.png")
        self.right_button=Button(image=right_image,highlightthickness=0,command=self.true_pressed)
        wrong_image=PhotoImage(file="images/false.png")
        self.wrong_button=Button(image=wrong_image,highlightthickness=0,command=self.false_pressed)
        self.right_button.grid(column=0,row=2)
        self.wrong_button.grid(column=1,row=2)

        self.score_label=Label(text="Score: 0",fg="white",bg=THEME_COLOR,font=("Arial",15,"bold"))
        self.score_label.grid(column=1,row=0,pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000,self.get_next_question)
