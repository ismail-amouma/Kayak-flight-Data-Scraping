
# Kyak Scraping

The Kyak Scraping project allows you to automate flight search and scrape flight details from Kayak.com. The script provides three types of search results: Cheapest, Quickest, and Best.

## Table of Contents
- [Requirements](#requirements)
- [Usage](#usage)
- [Disclaimer](#disclaimer)

## Requirements

Before running the script, make sure you have the following installed:

- Python 3.x
- Chrome browser

## Usage

1. Clone this repository to your local machine using the command:

   ```bash
   git clone https://github.com/ismail-amouma/Kayak-flight-Data-Scraping.git
   ```

2. Install the required Python packages using pip:

   ```bash
   pip install selenium openpyxl webdriver-manager
   ```

3. Open the terminal (command prompt) and navigate to the directory where `kayak.py` and `main.py` are located.

4. Run the script using Python:

   ```bash
   python main.py
   ```

5. Follow the instructions prompted on the terminal to enter the required details for the flight search:

   - From which city?
   - Where to?
   - When will you fly? (Use format DD-MM-YYYY)
   - When will you return? (Use format DD-MM-YYYY)

6. The script will automate the flight search on Kayak.com, scrape the flight details for Cheapest, Quickest, and Best options, and save the results in separate Excel files.

7. The Excel files will be named `Final_results_OutFlight_ReturnFlight.xlsx`, where `OutFlight` and `ReturnFlight` will be replaced with the actual flight routes you provided.

## Disclaimer

This script is intended for educational purposes and personal use only. Make sure to abide by Kayak.com's terms of service and use this script responsibly. The authors are not responsible for any misuse or violation of terms while using this script.

---

Please note that the usage instructions are general, and you may need to modify them based on the specific structure of your project or any additional features you might add. Also, consider adding more details and explanations about each function in the script if needed.
```

