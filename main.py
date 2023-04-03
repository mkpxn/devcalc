import tkinter as tk

class GUI:

    # Fonts
    font_l = ('Arial', 18)
    font_m = ('Arial', 14)
    font_s = ('Arial', 10)

    # Colors
    color_bg        = '#26272A'     #010409
    color_primary   = '#1B2125'     #0D1117
    color_accent    = '#4CCEAC'
    color_grey_f    = '#7A8490'     # Grey / Font
    color_grey_b    = '#21262D'     # Grey / Button
    color_white     = '#E4E8EC'
    color_red       = '#DB4F4A'
    color_blue      = '#6870FA'

    def __init__(self):

        # Root / Window
        self.root = tk.Tk()
        self.root.title('Dev Calculator')
        self.root.geometry('350x400')
        self.root.configure(background = self.color_bg)

        # Validation
        def validate(input):
            if input.isdigit() or input == '':
                return True
            else:
                return False

        int_validation = self.root.register(validate)

        # Frame 1: Pixel-to-REM calculator
        self.remcalc_frame = tk.Frame(self.root, background = self.color_bg)
        # self.remcalc_frame.columnconfigure(0, weight = 1)
        # self.remcalc_frame.columnconfigure(1, weight = 1)
        # self.remcalc_frame.columnconfigure(2, weight = 1)
        # self.remcalc_frame.columnconfigure(3, weight = 1)
        # self.remcalc_frame.columnconfigure(4, weight = 1)

        # Frame 1: Section Label
        self.remcalc_label = tk.Label(
            self.remcalc_frame, 
            text = "Rem Calculator", 
            font = self.font_l,
            bg = self.color_bg,
            fg = self.color_accent,
        )
        self.remcalc_label.grid(
            row = 0, 
            column = 0, 
            pady=(0, 20),
        )

        # Frame 1: Label for px input
        self.remcalc_px_label = tk.Label(
            self.remcalc_frame,
            text = "Pixel",
            font = self.font_s,
            bg = self.color_bg,
            fg = self.color_white,
        )
        self.remcalc_px_label.grid(
            row = 1, 
            column = 0,
        )

        # Frame 1: px input
        self.remcalc_px = tk.Entry(
            self.remcalc_frame,
            validate = 'all',
            validatecommand = (int_validation, '%P'),
            bg = self.color_primary,
            fg = self.color_white,
            insertbackground = self.color_white,
        )
        self.remcalc_px.insert(0, 16)
        self.remcalc_px.bind("<KeyPress>", self.shortcut)
        self.remcalc_px.grid(
            row = 2, 
            column = 0,
        )
        self.remcalc_px.focus()

        # Frame 1: Label for root input
        self.remcalc_root_label = tk.Label(
            self.remcalc_frame,
            text = "Root",
            font = self.font_s,
            bg = self.color_bg,
            fg = self.color_white,
        )
        self.remcalc_root_label.grid(
            row = 3, 
            column = 0,
            pady = (10, 0),
        )

        # Frame 1: root input
        self.remcalc_root = tk.Entry(
            self.remcalc_frame,
            validate = 'all',
            validatecommand = (int_validation, '%P'),
            bg = self.color_primary,
            fg = self.color_white,
            insertbackground = self.color_white,
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
            font = self.font_m,
            command = self.remcalc,
            bg = self.color_primary,
            fg = self.color_accent,
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
            font = self.font_l,
            bg = self.color_bg,
            fg = self.color_accent,
        )
        self.remcalc_result.grid(
            row = 6, 
            column = 0, 
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
    
    def shortcut(self, event):
        if event.keysym == 'Return':
            self.remcalc()
        
GUI()