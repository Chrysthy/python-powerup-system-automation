<h1 align="center"> Python PowerUP | System Automation </h1> 

<p align="center">
  A Python automation project that registers products in a web system using PyAutoGUI, Pandas and CSV data.
  <br>
  This project was created to practice task automation, data handling and project organization in Python.
</p>

<p align="center">  
  <a href="#-screenshots">Screenshots</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-features">Features</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-project">Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-how-it-works">How It Works</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-installation">Installation</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-license">License</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-contributing">Contributing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#support">Support</a>  
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=c920c9&labelColor=000000">
</p>

<br>

## 📸 Screenshots

<p align="center">
  <img src=".github/project-demo.gif" alt="Project Demo">
</p>

<br>

## 🛠 Technologies

* Python
* PyAutoGUI
* Pandas
* Python Dotenv
* Pathlib
* CSV
* Git and GitHub

<br>

## ✨ Features

- Opens the browser automatically
- Accesses the web system
- Uses environment variables for login credentials
- Reads product data from a CSV file
- Registers products automatically
- Handles empty observation fields
- Uses dynamic file paths with Pathlib
- Separates sensitive information from the source code

<br>

## 💻 Project

Python PowerUP is an automation project developed to simulate the registration of products in a company system.

The automation uses PyAutoGUI to control the keyboard and mouse, while Pandas is responsible for reading and handling the product database.

Sensitive information, such as login credentials, is stored using environment variables instead of being written directly in the source code.

<br>

## 🔄 How It Works

1. Opens Google Chrome
2. Accesses the system
3. Logs in using credentials stored in environment variables
4. Loads the product database from a CSV file
5. Reads each product from the database
6. Fills in the registration form automatically
7. Repeats the process until all products are registered

<br>
