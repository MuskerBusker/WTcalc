import tkinter as tk
import datetime
import os

def divide_by_45(event=None):
    num = int(entry.get())
    ge_result = num / 45
    czk_result = ge_result * 0.14 + 1
    eur_result = czk_result * 0.0425
    usd_result = czk_result * 0.0464

    # Write to log file
    log_entry = str(datetime.datetime.now()) + " - Original number: " + str(num) + ", GE Result: " + str(ge_result) + ", CZK Result: " + str(czk_result) + ", EUR Result: " + str(eur_result) + ", USD Result: " + str(usd_result) + "\n"
    with open("GoldenEagleCountResult.txt", "a") as f:
        f.write(log_entry)

    # Update result labels
    ge_result_label.config(text="GE Result: " + str(ge_result))
    czk_result_label.config(text="CZK Result: " + str(czk_result))
    eur_result_label.config(text="EUR Result: " + str(eur_result))
    usd_result_label.config(text="USD Result: " + str(usd_result))

def clear_log():
    with open("GoldenEagleCountResult.txt", "w") as f:
        f.write("")
    ge_result_label.config(text="GE Result: ")
    czk_result_label.config(text="CZK Result: ")
    eur_result_label.config(text="EUR Result: ")
    usd_result_label.config(text="USD Result: ")

def view_log():
    os.startfile("GoldenEagleCountResult.txt")

def exit_program():
    root.destroy()

root = tk.Tk()
root.geometry("350x300")
root.title("Divide by 45")

entry = tk.Entry(root)
entry.pack()
entry.focus()

button = tk.Button(root, text="Calculate", command=divide_by_45)
button.pack()

clear_log_button = tk.Button(root, text="Clear Log", command=clear_log)
clear_log_button.pack()

view_log_button = tk.Button(root, text="View Log", command=view_log)
view_log_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack()

ge_result_label = tk.Label(root, text="GE Result: ")
ge_result_label.pack()

czk_result_label = tk.Label(root, text="CZK Result: ")
czk_result_label.pack()

eur_result_label = tk.Label(root, text="EUR Result: ")
eur_result_label.pack()

usd_result_label = tk.Label(root, text="USD Result: ")
usd_result_label.pack()

root.bind('<Return>', divide_by_45)
root.mainloop()
