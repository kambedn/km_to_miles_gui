from tkinter import *
FONT = ("Arial", 14, 'normal')


def button_action():  # is called when the user clicks the button
    km = round(float(inp.get()) * 0.621, 3)
    result_l.config(text=str(km))


# Creating a window
window = Tk()
window.title("Km to mile converter")

# Adding padding to the window
window.config(padx=50, pady=30)

# "is equal to" label
is_equal_to_l = Label(text="is equal to", padx=10, pady=5, font=FONT)
is_equal_to_l.grid(column=0, row=1)

# input
inp = Entry(width=12, font=FONT)
inp.grid(column=1, row=0)

# "Km" label
km_l = Label(text="Km", padx=10, pady=5, font=FONT)
km_l.grid(column=2, row=0)

# result label
result_l = Label(text="0", padx=10, pady=5, font=FONT)
result_l.grid(column=1, row=1)

# 'Miles' label
miles_l = Label(text="Miles", padx=10, pady=5, font=FONT)
miles_l.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_action, font=FONT)
button.grid(column=1, row=2)


window.mainloop()
