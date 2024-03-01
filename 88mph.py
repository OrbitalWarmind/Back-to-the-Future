import requests
import os
import whois
import ssl
import datetime
import socket

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
        if isinstance(creation_date, datetime.datetime):
            return creation_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return "Website creation date not found."
    except Exception as e:
        return f"Error: {e}"

def get_ssl_certificate_info(url):
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=url) as s:
            s.connect((url, 443))
            cert = s.getpeercert()
            return {
                "Issuer": dict(x[0] for x in cert["issuer"]),
                "Subject": dict(x[0] for x in cert["subject"]),
                "Expiry Date": datetime.datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z").strftime("%Y-%m-%d %H:%M:%S"),
                "Serial Number": cert["serialNumber"],
            }
    except Exception as e:
        return f"Error: {e}"

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        if response.status_code == 200:
            return response.json()["ip"]
        else:
            return "Failed to fetch public IP."
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
    elif option == 3:
        public_ip = get_public_ip()
        print("Your Public IP Address:", public_ip)
    elif option == 4:
        ssl_info = get_ssl_certificate_info(url)
        if isinstance(ssl_info, dict):
            print("\nSSL Certificate Information:")
            for key, value in ssl_info.items():
                print(f"{key}: {value}")
        else:
            print("Error:", ssl_info)
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
        print("1. Back in Time to see website creation date")
        print("2. Stay in the present (most recent timestamp)")
        print("3. Get your public IP address")
        print("4. Check SSL Certificate of Site")
        option = input("Enter your choice (1, 2, 3, or 4): ")
        
        if option.isdigit():
            option = int(option)
            search_wayback(url_to_search, option)
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")
