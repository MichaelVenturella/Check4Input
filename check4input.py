import csv
import subprocess
import re
from urllib.parse import urljoin

# Cool ASCII art banner
ASCII_ART = """
  ______   __                            __        __    __  ______                                  __     
 /      \ /  |                          /  |      /  |  /  |/      |                                /  |    
/$$$$$$  |$$ |____    ______    _______ $$ |   __ $$ |  $$ |$$$$$$/  _______    ______   __    __  _$$ |_   
$$ |  $$/ $$      \  /      \  /       |$$ |  /  |$$ |__$$ |  $$ |  /       \  /      \ /  |  /  |/ $$   |  
$$ |      $$$$$$$  |/$$$$$$  |/$$$$$$$/ $$ |_/$$/ $$    $$ |  $$ |  $$$$$$$  |/$$$$$$  |$$ |  $$ |$$$$$$/   
$$ |   __ $$ |  $$ |$$    $$ |$$ |      $$   $$<  $$$$$$$$ |  $$ |  $$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ | __ 
$$ \__/  |$$ |  $$ |$$$$$$$$/ $$ \_____ $$$$$$  \       $$ | _$$ |_ $$ |  $$ |$$ |__$$ |$$ \__$$ |  $$ |/  |
$$    $$/ $$ |  $$ |$$       |$$       |$$ | $$  |      $$ |/ $$   |$$ |  $$ |$$    $$/ $$    $$/   $$  $$/ 
 $$$$$$/  $$/   $$/  $$$$$$$/  $$$$$$$/ $$/   $$/       $$/ $$$$$$/ $$/   $$/ $$$$$$$/   $$$$$$/     $$$$/  
                                                                              $$ |                          
                                                                              $$ |                          
                                                                              $$/                           
"""

# Input and output file names
input_file = 'subdomains.txt'
output_file = 'subdomains_user_input.csv'

# List to store results
results = []

# Patterns to detect user input elements
INPUT_PATTERNS = [
    r'<form',           # Form tags
    r'<input',          # Input fields
    r'<textarea',       # Text areas
    r'<button',         # Buttons
    r'login',           # Login-related keywords
    r'signin',          # Sign-in keywords
    r'submit'           # Submit keywords
]

# Read subdomains from file
try:
    with open(input_file, 'r') as file:
        subdomains = file.readlines()
except FileNotFoundError:
    print(f"Error: {input_file} not found. Please create it with your subdomains.")
    exit(1)

# Print ASCII art
print(ASCII_ART)

# Function to check a URL for input indicators
def check_url(url):
    try:
        # Run curl with redirect following (-L) and capture output
        curl_output = subprocess.check_output(
            ['curl', '-s', '-L', '--max-time', '5', url],
            stderr=subprocess.STDOUT
        )
        curl_text = curl_output.decode('utf-8', errors='replace').lower()
        
        # Check for input patterns
        for pattern in INPUT_PATTERNS:
            if re.search(pattern, curl_text):
                return True, curl_text
        return False, curl_text
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return False, None

# Check each subdomain
for subdomain in subdomains:
    subdomain = subdomain.strip()
    user_input_detected = "No"
    details = ""

    # Try HTTP and HTTPS
    for protocol in ['http', 'https']:
        base_url = f"{protocol}://{subdomain}"
        input_found, response_text = check_url(base_url)

        if input_found:
            user_input_detected = f"Yes ({protocol})"
            details = "Direct input detected"
            print(f"User input detected at {base_url}")
            break
        elif response_text:
            # Look for links/buttons that might lead to input pages
            link_pattern = r'href=["\'](.*?)["\']'
            links = re.findall(link_pattern, response_text)
            for link in links[:5]:  # Limit to 5 links to avoid overload
                if 'login' in link.lower() or 'signin' in link.lower():
                    full_url = urljoin(base_url, link)
                    input_found, _ = check_url(full_url)
                    if input_found:
                        user_input_detected = f"Yes ({protocol} - via {link})"
                        details = f"Input detected after following {link}"
                        print(f"User input detected at {full_url} via {link}")
                        break
            if user_input_detected.startswith("Yes"):
                break
        else:
            print(f"No response from {base_url}")

    # Add result to list
    results.append({
        'Subdomains': subdomain,
        'User Input Detected': user_input_detected,
        'Details': details
    })
    if user_input_detected == "No":
        print(f"No user input detected or subdomain offline: {subdomain}")

# Write results to CSV
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Subdomains', 'User Input Detected', 'Details']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for result in results:
        writer.writerow(result)

print(f"\nResults saved to {output_file}")