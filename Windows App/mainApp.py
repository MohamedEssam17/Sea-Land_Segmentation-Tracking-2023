import tkinter as tk
from page1 import Page1
from page2 import Page2
from page3 import Page3



class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.state("zoomed")  # to make full screen
        # self.geometry("1366x768+0+0")
        # self.w = self.winfo_screenwidth()
        # self.h = self.winfo_screenheight()
        # print(self.w, self.h)
        self.title("Home page")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for Page in (Page1, Page2, Page3):
            page = Page(self.container, self)
            self.pages[Page.__name__] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page("Page1")

    def show_page(self, page_name):
        page = self.pages[page_name]

        page.tkraise()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
