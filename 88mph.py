import whois
import requests
import os
from datetime import datetime  # Importing the datetime module

def generate_figlet_text(text):
    figlet_output = os.popen(f"figlet -f slant '{text}'").read()
    colored_output = "\033[1;31;40m" + figlet_output + "\033[0m"  # Red color with black background
    return colored_output

def get_website_creation_date(url):
    try:
        domain = whois.whois(url)
        creation_date = domain.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]  # Use the first creation date if there are multiple
        if isinstance(creation_date, datetime):
            return creation_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return "Website creation date not found."
    except Exception as e:
        return f"Error: {e}"

def search_wayback(url, option):
    if option == 1:
        creation_date = get_website_creation_date(url)
        print("Website Creation Date:", creation_date)
    elif option == 2:
        # API endpoint
        endpoint = "http://archive.org/wayback/available?url="

        # Sending the API request
        response = requests.get(endpoint + url)

        # Processing the response
        if response.status_code == 200:
            data = response.json()
            if 'archived_snapshots' in data:
                snapshots = data['archived_snapshots']
                if 'closest' in snapshots:
                    closest_snapshot = snapshots['closest']
                    print("Closest archived snapshot found:")
                    print("URL:", closest_snapshot['url'])
                    print("Timestamp:", closest_snapshot['timestamp'])
                else:
                    print("No archived snapshot found for the given URL.")
            else:
                print("No archived snapshot found for the given URL.")
        else:
            print("Error occurred while fetching archives.")
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    figlet_text = generate_figlet_text("Back to the Future")
    print(figlet_text)  # Printing Figlet text
    
    while True:
        # Example input for the user (printed in green)
        print("\033[1;32m\nExample Input: example.com\033[0m")
        url_to_search = input("\033[1;31mEnter the domain name (or type 'exit' to quit): \033[0m")
        
        if url_to_search.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'
        
        print("\nSelect an option:")
        print("1. Back in Time see website creation date")
        print("2. Stay in the Present (most recent timestamp)")
        option = input("Enter your choice (1 or 2): ")
        
        if option.isdigit():
            option = int(option)
            search_wayback(url_to_search, option)
        else:
            print("Invalid option. Please enter 1 or 2.")
