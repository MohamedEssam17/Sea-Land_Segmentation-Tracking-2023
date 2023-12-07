
import pyautogui
import customtkinter
import tkinter as tk
import datetime

from tkinter import messagebox

from tkintermapview import TkinterMapView

from geopy.geocoders import Nominatim

from PIL import ImageTk, Image

from location import add_location_from_file, read_location_file


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # set background
        self.configure(bg="#242424")

#############Create logo##############################
        label = customtkinter.CTkLabel(master=self, text="", width=1920, height=55, bg_color="#333333")
        label.place(x=0, y=0)

        logo = Image.open('logo blue small new 1.png')
        # Resize the image to 265x265 pixels
        logo = logo.resize((95, 55))
        # Convert the image to PhotoImag
        logo = ImageTk.PhotoImage(logo)

        # Create a new label to display the image
        image_label = customtkinter.CTkLabel(master=self, image=logo, text="" , bg_color="#333333")
        image_label.place(x=10, y=5)

        #----------------------------------------- Search Location -----------------------------------------------

        # Create the search function
        def search():
            # Get search query from search bar
            query = self.search_bar.get()
            # Convert search query to coordinates
            geolocator = Nominatim(user_agent="Map App")
            location = geolocator.geocode(query)
            if location is None:
                #print("Location not found")
                messagebox.showwarning('Location Not found', 'Please, Check The coordinates')
                return
            # Move map view to search location
            self.widgetmap.set_position(location.latitude, location.longitude)
            self.widgetmap.set_zoom(16)

        # Clear the search word from search bar
        def clear_search(event):
            self.search_bar.delete(0, tk.END)

        # Create the search button
        self.search_button = customtkinter.CTkButton(master=self, corner_radius=6, text="Search", width=100, height=35,
                                                     bg_color="#333333", fg_color="#1d5f9c", font=("Arial", 16, "bold"),
                                                     command=search)
        self.search_button.place(x=800, y=15)

        # Create search bar
        self.search_bar = customtkinter.CTkEntry(master=self, corner_radius=8, width=350, height=35,
                                                 fg_color="#333333", bg_color="#333333", font=("Arial", 15),
                                                 text_color="white",
                                                 border_width=2, border_color="#656565")

        self.search_bar.insert(5, "Search a location...")
        # Bind the search function to the search bar
        self.search_bar.bind('<Return>', lambda event: search())
        # Bind the clear function to the search bar
        self.search_bar.bind("<Button-1>", clear_search)
        self.search_bar.place(x=420, y=15)

        # ----------------------------------------- Map and Option Menu -----------------------------------------------
        # Create google maps widget
        self.widgetmap = TkinterMapView(self, width=1420, height=920, corner_radius=0, max_zoom=0)
        self.widgetmap.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga")
        self.widgetmap.place(x=500, y=70)

        # Create dropdown list
        self.map_mode_var = customtkinter.StringVar(value="Map mode")  # set initial value
        self.ports_var = customtkinter.StringVar(value="Ports")  # set initial value
        self.beaches_var = customtkinter.StringVar(value="Beaches")  # set initial value

        # fun for map mode optionmenu
        def map_mode_callback(choice):
            selection = self.dropdownlist_mapmode.get()
            result = " "
            if selection == "Google normal":
                result = self.widgetmap.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
                #print("optionmenu dropdown clicked:", selection)
            elif selection == "Google satellite":
                result = self.widgetmap.set_tile_server("https://mt0.google.com/vt/lyrs=s,m&hl=en&x={x}&y={y}&z={z}&s=Ga")
                #print("optionmenu dropdown clicked:", selection)
            elif selection == "Satellite no labels":
                result = self.widgetmap.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga")
                #print("optionmenu dropdown clicked:", selection)
            return result

        self.dropdownlist_mapmode_label = customtkinter.CTkLabel(master=self, text="Map Mode:", bg_color="#242424",
                                                            text_color="white", font=("Arial", 18))
        self.dropdownlist_mapmode_label.place(x=25, y=120)
        self.dropdownlist_mapmode = customtkinter.CTkOptionMenu(master=self, corner_radius=6, width=200, height=35,
                                                           bg_color="#242424", fg_color="#1d5f9c",
                                                           dropdown_fg_color="#333333", dropdown_font=("Arial", 14),
                                                           dropdown_text_color="white",
                                                           font=("Arial", 14), hover=True, button_color="#144870",
                                                            values=["Google normal", "Google satellite","Satellite no labels"],
                                                            command=map_mode_callback, variable=self.map_mode_var)
        self.dropdownlist_mapmode.place(x=25, y=150)



        # Provide the file path of your location data file
        location_ports = 'location_data_for_ports.txt'

        ports, ports_values = read_location_file(location_ports)
        #print(type(ports_values))
        ports_values.insert(0, "Ports")
        #print(ports, ports_values)
        # fun for ports optionmenu
        def ports_callback(choice):
            port = self.dropdownlist_seaport.get()
            if port == 'Ports':
                return

            result = self.widgetmap.set_position(ports[port][0], ports[port][1])
            self.widgetmap.set_zoom(16)

            #print(ports[port][0], ports[port][1])
            return result

        self.dropdownlist_seaport_label = customtkinter.CTkLabel(master=self, text="Ports:", bg_color="#242424",
                                                            text_color="white", font=("Arial", 18))
        self.dropdownlist_seaport_label.place(x=25, y=320)
        self.dropdownlist_seaport = customtkinter.CTkOptionMenu(master=self, corner_radius=6, width=220, height=35,
                                                           bg_color="#242424", fg_color="#1d5f9c",
                                                           dropdown_fg_color="#333333", dropdown_font=("Arial", 14),
                                                           dropdown_text_color="white",
                                                           font=("Arial", 14), hover=True, button_color="#144870",
                                                            values=ports_values, command=ports_callback, variable=self.ports_var)
        self.dropdownlist_seaport.place(x=25, y=350)

        #button for add port
        self.button_add_port = customtkinter.CTkButton(master=self, corner_radius=6, text="+ Add Port", width=105, height=35,
                                                        bg_color="#242424", fg_color="#1d5f9c", font=("Arial", 14),
                                                       command=lambda :add_location_from_file(location_ports))
        self.button_add_port.place(x=275, y=350)



        # Provide the file path of your location data file
        location_beaches = 'location_data_for_beaches.txt'

        beaches, beaches_values = read_location_file(location_beaches)
        beaches_values.insert(0, "Beaches")
        # fun for beaches optionmenu
        def beaches_callback(choice):
            beache = self.dropdownlist_beaches.get()
            if beache == 'Beaches':
                return
            result = self.widgetmap.set_position(beaches[beache][0], beaches[beache][1])
            self.widgetmap.set_zoom(16)

            # print(beaches[beache][0], beaches[beache][1])
            return result

        self.dropdownlist_beaches_label = customtkinter.CTkLabel(master=self, text="Beaches:", bg_color="#242424",
                                                            text_color="white", font=("Arial", 18))
        self.dropdownlist_beaches_label.place(x=25, y=420)

        self.dropdownlist_beaches = customtkinter.CTkOptionMenu(master=self, corner_radius=6, width=220, height=35,
                                                           bg_color="#242424", fg_color="#1d5f9c",
                                                           dropdown_fg_color="#333333", dropdown_font=("Arial", 14),
                                                           dropdown_text_color="white",
                                                           font=("Arial", 14), hover=True, button_color="#144870",
                                                           values=beaches_values, command=beaches_callback, variable=self.beaches_var)
        self.dropdownlist_beaches.place(x=25, y=450)

        # button for add beache
        self.button_add_beache = customtkinter.CTkButton(master=self, corner_radius=6, text="+ Add Beache", width=105,height=35,
                                                            bg_color="#242424", fg_color="#1d5f9c", font=("Arial", 14),
                                                         command=lambda :add_location_from_file(location_beaches))
        self.button_add_beache.place(x=275, y=450)

        self.dropdownlist_seaport.bind('<Return>', lambda event: ports_callback())
        self.dropdownlist_beaches.bind('<Return>', lambda event: beaches_callback())
        self.dropdownlist_mapmode.bind('<Return>', lambda event: map_mode_callback())

        # ----------------------------------------- Butons Capture, An -----------------------------------------------

        # fun for get image and set in folders
        def take_screenshot():
            screenshot = pyautogui.screenshot()
            # Specify the coordinates of the specific area
            left = 826
            top = 146
            right = 1594
            bottom = 914

            # Crop the screenshot
            screenshot = screenshot.crop((left, top, right, bottom))

            # Resize the cropped image to 400x400 pixels
            # resized_image = cropped_image.resize((400, 400))

            current_date = datetime.datetime.now().strftime("%Y-%m-%d")

            # Save the screenshot with the date
            port = self.dropdownlist_seaport.get()
            beache = self.dropdownlist_beaches.get()

            if port != 'Ports':
                screenshot.save(f"Info Data/Ports/{port}/images/{current_date}.png")
            elif beache != 'Beaches':
                screenshot.save(f"Info Data/Beaches/{beache}/images/{current_date}.png")
            else:
                screenshot.save(f"Info Data/Free_Capture/images/{current_date}.png")


        # button to take screenshot
        self.button_capture = customtkinter.CTkButton(master=self, corner_radius=6, text="Capture image", width=230, height=40,
                                                 bg_color="#242424", fg_color="#1d5f9c", font=("Arial", 16, "bold"), command=take_screenshot)
        self.button_capture.place(x=80, y=580)


        # add a button that open Page2
        self.button_analysis = customtkinter.CTkButton(master=self, corner_radius=6, text="Analysis image", width=230,
                                                  height=40,
                                                  bg_color="#242424", fg_color="#1d5f9c", font=("Arial", 16, "bold"),
                                                  command=lambda: [controller.show_page("Page2")])
        self.button_analysis.place(x=80, y=650)

        # add a button that open Page3
        self.button_tracing = customtkinter.CTkButton(master=self, corner_radius=6, text="Trace result", width=230,
                                                 height=40,
                                                 bg_color="#242424", fg_color="#1d5f9c", font=("Arial", 16, "bold"),
                                                 command=lambda: [controller.show_page("Page3")])
        self.button_tracing.place(x=80, y=720)


    # Create the search function




