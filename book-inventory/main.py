from tkinter import *
import backend

import contextlib

window = Tk()

window.title("Book Store")

label_title = Label(window, text="Title")
label_title.grid(row=0, column=0)


label_author = Label(window, text="Author")
label_author.grid(row=0, column=2)


label_year = Label(window, text="Year")
label_year.grid(row=1, column=0)


label_isbn = Label(window, text="ISBN")
label_isbn.grid(row=1, column=2)


title_variable = StringVar()
entry_title = Entry(window, textvariable=title_variable)
entry_title.grid(row=0, column=1)

author_variable = StringVar()
entry_author = Entry(window, textvariable=author_variable)
entry_author.grid(row=0, column=3)

year_variable = StringVar()
entry_year = Entry(window, textvariable=year_variable)
entry_year.grid(row=1, column=1)

isbn_variable = StringVar()
entry_isbn = Entry(window, textvariable=isbn_variable)
entry_isbn.grid(row=1, column=3)

box_list = Listbox(window, height=6, width=35)
box_list.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

box_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=box_list.yview)


def get_selected_row(event):
    with contextlib.suppress(IndexError):
        global selected_tuple
        index = box_list.curselection()[0]
        selected_tuple = box_list.get(index)
        entry_title.delete(0, END)
        entry_title.insert(END, selected_tuple[1])
        entry_author.delete(0, END)
        entry_author.insert(END, selected_tuple[2])
        entry_year.delete(0, END)
        entry_year.insert(END, selected_tuple[3])
        entry_isbn.delete(0, END)
        entry_isbn.insert(END, selected_tuple[4])


box_list.bind("<<ListboxSelect>>", get_selected_row)


def view_command():
    box_list.delete(0, END)
    for row in backend.view():
        box_list.insert(END, row)


def view_search():
    box_list.delete(0, END)
    for row in backend.search(
        title_variable.get(),
        author_variable.get(),
        year_variable.get(),
        isbn_variable.get(),
    ):
        box_list.insert(END, row)


def insert_command():
    backend.insert(
        title_variable.get(),
        author_variable.get(),
        year_variable.get(),
        isbn_variable.get(),
    )
    view_command()


def delete_book():
    backend.delete(selected_tutpe[0])
    view_command()


def update_book():
    backend.update(
        selected_tutpe[0],
        title_variable.get(),
        author_variable.get(),
        year_variable.get(),
        isbn_variable.get(),
    )
    view_command()


b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)
b2 = Button(window, text="Search Entry", width=12, command=view_search)
b2.grid(row=3, column=3)
b3 = Button(window, text="Add Entry", width=12, command=insert_command)
b3.grid(row=4, column=3)
b4 = Button(window, text="Update Selected", width=12, command=update_book)
b4.grid(row=5, column=3)
b5 = Button(window, text="Delete Selected", width=12, command=delete_book)
b5.grid(row=6, column=3)
b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
