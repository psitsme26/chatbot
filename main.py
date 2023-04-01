from tkinter import *
from retriever import get_relevant_docs
from qna import get_answer
import time


def botReply():
    claim_number = claim_field.get()
    claim_number = claim_number.upper()
    context = get_relevant_docs(claim_number)

    if not context == 'No information found for claim number.':
        question = question_field.get()
        question = question.capitalize()
        if question.__contains__('Bye'):
            text_area.insert(END, 'Bot: Bye have a nice day!' + '\n\n')

        else:
            answer = get_answer(question, context)
            text_area.insert(END, 'You: '+question+'\n\n')
            text_area.insert(END, 'Bot: '+str(answer)+'\n\n')
            question_field.delete(0, END)
    else:
        text_area.insert(END, 'Bot: ' + str(context) + '\n\n')

root = Tk()
root.geometry('500x570+100+30')
root.title('SunGPT')
root.config(bg='cyan')

logo_pic = PhotoImage(file='pic.png')

logo_pic_lable = Label(root, image=logo_pic, bg='cyan')
logo_pic_lable.pack(pady=10)

centre_frame = Frame(root)
centre_frame.pack()

scrollbar = Scrollbar(centre_frame)
scrollbar.pack(side=RIGHT)

text_area = Text(centre_frame,
                 font=('times new roman', '20', 'bold'),
                 height=10,
                 yscrollcommand=scrollbar.set,
                 wrap='word')
text_area.pack(side=LEFT)

text_area.insert(INSERT, 'Bot: ' + str('Hi This is JiVA,'
                                        ' Please let me know the claim number'
                                        'for which you have questions.') + '\n\n')
scrollbar.config(command=text_area.yview())

claim_field = Entry(root, font=('verdana', '20', 'bold'))
claim_field.pack(pady=15, fill=X)
question_field = Entry(root, font=('verdana', '20', 'bold'))
question_field.pack(pady=15, fill=X)

send_pic = PhotoImage(file='send.png')


button = Button(root, image=send_pic, command=botReply)
button.pack(pady=10)


def click(event):
    button.invoke()


root.bind('<Return>', click)

root.mainloop()
