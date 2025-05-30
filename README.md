# International-Risk-Assessment-System
Our project aims to utilize various international databases of individuals and companies of political, criminal, or economic interest that may pose a risk to any entity, in order to prevent and combat any potential threats. give me name to this project
🛡️ OpenSanctions Personal Profile Monitoring Tool
This is a GUI-based Python application that allows users to search individuals or organizations in the OpenSanctions database and visualize match results. It is especially useful for compliance checks, background screening, and personal investigations.

🔧 Built With
Python 3

Tkinter – GUI interface

Requests – HTTP communication with the API

Matplotlib – For plotting match result percentages

OpenSanctions API – Real-time access to global sanctions and risk data

✨ Features
Search individuals or entities by name and type (Person, Company, Organization, etc.)

Optional country filter for more accurate results

Live match results displayed in a sortable table

Double-click to view details, including aliases, nationality, birth info, positions, and source URLs

Color-coded bar chart visualization of match confidence scores:

🔵 Blue: Low match (≤ 50%)

🟠 Orange: Medium match (51–80%)

🔴 Red: High match (> 80%)

🖥️ How It Works
OpenSanctionsAPI class
Handles communication with the OpenSanctions API:

Sends POST requests with the query

Parses and returns results

Fetches detailed entity data when needed

App class (Tkinter GUI)
Manages the entire user interface:

Input fields for name, entity type, and country

Results shown in a ttk.Treeview table

Double-clicking a row opens a detail window

Uses matplotlib to display a bar chart of match scores

Plotting logic

Takes all match scores and builds a horizontal bar chart

Colors indicate the level of match

Bar labels show exact percentages
