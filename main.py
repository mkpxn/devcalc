import tkinter as tk

class GUI:

    def __init__(self):

        # Root / Window
        self.root = tk.Tk()
        self.root.title('Dev Calculator')
        self.root.geometry('350x400')
        self.root.configure()

        # Frame 1: Pixel-to-REM calculator
        self.remcalc_frame = tk.Frame(self.root)
        # self.remcalc_frame.columnconfigure(0, weight = 1)
        # self.remcalc_frame.columnconfigure(1, weight = 1)
        # self.remcalc_frame.columnconfigure(2, weight = 1)
        # self.remcalc_frame.columnconfigure(3, weight = 1)
        # self.remcalc_frame.columnconfigure(4, weight = 1)

        # Frame 1: Section Label
        self.remcalc_label = tk.Label(
            self.remcalc_frame, 
            text = "Rem Calculator", 
            font = ('Arial', 18),
        )
        self.remcalc_label.grid(
            row = 0, 
            column = 0, 
            # columnspan = 5, 
            pady=(0, 20),
        )

        # Frame 1: Label for px input
        self.remcalc_px_label = tk.Label(
            self.remcalc_frame,
            text = "Pixel",
            font = ('arial', 14),
        )
        self.remcalc_px_label.grid(
            row = 1, 
            column = 0,
        )

        # Frame 1: px input

        # Validation
        def validate(input):
            return input.isdigit()

        int_validation = self.root.register(validate)

        # Widget setup
        self.remcalc_px = tk.Entry(
            self.remcalc_frame,
            validate = 'all',
            validatecommand = (int_validation, '%P')
        )
        self.remcalc_px.insert(0, 16)
        self.remcalc_px.grid(
            row = 2, 
            column = 0,
        )

        # Frame 1: and 
        # self.remcalc_and = tk.Label(
        #     self.remcalc_frame,
        #     text = '=',
        #     font = ('Arial', 14),
        # )
        # self.remcalc_and.grid(
        #     row = 3, 
        #     column = 0, 
        #     padx = 20,
        # )

        # Frame 1: Label for root input
        self.remcalc_root_label = tk.Label(
            self.remcalc_frame,
            text = "Root",
            font = ('arial', 14),
        )
        self.remcalc_root_label.grid(
            row = 3, 
            column = 0,
            pady = (10, 0),
        )

        # Frame 1: root input
        self.remcalc_root = tk.Entry(
            self.remcalc_frame,
        )
        self.remcalc_root.insert(0, 16)
        self.remcalc_root.grid(
            row = 4, 
            column = 0,
        )

        # Frame 1: Button
        self.remcalc_button = tk.Button(
            self.remcalc_frame,
            text = "berechnen",
            font = ('Arial', 14),
            command = self.remcalc,
        )
        self.remcalc_button.grid(
            row = 5, 
            column = 0, 
            pady = 20,
        )

        # Frame 1: Result
        self.remcalc_result = tk.Label(
            self.remcalc_frame,
            text = "1.0",
            font = ('Arial', 18),
        )
        self.remcalc_result.grid(
            row = 6, 
            column = 0, 
            # columnspan = 5, 
            pady = 30,
        )

        # Frame 1: Pack
        self.remcalc_frame.pack(padx=20, pady=20)

        # Main Loop
        self.root.mainloop()

    # Functions
    def remcalc(self):
        px = int(self.remcalc_px.get())
        root = int(self.remcalc_root.get())

        result = px / root
        self.remcalc_result.config(text = result)
        
GUI()