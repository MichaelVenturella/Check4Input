# Check4Input
<br>
 
 ```  ______   __                            __        __    __  ______                                  __     
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

```

                                                                              
<br>
A Python script designed to scan a list of subdomains for user input elements such as forms, input fields, textareas, buttons, and keywords like "login" or "submit". It uses `curl` to fetch webpage content and checks both HTTP and HTTPS protocols, including following links that might lead to input pages. This can be useful for Red Teamers for quick identification of websites that may be targeted for later input attacks such as BruteForce, SQL Injection, etc. Or this could be a great tool for Defenders to understand what sites may be targeted in potential attacks!

## Features
- Scans subdomains over HTTP and HTTPS.
- Detects HTML elements like `<form>`, `<input>`, `<textarea>`, and `<button>`.
- Searches for keywords indicating user input (e.g., "login", "signin", "submit").
- Follows up to 5 links per page (e.g., login redirects) to detect hidden input pages.
- Outputs results to a CSV file with detailed findings.
- Customizable input and output files via command-line switches.

## Requirements
- **Python 3.x**: Ensure Python is installed (`python3 --version`).
- **`curl`**: Used to fetch webpage content.
  - **Ubuntu/Debian**: `sudo apt install curl`
  - **macOS**: `brew install curl`
  - **Windows**: Install via WSL or download a `curl` binary (e.g., from [curl.se](https://curl.se/windows/)).
- A text file containing subdomains to scan (one per line).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MichaelVenturella/check4input.git
   cd check4input
## Usage
 ```bash
python check4input.py -i <input_file> -o <output_file>
```
- -i/--input: Specifies the input file with subdomains (default: subdomains.txt).
- -o/--output: Specifies the output CSV file (default: subdomains_user_input.csv).

## Contributing
- Report bugs or suggest features via Issues.
- Submit improvements via pull requests.
- Questions? Open a discussion or issue!
