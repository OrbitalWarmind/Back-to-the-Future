# Back-to-the-Future (Website Analysis Tool)

This Python script allows you to see when a website was created and it will search for archived snapshots of a URL using the Wayback Machine API. It retrieves the closest archived snapshot, Give your public IP address and the SSL certificate of the site.

## Features

- Retrieve website creation dates using WHOIS database.
- Check SSL certificate details for a given website.
- Fetch and display the public IP address of the user.
- View the closest archived snapshot available on the Wayback Machine.
- Simple and intuitive command-line interface.

## Installation
1. Clone the repository to your local machine:
    ```
    git clone https://github.com/OrbitalWarmind/Back-to-the-Future.git
    ```
## Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
    ```
    pip install requests python-whois
    pip install requests
    ```
3. Navigate to the directory containing the `88mph.py` file in your terminal.
4. Run the script by executing the following command:
    ```
    python 88mph.py
    ```
5. Follow the on-screen instructions to enter the URL you want to search for archives.
6. The script will give you creation date and display the closest archived snapshot URL and timestamp if found.

## Dependencies

- requests: This library is used for making HTTP requests to the Wayback Machine API.

## Notes
- Make sure to have an active internet connection to fetch data from the Wayback Machine API.
- For more information about the Wayback Machine API, visit: https://archive.org/help/wayback_api.php
## Creator Pcap_Pirate with help from ChatGPT.
I wanted to see if I could get ChatGPT 3.5 to create me this idea I had with Python.
