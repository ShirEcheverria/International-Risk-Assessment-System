from tkinter import Tk
from Open_Sanctions_API import OpenSanctionsAPI, OS_API_KEY
from App_Section import App

OS_API_KEY = "c1adfd53d859be0245bd4fa03a1f98de"  # OpenSanctions API key

if __name__ == "__main__":
    root = Tk()  # Create the main application window
    api = OpenSanctionsAPI(OS_API_KEY)  # Create an instance of the OpenSanctionsAPI class with the API key
    app = App(root, api)  # Create an instance of the App class, passing in the root window and API instance
    root.mainloop()  # Start the main event loop
