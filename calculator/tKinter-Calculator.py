from tkinter import Tk, Button, Label, Entry
import tkinter as tk

wn = Tk()
wn.title("Calculator")
wn.resizable(0, 0)
label = Label(wn, text="created by Hujaakbar", fg="red", bg="black", width=26)
label.grid(row=7, columnspan=4)

entry = Entry(wn, width=26, bg="black", fg="white", borderwidth=4)
entry.grid(row=0, column=0, columnspan=4, pady=10, ipady=9)


def display_num(x):
    global rt
    if x in range(0, 10):
        h = entry.get()
        entry.delete(0, tk.END)
        rt = h + str(x)
        entry.insert(0, rt)


def display_multiply_sign(s):
    global r
    global bt
    r = entry.get()
    if "=" not in r:
        h = entry.get()
        entry.delete(0, tk.END)
        bt = h + "*"
        entry.insert(0, bt)
    else:
        h = entry.get()
        b = h.find("=")
        h = h.replace(h[0 : b + 1], "")
        entry.delete(0, tk.END)
        bt = h + "*"
        entry.insert(0, bt)

    global g
    g = "*"

    return s


def display_divide_sign(s):
    global r
    r = entry.get()
    if "=" not in r:
        h = entry.get()
        entry.delete(0, tk.END)
        bt = h + "/"
        entry.insert(0, bt)
    else:
        h = entry.get()
        b = h.find("=")
        h = h.replace(h[0 : b + 1], "")
        entry.delete(0, tk.END)
        bt = h + "/"
        entry.insert(0, bt)

    global g
    g = "/"
    return s


def display_subtract_sign(s):
    global r
    r = entry.get()
    if "=" not in r:
        h = entry.get()
        entry.delete(0, tk.END)
        bt = h + "-"
        entry.insert(0, bt)
    else:
        h = entry.get()
        b = h.find("=")
        h = h.replace(h[0 : b + 1], "")
        entry.delete(0, tk.END)
        bt = h + "-"
        entry.insert(0, bt)
    global g
    g = "-"
    return s


def display_factorial_sign(s):
    global r
    r = entry.get()

    if "=" not in r:
        h = entry.get()
        entry.delete(0, tk.END)
        bt = h + "!"
        entry.insert(0, bt)
    else:
        h = entry.get()
        b = h.find("=")
        h = h.replace(h[0 : b + 1], "")
        entry.delete(0, tk.END)
        bt = h + "!"
        entry.insert(0, bt)

    global g
    g = "!"
    return s


def display_sqrt_sign(s):
    global r
    r = entry.get()

    if "=" not in r:
        h = entry.get()
        entry.delete(0, tk.END)
        bt = h + "sqrt"
        entry.insert(0, bt)
    else:
        h = entry.get()
        b = h.find("=")
        h = h.replace(h[0 : b + 1], "")
        entry.delete(0, tk.END)
        bt = h + "sqrt"
        entry.insert(0, bt)

    global g
    g = "1/x"
    return s


def display_sq_sign(s):
    global r
    r = entry.get()
    if "=" not in r:
        h = entry.get()
        entry.delete(0, tk.END)
        bt = h + "**"
        entry.insert(0, bt)
    else:
        h = entry.get()
        b = h.find("=")
        h = h.replace(h[0 : b + 1], "")
        entry.delete(0, tk.END)
        bt = h + "**"
        entry.insert(0, bt)

    global g
    g = "x2"
    return s


def clear_entry():
    entry.delete(0, tk.END)
    return


def display_plus_sign(s):
    global r
    global bt
    r = entry.get()
    if "=" not in r:
        h = entry.get()
        entry.delete(0, tk.END)
        bt = h + "+"
        entry.insert(0, bt)
    else:
        h = entry.get()
        b = h.find("=")
        h = h.replace(h[0 : b + 1], "")
        entry.delete(0, tk.END)
        bt = h + "+"
        entry.insert(0, bt)
    global g
    g = "+"

    return "+"


