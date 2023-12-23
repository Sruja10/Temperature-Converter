import tkinter as tk

options = [
    'Degree Celsius',
    'Fahrenheit',
    'Kelvin'
]


def convert():

    to_unit_ent.delete(0, tk.END)

    from_unit = from_unit_opt.get()
    to_unit = to_unit_opt.get()

    from_unit_var = float(from_unit_ent.get())


    if from_unit == 'Degree Celsius' and to_unit == 'Fahrenheit':
        to_unit_var = round((from_unit_var * 9/5) + 32, 2)
        to_unit_ent.insert(0, str(to_unit_var))

    elif from_unit == 'Degree Celsius' and to_unit == 'Kelvin':
        to_unit_var = round(from_unit_var + 273.15, 2)
        to_unit_ent.insert(0, str(to_unit_var))

    elif from_unit == 'Fahrenheit' and to_unit == 'Degree Celsius':
        to_unit_var = round((from_unit_var - 32) * 5/9, 2)
        to_unit_ent.insert(0, str(to_unit_var))

    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        to_unit_var = round((from_unit_var + 459.67) * 5/9, 2)
        to_unit_ent.insert(0, str(to_unit_var))

    elif from_unit == 'Kelvin' and to_unit == 'Degree Celsius':
        to_unit_var = round((from_unit_var - 273.15), 2)
        to_unit_ent.insert(0, str(to_unit_var))

    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        to_unit_var = round((from_unit_var * 9/5) - 459.67, 2)
        to_unit_ent.insert(0, str(to_unit_var))

    else:
        to_unit_ent.insert(0, str(from_unit_var))


window = tk.Tk()
window.title('Temperature Converter')

main_frm = tk.Frame(master=window)
main_frm.pack()


from_unit_lbl = tk.Label(master=main_frm, text='Value to convert')
from_unit_lbl.grid(row=0, column=0)

from_unit_ent = tk.Entry(master=main_frm)
from_unit_ent.grid(row=1, column=0, sticky='nsew', padx=5, pady=3, ipadx=5)

from_unit_opt = tk.StringVar()
from_unit_opt.set('Degree Celsius')

from_unit_dropdown = tk.OptionMenu(main_frm, from_unit_opt, *options)
from_unit_dropdown.grid(row=2, column=0, padx=5, pady=3, sticky='w')


lbl_text = tk.Label(master=main_frm, text='=')
lbl_text.grid(row=1, column=1)


to_unit_lbl = tk.Label(master=main_frm, text='Result')
to_unit_lbl.config(anchor='w')
to_unit_lbl.grid(row=0, column=2)

to_unit_ent = tk.Entry(master=main_frm)
to_unit_ent.grid(row=1, column=2, sticky='nsew', padx=5, pady=3, ipadx=5)


to_unit_opt = tk.StringVar()
to_unit_opt.set('Fahrenheit')

to_unit_dropdown = tk.OptionMenu(main_frm, to_unit_opt, *options)
to_unit_dropdown.config(width=15, anchor='w')
to_unit_dropdown.grid(row=2, column=2, padx=5, pady=3, sticky='w')

button = tk.Button(master=main_frm, text='Convert', command=convert, relief=tk.RAISED)
button.grid(row=3, column=1, padx=5, pady=3, ipadx=5)

window.mainloop()

