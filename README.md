# SilentTrend
This is 'SilentTrend', a tool that curates COT data to usable and actionable steps for trading.

### What is it?

COT data, or the *Commitment of Traders**, is data given by the US government from many different exchanges, e.g.,CME, CBOE, CBOT, etc. However, the data it is given is often very cluttered and hard to decipher. On top of that, it is hard to know what you want to do **with** that data. 

<img width="462" alt="image" src="https://github.com/Pinkk-Flag/SilentTrend/assets/91942071/9fdf4798-c83b-48e7-b03b-874f2371ef7c">

Of course, it is still decipherable, but really, it becomes hard to do some real analysis and gain true efficiency with time.
Hence, SilentTrend.


### How does it work?

Created in python (due to my inexperience in other languages and large library amount) and relies heavily on libraries.

Main library I would credit would be **BeautifulSoup**, a webscraping library. I used it to get the data from online sources, then used other libraries to create it into a csv, then convert it into a dictionary. After that, analysis is preformed in order to get the confidence and direction. Finally, outputted via the terminal. Also uses the library subprocesses to make sure it is all run from **main.py**. Of course, right now, it is quite inefficient, but it gets the work done (if you can wait 30 seconds or so). 

# Main Dependencies

Before using 'Silent Trend', ensure you have the following dependencies installed:

- **Python 3.x:** Ensure you have Python 3.x installed on your system. You can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

- **Python Packages:** You will need to install the following Python packages using pip, Python's package installer:
  - `beautifulsoup4`: This package is used for web scraping. You can install it using the following command:
    ```bash
    pip install beautifulsoup4
    ```

- **Requests:** Requests is an elegant and simple HTTP library for Python. You can install it using the following command:
  ```bash
  pip install requests

### How to run?
First, please download as a zip, or clone it in the directory of your choice with the link (click the green "code" button you see. Then, given you have all the dependencies, run main.py either on an IDE or a terminal or anything that can run your code, and that is all you need.

### Example use case

<img width="183" alt="image" src="https://github.com/Pinkk-Flag/SilentTrend/assets/91942071/1ba5920e-f115-415d-8c78-2d9e065fb20c">

A simple terminal interface. Admittedly, the interface is not the most user friendly, but that will come in future github repositories.

### Tickers
"S&P500", "NASDAQ", "RUSSEL", "DOW E-MINI", "30Y T-BOND", "10Y T-BOND", "DOLLAR INDEX", "EURO FX", "SWISS FRANC", "BRITISH POUND", "JAPANESE YEN", "CANADIAN DOLLAR", "AUSTRALIAN DOLLAR", "NEW ZEALAND DOLLAR", "MEXICAN PESO", "CRUDE OIL", "GASOLINE", "HEATING OIL", "NATURAL GAS", "GOLD", "SILVER", "PLATINUM", "PALLADIUM", "COPPER", "SOYBEANS", "SOYBEAN MEAL", "SOYBEAN OIL", "CORN", "WHEAT", "ROUGH RICE", "COTTON", "COFFEE", "COCOA", "SUGAR", "ORANGE JUICE", "LIVE CATTLE", "FEEDER CATTLE", "LEAN HOGS", "BITCOIN", "VIX FUTURES"

