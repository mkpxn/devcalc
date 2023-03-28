import tkinter as tk

class GUI:

    def __init__(self):

        # Root / Window
        self.root = tk.Tk()
        self.root.title('Dev Calculator')
        self.root.geometry('800x500')
        self.root.configure()

        # Frame 1: Pixel-to-REM calculator
        self.remcalc_frame = tk.Frame(self.root)
        self.remcalc_frame.columnconfigure(0, weight=1)
        self.remcalc_frame.columnconfigure(1, weight=1)
        self.remcalc_frame.columnconfigure(2, weight=1)
        self.remcalc_frame.columnconfigure(3, weight=1)
        self.remcalc_frame.columnconfigure(4, weight=1)

        # Frame 1: Section Label
        self.remcalc_label = tk.Label(
            self.remcalc_frame, 
            text="Rem Calculator", 
            font=('Arial', 18),
        )
        self.remcalc_label.grid(row=0, column=0, columnspan=5, pady=(0, 20))

        # Frame 1: Label for px input
        self.remcalc_px_label = tk.Label(
            self.remcalc_frame,
            text="Pixel",
            font=('arial', 14)
        )
        self.remcalc_px_label.grid(row=1, column=1)

        # Frame 1: px input
        self.remcalc_px = tk.Entry(
            self.remcalc_frame
        )
        self.remcalc_px.grid(row=2, column=1)

        # Frame 1: and 
        self.remcalc_and = tk.Label(
            self.remcalc_frame,
            text='=',
            font=('Arial', 14)
        )
        self.remcalc_and.grid(row=2, column=2, padx=20)

        # Frame 1: Label for rem input
        self.remcalc_px_label = tk.Label(
            self.remcalc_frame,
            text="rem",
            font=('arial', 14)
        )
        self.remcalc_px_label.grid(row=1, column=3)

        # Frame 1: rem input
        self.remcalc_rem = tk.Entry(
            self.remcalc_frame,
        )
        self.remcalc_rem.insert(0, '16')
        self.remcalc_rem.grid(row=2, column=3)

        # Frame 1: Button
        self.remcalc_button = tk.Button(
            self.remcalc_frame,
            text="berechnen",
            font=('Arial', 14),
        )
        self.remcalc_button.grid(row=2, column=4, padx=(20, 0))

        # Frame 1: Result
        self.remcalc_result = tk.Label(
            self.remcalc_frame,
            text="(Result)",
            font=('Arial', 18)
        )
        self.remcalc_result.grid(row=3, column=0, columnspan=5, pady=(20, 0))

        # Frame 1: Pack
        self.remcalc_frame.pack(padx=20, pady=20)

        self.root.mainloop()

GUI()