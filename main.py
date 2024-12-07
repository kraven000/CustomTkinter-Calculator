import customtkinter as ct


index = 0
error = False

def insert_text(events=None):
    '''It is the function which adds the number or mathematical operators in the Entry widget.'''
    
    global index
    
    if number_expression.get()=="ERROR!":
        entry.delete(0,ct.END)
    
    try:
        if events.char.isdigit() or events.char in {"+","-","*",r"/","."}:
            if len(number_expression.get())==0 and not error:
                index = 0
            else:
                index += 1
            
            entry.insert(index,events.char)
    except AttributeError:
        if events.isdigit() or events in {"+","-","*",r"/","."}:
            entry.insert(index,events)
    
    index += 1


def remove_text(events=None,remove_all=False):
    '''It is the function which remove the previous charater from entry widget if backspace key is pressed
    or clear all the charaters from the entry widget if 'CE' button is clicked.'''
    
    prev_text = number_expression.get()
    entry.delete(0,ct.END)
    if remove_all:
        ...
    else:
        entry.insert(0,prev_text[:-1])


def evaluate_expression(events=None):
    '''It is the function which evaluate all the expression in the entry widget if enter is pressed or
    '=' is clicked.'''
    
    global error
    try:
        result = str(eval(number_expression.get()))
        entry.delete(0,ct.END)
        
    except SyntaxError:
        entry.delete(0,ct.END)
        entry.insert(0,"ERROR!")
    else:
        entry.insert(0,result)


if __name__=="__main__":
    window = ct.CTk()

    window.geometry("377x382")
    window.title("Calculator")
    window.iconbitmap("icon.ico")
    window.resizable(False,False)

    number_expression = ct.StringVar()
    entry = ct.CTkEntry(window,textvariable=number_expression,width=377,height=120,font=("Roboto",40),
                                justify="right")
    entry.place(x=0,y=1)


    window.bind("<Key>",insert_text)
    window.bind("<BackSpace>",remove_text)
    window.bind("<Return>",evaluate_expression)


    button0 = ct.CTkButton(window,text="0",font=("Roboto",20),width=90,height=60,
                                    border_width=0,command=lambda:insert_text("0"))

    button1 = ct.CTkButton(window,text="1",font=("Roboto",16),width=90,height=60,
                                    border_width=0,command=lambda:insert_text("1"))

    button2 = ct.CTkButton(window,text="2",font=("Roboto",16),width=90,height=60,
                                    border_width=0,command=lambda:insert_text("2"))

    button3 = ct.CTkButton(window,text="3",font=("Roboto",16),width=90,height=60,
                                    border_width=0,command=lambda:insert_text("3"))

    button4 = ct.CTkButton(window,text="4",font=("Roboto",16),width=90,height=60,
                                    border_width=0,command=lambda:insert_text("4"))

    button5 = ct.CTkButton(window,text="5",font=("Roboto",16),width=90,height=60,
                                    border_width=0,command=lambda:insert_text("5"))

    button6 = ct.CTkButton(window,text="6",font=("Roboto",16),width=90,height=60,
                                    border_width=0,command=lambda:insert_text("6"))

    button7 = ct.CTkButton(window,text="7",font=("Roboto",16),width=90,height=60,
                                    border_width=0,command=lambda:insert_text("7"))

    button8 = ct.CTkButton(window,text="8",font=("Roboto",16),width=90,height=60,
                                    border_width=0,command=lambda:insert_text("8"))

    button9 = ct.CTkButton(window,text="9",font=("Roboto",16),width=90,height=60,
                                    border_width=0,command=lambda:insert_text("9"))


    button_addition = ct.CTkButton(window,text="+",font=("Roboto",16),width=90,height=60,
                                        border_width=0,command=lambda:insert_text("+"))

    button_subtraction = ct.CTkButton(window,text="-",font=("Roboto",16),width=90,height=60,
                                        border_width=0,command=lambda:insert_text("-"))

    button_multiplication = ct.CTkButton(window,text="*",font=("Roboto",16),width=90,height=60,
                                        border_width=0,command=lambda:insert_text("*"))

    button_division = ct.CTkButton(window,text=r"/",font=("Roboto",16),width=90,height=60,
                                        border_width=0,command=lambda:insert_text(r"/"))


    button_equal = ct.CTkButton(window,text="=",font=("Roboto",16),width=90,height=60,
                                        border_width=0,command=lambda:evaluate_expression())

    button_backspace = ct.CTkButton(window,text="CE",font=("Roboto",16),width=90,height=60,
                                        border_width=0,command=lambda:remove_text(remove_all=True))


    button0.place(x=0,y=125)
    button1.place(x=95,y=125)
    button2.place(x=190,y=125)
    button3.place(x=0,y=190)
    button4.place(x=95,y=190)
    button5.place(x=190,y=190)
    button6.place(x=0,y=255)
    button7.place(x=95,y=255)
    button8.place(x=190,y=255)
    button9.place(x=0,y=320)

    button_addition.place(x=285,y=125)
    button_subtraction.place(x=285,y=190)
    button_multiplication.place(x=285,y=255)
    button_division.place(x=285,y=320)

    button_equal.place(x=95,y=320)
    button_backspace.place(x=190,y=320)


    window.mainloop()