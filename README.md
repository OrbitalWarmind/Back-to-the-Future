# Back-to-the-Future
Python program that pulls the latest pages of URL's using the Wayback Machine.
# Wayback Machine URL Search

This Python script allows you to search for archived snapshots of a URL using the Wayback Machine API. It retrieves the closest archived snapshot along with its URL and timestamp.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
    ```
    pip install requests
    ```
3. Clone or download this repository to your local machine.
4. Run the script by executing the following command:
    ```
    python wayback_machine_search.py
    ```
5. Follow the on-screen instructions to enter the URL you want to search for archives.
6. The script will display the closest archived snapshot URL and timestamp if found.

## Dependencies

- requests: This library is used for making HTTP requests to the Wayback Machine API.

## Notes

- Make sure to have an active internet connection to fetch data from the Wayback Machine API.
- This version of the script does not include the option to play an mp3 file.
- For more information about the Wayback Machine API, visit: https://archive.org/help/wayback_api.php
