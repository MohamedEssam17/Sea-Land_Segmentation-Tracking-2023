
import os

from tkinter import filedialog, messagebox
from skimage.metrics import structural_similarity as compare_ssim
import imutils
import cv2
import customtkinter
from tkinter import *

from PIL import ImageTk, Image
import matplotlib.pyplot as plt

import datetime

import tkinter as tk


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # set background
        self.configure(bg="#242424")

        #Initialise the vars
        self.current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.image_label1 = None
        self.image_label2 = None
        self.mask_label1 = None
        self.mask_label2 = None
        self.chart_image2 = None
        self.file_path_figure = None
        self.chart_label2 = None
        self.file_paths = []
        self.diff_label = None
        self.diff_image = None
        self.text1 = None
        self.text2 = None
        self.label1 = None
        self.label2 = None
        self.label3 = None
        self.label4 = None


        #fun get the difference in between two masks
        def difference(image1, image2, save1, save2, save3):
            # load the two input images
            imageA = cv2.imread(image1)
            imageB = cv2.imread(image2)
            # convert the images to grayscale
            grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

            # compute the Structural Similarity Index (SSIM) between the two
            # images, ensuring that the difference image is returned
            (score, diff) = compare_ssim(grayA, grayB, full=True)
            diff = (diff * 255).astype("uint8")
            # print("SSIM: {}".format(score))
            # print("SSIM: {}".format(1 - score))

            # threshold the difference image, followed by finding contours to
            # obtain the regions of the two input images that differ
            thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)

            for c in cnts:
                # compute the bounding box of the contour and then draw the
                # bounding box on both input images to represent where the two
                # images differ
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

            bitwiseXor = cv2.bitwise_xor(imageA, imageB)

            cv2.imwrite(save3, bitwiseXor)
            cv2.imwrite(save1, imageA)
            cv2.imwrite(save2, imageB)

        # Create a function for selecting an image file
        def select_images():

            # Get a list of file paths for the selected images
            self.file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.tif")])
            # Check that at least one image was selected
            if len(self.file_paths) == 2:

                # image1 and image2 selected in pag3
                image1 = Image.open(self.file_paths[0])
                image1 = image1.resize((330, 330))
                photo1 = ImageTk.PhotoImage(image1)

                if self.image_label1:
                    self.image_label1.destroy()
                self.image_label1 = tk.Label(self, image=photo1)
                self.image_label1.image = photo1
                self.image_label1.place(x=180, y=160)

                image2 = Image.open(self.file_paths[1])
                image2 = image2.resize((330, 330))
                photo2 = ImageTk.PhotoImage(image2)

                if self.image_label2:
                    self.image_label2.destroy()
                self.image_label2 = tk.Label(self, image=photo2)
                self.image_label2.image = photo2
                self.image_label2.place(x=180, y=550)

                head_tail = os.path.split(self.file_paths[0])
                first = head_tail[0].split('/')[:-1]
                first = '/'.join([str(elem) for elem in first])
                last = head_tail[1].split('.')
                self.text1 = last[0]

                # must be create folder name masks
                file_path_mask1 = first + '/masks/' + last[0] + '.png'
                file_path_difference1 = first + '/differences/' + last[0] + '.png'


                head_tail = os.path.split(self.file_paths[1])
                first = head_tail[0].split('/')[:-1]
                first = '/'.join([str(elem) for elem in first])
                last = head_tail[1].split('.')
                self.text2 = last[0]

                # must be create folder name masks
                file_path_mask2 = first + '/masks/' + last[0] + '.png'
                file_path_difference2 = first + '/differences/' + last[0] + '.png'


                coast_line_path = first + '/differences/between (' + self.text1 + ') and (' + self.text2 + ').png'
                print(coast_line_path)
                #call fun difference
                difference(file_path_mask1, file_path_mask2, file_path_difference1, file_path_difference2, coast_line_path)

                # mask1 and mask2 selected in pag3
                mask1 = Image.open(file_path_difference1)
                # mask = mask.convert("L")
                mask1 = mask1.resize((330, 330))
                mask1 = ImageTk.PhotoImage(mask1)
                if self.mask_label1:
                    self.mask_label1.destroy()

                self.mask_label1 = customtkinter.CTkLabel(master=self, image=mask1, text="")
                self.mask_label1.mask = mask1
                self.mask_label1.place(x=450, y=130)

                mask2 = Image.open(file_path_difference2)
                # mask = mask.convert("L")
                mask2 = mask2.resize((330, 330))
                mask2 = ImageTk.PhotoImage(mask2)
                if self.mask_label2:
                    self.mask_label2.destroy()

                self.mask_label2 = customtkinter.CTkLabel(master=self, image=mask2, text="")
                self.mask_label2.mask = mask2
                self.mask_label2.place(x=450, y=440)



                #print(self.text1, self.text2)
                # labels for images and masks
                self.label1 = customtkinter.CTkLabel(master=self, text=f"Image at: {self.text1}", bg_color="#242424",
                                                     text_color="white", font=("Arial", 16, "bold"))
                self.label1.place(x=205, y=100)

                self.label2 = customtkinter.CTkLabel(master=self, text=f"Mask at: {self.text1}", bg_color="#242424",
                                                     text_color="white", font=("Arial", 16, "bold"))
                self.label2.place(x=505, y=100)

                # another label then 6 mon
                self.label3 = customtkinter.CTkLabel(master=self, text=f"Image at: {self.text2}", bg_color="#242424",
                                                     text_color="white", font=("Arial", 16, "bold"))
                self.label3.place(x=205, y=410)

                self.label4 = customtkinter.CTkLabel(master=self, text=f"Mask at: {self.text2}", bg_color="#242424",
                                                     text_color="white", font=("Arial", 16, "bold"))
                self.label4.place(x=505, y=410)

                # Load the first image
                image1 = Image.open(file_path_mask2).convert('1')
                filename_with_extension = os.path.basename(file_path_mask2)
                filename, extension = os.path.splitext(filename_with_extension)
                image_data1 = image1.load()

                # Load the second image
                image2 = Image.open(file_path_mask1).convert('1')
                filename_with_extension = os.path.basename(file_path_mask1)
                filename2, extension2 = os.path.splitext(filename_with_extension)
                image_data2 = image2.load()

                # Define variables to store the counts of 0 and 1 pixels for both images
                zeros_count1 = 0
                ones_count1 = 0
                zeros_count2 = 0
                ones_count2 = 0

                plt.rcParams['axes.facecolor'] = '#242424'
                plt.rcParams['figure.facecolor'] = '#242424'
                # plt.gca().tick_params(colors='white')
                # Iterate over each pixel in the first image and increment the appropriate count
                for x in range(image1.width):
                    for y in range(image1.height):
                        if image_data1[x, y] == 0:
                            zeros_count1 += 1
                        else:
                            ones_count1 += 1

                # Iterate over each pixel in the second image and increment the appropriate count
                for x in range(image2.width):
                    for y in range(image2.height):
                        if image_data2[x, y] == 0:
                            zeros_count2 += 1
                        else:
                            ones_count2 += 1

                # Calculate the percentage of zeros in each image
                zero_percentage1 = (zeros_count1 / (image1.width * image1.height)) * 100
                zero_percentage2 = (zeros_count2 / (image2.width * image2.height)) * 100

                # Create a figure and plot the bars for both images side by side
                labels = [filename, filename2]
                counts1 = [100 - zero_percentage1, zero_percentage1]
                counts2 = [100 - zero_percentage2, zero_percentage2]
                bar_width = 0.2

                fig, ax = plt.subplots(figsize=(8, 4))
                ax.bar([0.3, 0.5], counts1, bar_width, color=['#52BD96', '#305DA1'], label='Image 1')
                ax.bar([1.1, 1.3], counts2, bar_width, color=['#52BD96', '#305DA1'], label='Image 2')
                # Calculate the x-coordinates of the start and end points of the dashed line
                x1 = 0 + bar_width / 2
                x2 = 1.3 + bar_width / 2
                y = counts1[0]

                # Draw the dashed line
                ax.plot([x1, x2], [y, y], linestyle='--', color='green')
                # Calculate the x-coordinates of the start and end points of the dashed line
                z1 = 0 + bar_width / 2
                z2 = 1.3 + bar_width / 2
                y = counts1[1]

                # Draw the dashed line
                ax.plot([z1, z2], [y, y], linestyle='--', color='red')
                # get name of folder
                area = head_tail[0].split('/')[-2]
                # Set the chart properties
                ax.set_ylim([0, 100])
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
                plt.gca().tick_params(colors='white')
                ax.set_title(f"This figure shows the ratio between land and sea in {area}", fontsize=15, color="white")
                ax.set_ylabel('Percentage')
                ax.set_xticks([0.4, 1.2])
                ax.set_xticklabels(labels)

                legend_labels = ["Land ", "Sea "]
                legend_colors = ["#52BD96", "#305DA1"]
                legend_elements = [plt.Rectangle((0, 0), 1, 1, color=color) for color in legend_colors]
                plt.legend(legend_elements, legend_labels, labelcolor='white', frameon=False)

                for i, v in enumerate(counts1):
                    ax.text(i * 0.2 + 0.3, v + 2, f'{v:.1f}%', color='white', ha='center', fontweight='bold')

                for i, v in enumerate(counts2):
                    ax.text(i * 0.2 + 1.1, v + 2, f'{v:.1f}%', color='white', ha='center', fontweight='bold')

                head_tail = os.path.split(self.file_paths[0])
                first = head_tail[0].split('/')[:-1]
                first = '/'.join([str(elem) for elem in first])

                # must be create folder name histograms
                self.file_path_figure = first + '/trace/between (' + self.text1 + ') and (' + self.text2 + ').png'
                plt.savefig(self.file_path_figure)

                self.button_select.place_forget()

                self.button_tracing.place(x=310, y=720)


                if self.chart_label2:
                    self.chart_label2.place_forget()
                if self.diff_label:
                    self.diff_label.place_forget()
                if self.diff_image:
                    self.diff_image.place_forget()
            elif (len(self.file_paths) != 2 and len(self.file_paths) > 0):
                messagebox.showinfo('Warning', 'Choose only two images please!')
        #fun show figure tracing
        def open_figure():

            head_tail = os.path.split(self.file_paths[0])
            first = head_tail[0].split('/')[:-1]
            first = '/'.join([str(elem) for elem in first])

            # must be create folder name histograms
            file_path_figure2 = first + '/trace/between (' + self.text1 + ') and (' + self.text2 + ').png'

            # Load the chart image into a PhotoImage object
            if file_path_figure2:
                # Load the chart image into a PhotoImage object
                self.chart_image2 = Image.open(file_path_figure2)
                self.chart_image2 = ImageTk.PhotoImage(self.chart_image2)

                if self.chart_label2:
                    self.chart_label2.destroy()
                # Embed the chart image in a Tkinter Label
                self.chart_label2 = customtkinter.CTkLabel(master=self, image=self.chart_image2, text="", width=800, height=400)
                self.chart_label2.place(x=780, y=410)

            coast_line_figure = first + '/differences/between (' + self.text1 + ') and (' + self.text2 + ').png'
            self.diff_label = customtkinter.CTkLabel(master=self, text="This image show the amount of change between masks",
                                                bg_color="#242424",
                                                text_color="white", font=("Arial", 16, "bold"))
            self.diff_label.place(x=920, y=90)

            if coast_line_figure:
                self.diff_image = Image.open(coast_line_figure)
                self.diff_image = self.diff_image.resize((330, 330))
                self.diff_image = ImageTk.PhotoImage(self.diff_image)

                # if self.diff_image:
                #     self.diff_image.destroy()

                self.diff_image = customtkinter.CTkLabel(master=self, image=self.diff_image, text="")
                self.diff_image.place(x=1000, y=125)


        # fun show select button
        def show_button_select():
                self.button_select.place(x=310, y=720)

                self.button_tracing.place_forget()
                if self.diff_image:
                    self.diff_image.place_forget()
                if self.diff_label:
                    self.diff_label.place_forget()
        #fun for clean the page
        def clean_page3():

            self.image_label1.place_forget()

            self.image_label2.place_forget()
            self.mask_label1.place_forget()
            self.mask_label2.place_forget()
            if self.chart_label2:
                self.chart_label2.place_forget()

            self.label1.place_forget()
            self.label2.place_forget()
            self.label3.place_forget()
            self.label4.place_forget()

            if self.diff_label:
                self.diff_label.place_forget()
            if self.diff_image:
                self.diff_image.place_forget()

            self.button_tracing.place_forget()
            self.button_select.place(x=310, y=720)

        # add a button to close Page2 and show homepage
        self.button_back = customtkinter.CTkButton(master=self, corner_radius=200, text="❮ Back", width=30, height=35,
                                                   fg_color="#242424", bg_color="#242424", font=("Arial", 20, "bold"),
                                                   text_color="white",
                                                   command=lambda: [controller.show_page("Page1"), clean_page3()],
                                                   hover_color="#333333")
        self.button_back.place(x=50, y=35)



        # button for select image
        self.button_select = customtkinter.CTkButton(master=self, corner_radius=6, text="Select Image", width=230,
                                                     height=40, bg_color="#242424", fg_color="#3c4043",
                                                     hover_color="#444444",
                                                     font=("Arial", 16, "bold"),
                                                     command=lambda: [select_images()])
        self.button_select.place(x=310, y=720)

        self.button_tracing = customtkinter.CTkButton(master=self, corner_radius=6, text="Tracing", width=230,
                                                       height=40,
                                                       bg_color="#242424", fg_color="#1d5f9c",
                                                       font=("Arial", 16, "bold"),
                                                       command=lambda: [show_button_select(), open_figure()])

