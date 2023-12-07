import threading

import os

from tkinter import filedialog


import customtkinter
import tkinter as tk
from prediction_using_smooth_blending import MODEL
from tkinter import *

from PIL import ImageTk, Image
import matplotlib.pyplot as plt




class Page2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # set background
        self.configure(bg="#242424")



        # Create a label to display the mask from the selected photo
        self.label_image = customtkinter.CTkLabel(master=self, text="Original Image", bg_color="#242424",
                                                  text_color="white", font=("Arial", 20, "bold"))
        self.label_image.place(x=1220, y=40)

        # Create a label to display the selected photo
        self.label_mask = customtkinter.CTkLabel(master=self, text="Mask", bg_color="#242424",
                                                 text_color="white", font=("Arial", 20, "bold"))
        self.label_mask.place(x=1255, y=423)

        self.image_label = None
        self.mask_label = None
        self.chart_label = None
        self.file_path = None
        self.file_path_mask = None
        self.file_path_figure = None
        #-------------------------------------------  Functios select_image, show_mask, show_figure  ------------------------------------


        list_buttons = ['self.button_show_mask', 'self.button_select', 'self.button_analysis']
        # def showed(button_show):
        #     for button in list_buttons:
        #         if (button_show == button):
        #             button.place(x=480, y=720)
        #         else:
        #             button.place_forget()



        #fun for open mask and create figure save them
        def open_mask():

            head_tail = os.path.split(self.file_path)
            # عدد الpathes ال فوق لحد ال folder ال فيه folder image, mask, histogram
            first = head_tail[0].split('/')[:-1]
            first = '/'.join([str(elem) for elem in first])
            last = head_tail[1].split('.')
            # must be create folder name masks
            self.file_path_mask = first + '/masks/' + last[0] + '.png'

            if self.file_path_mask:
                # print(type(file_path_mask), '\n', type(file_path))
                mask = Image.open(self.file_path_mask)
                # mask = mask.convert("L")
                mask = mask.resize((400, 400))
                mask = ImageTk.PhotoImage(mask)
                if self.mask_label:
                    self.mask_label.destroy()

                self.mask_label = customtkinter.CTkLabel(master=self, image=mask, text="")
                self.mask_label.mask = mask
                self.mask_label.place(x=1120, y=465)

                # make a graph for the mask
                image = Image.open(self.file_path_mask).convert('1')
                image_data = image.load()

                # Define variables to store the counts of 0 and 1 pixels
                zeros_count = 0
                ones_count = 0

                # Iterate over each pixel in the image and increment the appropriate count
                plt.rcParams['axes.facecolor'] = '#242424'
                plt.rcParams['figure.facecolor'] = '#242424'
                plt.gca().tick_params(colors='white')
                for x in range(image.width):
                    for y in range(image.height):
                        if image_data[x, y] == 0:
                            zeros_count += 1
                        else:
                            ones_count += 1
                plt.figure(figsize=(8, 6))
                # Calculate the percentage of zeros in the image
                zero_percentage = (zeros_count / (image.width * image.height)) * 100

                # Create a bar chart using matplotlib

                ax = plt.axes()
                labels = ['Land', 'Sea']
                counts = [100 - zero_percentage, zero_percentage]
                plt.bar(labels, counts, color=['#52BD96', '#305DA1'], width=0.8)

                # get name of folder
                area = head_tail[0].split('/')[-2]

                ax.spines['bottom'].set_color('white')
                ax.spines['left'].set_color('white')
                ax.spines['top'].set_color('#242424')
                ax.spines['right'].set_color('#242424')
                ax.spines['left'].set_linewidth(2)
                ax.spines['bottom'].set_linewidth(2)
                plt.xlabel('Pixel Value', color='white')
                plt.ylabel('Percentage', color="white")
                plt.ylim([0, 100])  # set y-axis limits to 0-100%
                plt.yticks([0, 25, 50, 75, 100])
                plt.gca().tick_params(colors='white')  # set the color of the axis to white
                ax.set_title(f"This figure shows the ratio between land and sea in {area}", fontsize=15, color="white")
                legend_labels = ["Land ", "Sea "]
                legend_colors = ["#52BD96", "#305DA1"]
                legend_elements = [plt.Rectangle((0, 0), 1, 1, color=color) for color in legend_colors]
                plt.legend(legend_elements, legend_labels, labelcolor='white', frameon=False)
                # Add percentages to the top of each bar
                for i, v in enumerate(counts):
                    plt.text(i - 0.1, v + 1, str(round(v, 1)) + '%', color='white', fontweight='bold')

                last = head_tail[1].split('.')
                self.file_path_figure = first + '/histograms/' + last[0] + '.png'
                #print(self.file_path_mask + '\n' + self.file_path_figure)
                plt.savefig(self.file_path_figure)

                #print(self.file_path_mask + '\n' + self.file_path + '\n' + self.file_path_figure)

        def open_figure():
            head_tail = os.path.split(self.file_path)
            first = head_tail[0].split('/')[:-1]
            first = '/'.join([str(elem) for elem in first])
            last = head_tail[1].split('.')
            # must be create folder name histograms
            self.file_path_figure = first + '/histograms/' + last[0] + '.png'

            if self.file_path_figure:
                # Load the chart image into a PhotoImage object
                self.chart_image = Image.open(self.file_path_figure)
                self.chart_image = ImageTk.PhotoImage(self.chart_image)

                if self.chart_label:
                    self.chart_label.destroy()

                # Embed the chart image in a Tkinter Label
                self.chart_label = customtkinter.CTkLabel(master=self, image=self.chart_image, text="", width=800, height=400)
                self.chart_label.place(x=0, y=150)

        #fun for cleaning this page after click on the back
        def clean_page2():
            if self.image_label:
                self.image_label.place_forget()
            if self.mask_label:
                self.mask_label.place_forget()
            if self.chart_label:
                self.chart_label.place_forget()

        def clean_mask_figure():
            if self.mask_label:
                self.mask_label.place_forget()
            if self.chart_label:
                self.chart_label.place_forget()

        # Create a function for selecting an image file
        def select_image():

            self.file_path = filedialog.askopenfilename()
            if self.file_path:
                image = Image.open(self.file_path)
                # Resize the image to 265x265 pixels
                image = image.resize((400, 400))
                # Convert the image to PhotoImag
                image = ImageTk.PhotoImage(image)
                # Remove the old image
                if self.image_label:
                    self.image_label.destroy()

                # Create a new label to display the image
                self.image_label = customtkinter.CTkLabel(master=self, image=image, text="")
                self.image_label.image = image
                self.image_label.place(x=1120, y=80)

                self.button_show_mask.place_forget()
                self.button_select.place_forget()
                self.button_analysis.place(x=480, y=720)


        # create two thread for splits the process on the CPU
        self.stop_t1 = threading.Event()

        # fun show button mask
        def show_button_mask():
            self.button_show_mask.place(x=480, y=720)
            self.label.place_forget()
            self.button_analysis.place_forget()
            self.stop_t1.set()




        # fun show select button
        def show_button_select():
            self.button_select.place(x=480, y=720)
            self.button_analysis.place_forget()
            self.button_show_mask.place_forget()

        # fun loading label
        def show_label_loading():
            # create label with "Loading" text
            self.label = customtkinter.CTkLabel(master=self, text="Loading......", text_color="white",
                                                        font=("arial", 20, "bold"))
            self.label.place(x=400, y=400)
            # set timer for 3 seconds
            self.after(60000, show_button_mask)
            threading.Thread(target=lambda: MODEL(self.file_path), name='t1').start()




        # add a button to close Page2 and show homepage
        self.button_back = customtkinter.CTkButton(master=self, corner_radius=200, text="❮ Back", width=30, height=35,
                                                   fg_color="#242424", bg_color="#242424", font=("Arial", 20, "bold"),
                                                   text_color="white",
                                                   command=lambda: [controller.show_page("Page1"), clean_page2()],
                                                   hover_color="#333333")
        self.button_back.place(x=50, y=35)

        #button for select image
        self.button_select = customtkinter.CTkButton(master=self, corner_radius=6, text="Select Image", width=230,
                                                       height=40, bg_color="#242424", fg_color="#3c4043",hover_color="#444444",
                                                       font=("Arial", 16, "bold"),
                                                       command=lambda :[select_image(), clean_mask_figure()])
        self.button_select.place(x=480, y=720)



        #button for analysis image
        self.button_analysis = customtkinter.CTkButton(master=self, corner_radius=6, text="Analysis", width=230, height=40,
                                             bg_color="#242424", fg_color="#1d5f9c", font=("Arial", 16, "bold"),
                                                       command=lambda: [show_label_loading()])

        #button for show mask
        self.button_show_mask = customtkinter.CTkButton(master=self, corner_radius=6, text="Show Mask", width=230, height=40,
                                              bg_color="#242424", fg_color="#52BD96", hover_color="#337a61",
                                              font=("Arial", 16, "bold"), command=lambda :[show_button_select(), open_mask(), open_figure()])

