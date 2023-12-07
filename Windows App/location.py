import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import os

def add_location_from_file(file_path):
    def save_location_data():
        location_name = entry_location_name.get()
        longitude = entry_longitude.get()
        latitude = entry_latitude.get()

        # Validate if all fields are filled
        if location_name == '' or longitude == '' or latitude == '':
            messagebox.showwarning('Missing Information', 'Please fill in all fields.')
            return

        # Save the location data to a text file
        with open(file_path, 'a') as file:
            file.write(f"{location_name},{longitude},{latitude}\n")

        messagebox.showinfo('Success', 'The data has been added successfully!,\nrestart the program to see the changes,please!')
        window.destroy()

    # Create the main window
    window = tk.Tk()
    window.title('Location Data')
    window.geometry('300x300')
    window.configure(bg='#242424')

    # Create the input fields for location name, longitude, and latitude
    label_location_name = ctk.CTkLabel(master=window, text='Location Name:', text_color='white')
    label_location_name.pack()
    entry_location_name = ctk.CTkEntry(master=window)
    entry_location_name.pack()

    label_longitude = ctk.CTkLabel(master=window, text='Longitude:', text_color='white')
    label_longitude.pack()
    entry_longitude = ctk.CTkEntry(master=window)
    entry_longitude.pack()

    label_latitude = ctk.CTkLabel(master=window, text='Latitude:', text_color='white')
    label_latitude.pack()
    entry_latitude = ctk.CTkEntry(master=window)
    entry_latitude.pack()

    # Create the save button
    button_save = ctk.CTkButton(master=window, fg_color="#1d5f9c", text='Save', command=save_location_data)
    button_save.pack(pady=20)

    # Start the application
    window.mainloop()


# read beaches from file 'location_data_for_beaches.txt'
#add_location_from_file('location_data_for_beaches.txt')
def read_location_file(file_path):
    loction = {}
    loction_coordinate = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == '':
                continue
            name, longitude, latitude = line.strip().split(',')
            loction[name] = [float(longitude), float(latitude)]
            loction_coordinate.append(name)


        place = file_path.split('_')
        list_folders = ['images', 'masks', 'histograms', 'trace', 'differences']
        for loc in loction_coordinate:

            if place[-1] == 'beaches.txt':
                loct = f"Info Data/Beaches/{loc}"
            else:
                loct = f"Info Data/Ports/{loc}"

            if not os.path.exists(loct):
                os.makedirs(loct)
                for subfolder_name in list_folders:
                    subfolder_path = os.path.join(loct, subfolder_name)
                    os.makedirs(subfolder_path)

        return loction, loction_coordinate