def evaluate():
    if g == "+":
        we = entry.get()
        k = we.split("+")
        fr = float(k[0])
        sn = float(k[1])
        y = fr + sn
        y = str(y)
        if y[-2] + y[-1] == ".0":
            y = y.replace(".0", "")

        entry.delete(0, tk.END)
        gt = we + "=" + str(y)

        entry.insert(0, gt)
    if g == "*":
        we = entry.get()
        k = we.split("*")
        fr = float(k[0])
        sn = float(k[1])
        y = fr * sn
        y = str(y)

        if y[-2] + y[-1] == ".0":
            y = y.replace(".0", "")

        entry.delete(0, tk.END)
        gt = we + "=" + str(y)

        entry.insert(0, gt)

    if g == "x2":
        sa = str(entry.get())
        ba = sa.replace("**", "")
        y = float(ba) ** 2
        y = str(y)
        if y[-2] + y[-1] == ".0":
            y = y.replace(".0", "")
        entry.delete(0, tk.END)
        a = str(sa) + "=" + str(y)

        entry.insert(0, a)
    if g == "/":
        ed = entry.get()
        k = ed.split("/")
        fr = float(k[0])
        sn = float(k[1])
        y = fr / sn
        y = str(y)
        if y[-2] + y[-1] == ".0":
            y = y.replace(".0", "")
        entry.delete(0, tk.END)
        gt = ed + "=" + str(y)

        entry.insert(0, gt)
    if g == "!":
        it = entry.get()
        ti = it.replace("!", "")
        y = int(ti) + 1

        ll = 1
        for i in range(1, y):
            ll = ll * i

        bbb = it + "=" + str(ll)

        entry.delete(0, tk.END)

        entry.insert(0, bbb)
    if g == "1/x":
        ed = entry.get()
        k = ed.replace("sqr", "")
        entry.delete(0, tk.END)
        y = float(k) ** 0.5
        y = str(y)
        if y[-2] + y[-1] == ".0":
            y = y.replace(".0", "")
        gt = ed + "=" + str(y)
        entry.insert(0, gt)

    if g == "-":
        ed = entry.get()
        k = ed.split("-")
        fr = float(k[0])
        sn = float(k[1])
        y = fr - sn
        y = str(y)
        if y[-2] + y[-1] == ".0":
            y = y.replace(".0", "")
        entry.delete(0, tk.END)
        gt = ed + "=" + str(y)
        entry.insert(0, gt)


def display_dot(x):
    if (
        "-" not in entry.get()
        and "*" not in entry.get()
        and "/" not in entry.get()
        and "+" not in entry.get()
    ):
        if x not in entry.get():
            h = entry.get()
            entry.delete(0, tk.END)
            rt = h + str(x)
            entry.insert(0, rt)
        print(entry.get())
    elif (
        "-" in entry.get()
        or "*" in entry.get()
        or "/" in entry.get()
        or "+" in entry.get()
    ):
        aa = entry.get()
        bb = aa.count(".")
        if bb == 1:
            h = entry.get()
            entry.delete(0, tk.END)
            rt = h + str(x)
            entry.insert(0, rt)


btn_7 = Button(
    wn,
    text="7",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_num(7),
)
btn_7.grid(row=1, column=0)
btn_8 = Button(
    wn,
    text="8",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_num(8),
)
btn_8.grid(row=1, column=1)
btn_9 = Button(
    wn,
    text="9",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_num(9),
)
btn_9.grid(row=1, column=2)
btn_c = Button(
    wn,
    text="C",
    fg="white",
    bg="black",
    padx=13,
    pady=10,
    command=lambda: clear_entry(),
)
btn_c.grid(row=1, column=3)
btn_4 = Button(
    wn,
    text="4",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_num(4),
)
btn_4.grid(row=2, column=0)
btn_5 = Button(
    wn,
    text="5",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_num(5),
)
btn_5.grid(row=2, column=1)
btn_6 = Button(
    wn,
    text="6",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_num(6),
)
btn_6.grid(row=2, column=2)
btn_m = Button(
    wn,
    text="*",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_multiply_sign("*"),
)
btn_m.grid(row=2, column=3)
btn_1 = Button(
    wn,
    text="1",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_num(1),
)
btn_1.grid(row=3, column=0)
btn_2 = Button(
    wn,
    text="2",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_num(2),
)
btn_2.grid(row=3, column=1)
btn_3 = Button(
    wn,
    text="3",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_num(3),
)
btn_3.grid(row=3, column=2)
btn_d = Button(
    wn,
    text="/",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_divide_sign("/"),
)
btn_d.grid(row=3, column=3)
btn_s = Button(
    wn,
    text="--",
    fg="white",
    bg="black",
    padx=13,
    pady=10,
    command=lambda: display_subtract_sign("-"),
)
btn_s.grid(row=4, column=2)
btn_0 = Button(
    wn,
    text="0",
    fg="white",
    bg="black",
    padx=15,
    pady=10,
    command=lambda: display_num(0),
)
btn_0.grid(row=4, column=1)
btn_p = Button(
    wn,
    text="+",
    fg="white",
    bg="black",
    padx=14,
    pady=10,
    command=lambda: display_plus_sign("+"),
)
btn_p.grid(row=4, column=3)
btn_e = Button(
    wn, text="=", fg="white", bg="black", padx=14, pady=10, command=lambda: evaluate()
)
btn_e.grid(row=5, column=3)
btn_sqrt = Button(
    wn,
    text="sqrt",
    fg="white",
    bg="black",
    padx=7,
    pady=10,
    command=lambda: display_sqrt_sign("1/x"),
)
btn_sqrt.grid(row=5, column=0)
btn_sq = Button(
    wn,
    text="x2",
    fg="white",
    bg="black",
    padx=12,
    pady=10,
    command=lambda: display_sq_sign("x2"),
)
btn_sq.grid(row=5, column=1)
btn_f = Button(
    wn,
    text="!",
    fg="white",
    bg="black",
    padx=16,
    pady=10,
    command=lambda: display_factorial_sign("!"),
)
btn_f.grid(row=5, column=2)
btn_t = Button(
    wn,
    text=".",
    fg="white",
    bg="black",
    padx=17,
    pady=10,
    command=lambda: display_dot("."),
)
btn_t.grid(row=4, column=0)
wn.mainloop()
