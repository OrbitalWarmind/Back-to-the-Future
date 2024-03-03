# Back-to-the-Future (Website Analysis Tool)

This Python script offers a variety of functionalities related to internet tools and utilities, with a fun "Back to the Future" theme. Here's a breakdown of what it does:

Figlet Text Generation: It generates stylized text using the figlet command and displays it using lolcat.

User Interaction Loop: It runs an interactive loop where the user can input a domain name and choose from several options.

## Functionality

- Option 1: Retrieves and displays the creation date of the provided website.
- Option 2: Checks for the most recent archived snapshot of the website using the Wayback Machine.
- Option 3: Fetches and displays SSL certificate information for the website.
- Option 4: Retrieves and displays the public IP address of the user.
- Option 5: Initiates a graphical effect mimicking the time travel effect from "Back to the Future" using Turtle graphics.
- Support for Exiting: The loop can be exited by typing 'exit'.

Error Handling: It includes basic error handling for various operations like fetching SSL information, getting public IP, etc.

Colorful Output: The script also uses ANSI escape codes for colorful output in the terminal.

Overall, it's a playful and functional script that combines internet utilities with a theme from popular culture.

## Features

- Retrieve website creation dates using WHOIS database.
- View the closest archived snapshot available on the Wayback Machine.
- Check SSL certificate details for a given website.
- Fetch and display the public IP address of the user.
- Start Flux Capacitor (easter egg)
- Simple and intuitive command-line interface.
- Python 3.x is required to run the script.

## Installation
1. Clone the repository to your local machine:
    ```
    git clone https://github.com/OrbitalWarmind/Back-to-the-Future.git
    ``` 
## Dependencies 
1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
    ```
    pip install requests python-whois
    pip install requests
    ```
## Usage
3. Navigate to the directory containing the `88mph.py` file in your terminal.
4. Run the script by executing the following command:
    ```
    python 88mph.py
    ```
5. Follow the on-screen instructions to enter the URL you want to search for archives.
6. The script will give you creation date and display the closest archived snapshot URL and timestamp if found.
  
## Additional Library Details:
- whois: Used to retrieve WHOIS information for domain names, enabling extraction of creation dates.
- requests: Utilized for making HTTP requests, enabling communication with external APIs such as the Wayback Machine.
  
## Modules Used
- import subprocess
- import os
- import whois
- import ssl
- import datetime
- import socket
- import requests
- import turtle
- import random
- import time

## Notes
- System Dependencies
Certain functionalities of the script depend on system-level features, which may require additional setup or permissions:

## Internet Access
- The script relies on internet connectivity to fetch data such as SSL certificate information, public IP addresses, and archived snapshots from the Wayback Machine. Ensure your system has internet access during script execution.
SSL Certificate Information
SSL certificate retrieval requires a functioning SSL/TLS connection to the specified domain. Ensure that your system's SSL/TLS configuration is properly set up and that it allows outbound connections on port 443 (the default HTTPS port).
Graphical Effects (Turtle Graphics)
If you intend to use the "Start the Flux Capacitor" feature, ensure that your system supports graphical output using the Turtle module. This typically requires a GUI environment or an X server.
-
## Creator ChatGPT 3.5 assisted by Pcap_Pirate.
Hello, I wanted to see if I could get ChatGPT 3.5 to fully create me this idea I had with Python on it's own and it did it! It would give me errors at times when it got futher into the program but feeding it it's own errors fixed its own code and TaDa! Here it is full code written in ChatGPT 3.5.
