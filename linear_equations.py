from tkinter import *
from tkinter import messagebox
import numpy as np

window = Tk()
window.geometry("500x500")
window.title("Linear Equation Solver")
window.config(bg="light blue")
window.resizable(True, True)

main_label = Label(window, text="Welcome".upper(), font=('arial', 20, 'bold'), background="light blue",
                   foreground='maroon')
main_label.place(x=170, y=10)

equations_label = Label(window, text="Enter number of equations ", font=('arial', 12, 'bold'))
equations_label.place(x=50, y=80)
equations_entry = Entry(window, font=('calibri', 12), width=10)
equations_entry.place(x=280, y=80)

unknowns_label = Label(window, text="Enter number of Unknowns ", font=('arial', 12, 'bold'))
unknowns_label.place(x=50, y=110)
unknowns_entry = Entry(window, font=('calibri', 12), width=10)
unknowns_entry.place(x=280, y=110)


def result():
    no_equations = equations_entry.get()
    no_unknowns = unknowns_entry.get()
    no_unknowns, no_equations = int(no_unknowns), int(no_equations)

    if (int(no_unknowns) > int(no_equations)):
        messagebox.showerror("showerror", "Invalid Entries")
    else:
        newWindow = Toplevel(window)
        newWindow.title("Solver")
        newWindow.geometry("600x600")
        newWindow.config(bg="light pink")
        newWindow.resizable(True, True)

        title_label = Label(newWindow,
                            text="Enter the data- x(i),constants under X,C\n Enter the variables such that its matrix is not singular",
                            font=('arial', 12, 'bold'))
        title_label.pack()

        x_s, x_point, y_point = 1, 20, 50
        while (x_s <= no_unknowns):
            x_label = Label(newWindow, text="X{}".format(x_s), width=4, font=('arial', 12, 'bold'))
            x_label.place(x=x_point, y=y_point)
            x_s += 1
            x_point += 60
        const_label = Label(newWindow, text="C", width=4, font=('arial', 12, 'bold'))
        const_label.place(x=x_point, y=y_point)

        arr = np.zeros((no_equations, no_unknowns + 1), dtype=int)
        end = np.zeros((no_equations, 1))

        entries = [[0 for i in range(no_unknowns + 1)] for j in range(no_equations)]

        x_point, y_point = 20, y_point + 40

        for i in range(no_equations):
            for j in range(no_unknowns + 1):
                entries[i][j] = Entry(newWindow, font=('calibri'), width=4)
                entries[i][j].place(x=x_point, y=y_point)
                x_point += 60
            x_point = 20
            y_point += 30

        Output_1 = Text(newWindow, height=5, width=25, bg="light cyan", font=('arial', 18, 'bold'))

        def get_values():
            for i in range(no_equations):
                for j in range(no_unknowns + 1):
                    arr[i][j] = round(float(entries[i][j].get()), 2)
            print(arr)
            Output_1.insert(END, arr)

        x_point += 10
        y_point += 10
        btn_submit = Button(newWindow, text="Show Value Matrix", font=('arial', 12, 'bold'), command=get_values,
                            width=40)
        btn_submit.place(x=x_point, y=y_point)

        y_point += 50
        Output_1.place(x=x_point, y=y_point)

        Output_2 = Text(newWindow, height=5, width=25, bg="light cyan", font=('arial', 18, 'bold'))

        def get_answer_array():
            a = arr[:no_unknowns, :no_unknowns]
            b = []
            aug = np.take(arr, [no_unknowns], axis=1)
            for ele in aug:
                for pin in ele:
                    b.append(pin)
            b = b[:no_unknowns]
            try:
                res = np.linalg.solve(a, b)
                for ele in res:
                    ele = round(ele, 3)
                msg = res
                Output_2.insert(END, msg)
            except:
                msg = "Error in the data\n"
                Output_2.insert(END, msg)
            print(msg)
            # return msg

        y_point += 150
        btn_reform = Button(newWindow, text="Show End Result", font=('arial', 12, 'bold'),
                            command=get_answer_array,
                            width=40)
        btn_reform.place(x=x_point, y=y_point)

        y_point += 50
        Output_2.place(x=x_point, y=y_point)


btn = Button(window, text="Show Results", font=('arial', 12, 'bold'), command=result, width=40)
btn.place(x=50, y=150)

window.mainloop()
