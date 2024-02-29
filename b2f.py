import requests
import os

def generate_figlet_text(text):
    figlet_output = os.popen(f"figlet -f slant '{text}'").read()
    colored_output = "\033[1;31;40m" + figlet_output + "\033[0m"  # Red color with black background
    return colored_output

def search_wayback(url):
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
                if 'url' in closest_snapshot:
                    print("Closest archived snapshot found:")
                    print("URL:", closest_snapshot['url'])
                    print("Timestamp:", closest_snapshot['timestamp'])
                else:
                    print("No archived snapshot found for the given URL.")
            else:
                print("No archived snapshot found for the given URL.")
        else:
            print("No archived snapshot found for the given URL.")
    else:
        print("Error occurred while fetching archives.")

if __name__ == "__main__":
    figlet_text = generate_figlet_text("Back to the Future ->")
    print(figlet_text)  # Printing Figlet text
    
    while True:
        # Example input for the user
        print("\nExample Input: https://www.example.com")
        url_to_search = input("Enter the URL to search for archives (or type 'exit' to quit): ")
        
        if url_to_search.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'
        
        search_wayback(url_to_search)
