import subprocess
import os
import whois
import ssl
import datetime
import socket
import requests
import turtle
import random
import time

def generate_figlet_text(text):
    figlet_output = os.popen(f"figlet -f slant '{text}' | lolcat").read()
    return figlet_output

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

def start_flux_capacitor():
    # Delay for 1 second before starting
    time.sleep(1)
    
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("black")

    # Create a turtle object
    artist = turtle.Turtle()
    artist.speed(0)
    artist.width(2)

    # Define colors
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # Draw the time travel effect
    for i in range(600):
        artist.pencolor(random.choice(colors))
        artist.forward(i)
        artist.left(135)

    # Hide the turtle
    artist.hideturtle()

    # Keep the window open
    screen.mainloop()

def search_wayback(url, option):
    if option == 1:
        creation_date = get_website_creation_date(url)
        print("\033[1;34mWebsite Creation Date:\033[0m", creation_date)
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
                    print("\033[1;34mClosest archived snapshot found:\033[0m")
                    print("\033[1;34mURL:\033[0m", closest_snapshot['url'])
                    print("\033[1;34mTimestamp:\033[0m", closest_snapshot['timestamp'])
                else:
                    print("\033[1;31mNo archived snapshot found for the given URL.\033[0m")
            else:
                print("\033[1;31mNo archived snapshot found for the given URL.\033[0m")
        else:
            print("\033[1;31mError occurred while fetching archives.\033[0m")
    elif option == 3:
        ssl_info = get_ssl_certificate_info(url)
        if isinstance(ssl_info, dict):
            print("\n\033[1;34mSSL Certificate Information:\033[0m")
            for key, value in ssl_info.items():
                print("\033[1;34m{}:\033[0m {}".format(key, value))
        else:
            print("\033[1;31mError:\033[0m", ssl_info)
    elif option == 4:
        public_ip = get_public_ip()
        print("\033[1;32mYour Public IP Address:\033[0m", public_ip)
    elif option == 5:
        start_flux_capacitor()
    else:
        print("\033[1;31mInvalid option selected.\033[0m")

if __name__ == "__main__":
    figlet_text = generate_figlet_text("Back to the Future")
    print(figlet_text)  # Printing Figlet text
    
    while True:
        # Example input for the user
        print("\033[1;34mExample Input: example.com\033[0m")
        url_to_search = input("\033[1;32mEnter the domain name (or type 'exit' to quit):\033[0m ")
        
        if url_to_search.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'
        
        print("\nSelect an option:")
        print("1. Back in Time see website creation date")
        print("2. Stay in the present (most recent timestamp)")
        print("3. Check SSL Certificate")
        print("4. Get your public IP address")
        print("5. Start the Flux Capacitor")
        option = input("Enter your choice (1, 2, 3, 4, or 5): ")
        
        if option.isdigit():
            option = int(option)
            search_wayback(url_to_search, option)
        else:
            print("\033[1;31mInvalid option. Please enter 1, 2, 3, 4, or 5.\033[0m")
