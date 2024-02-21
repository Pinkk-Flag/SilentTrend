import csv

PATH_location = "Weekly Data CSV/Data.csv"
tickers = ["S&P500", "NASDAQ", "RUSSEL", "DOW E-MINI", "30Y T-BOND", "10Y T-BOND", "DOLLAR INDEX", "EURO FX", "SWISS FRANC", "BRITISH POUND", "JAPANESE YEN", "CANADIAN DOLLAR", "AUSTRALIAN DOLLAR", "NEW ZEALAND DOLLAR", "MEXICAN PESO", "CRUDE OIL", "GASOLINE", "HEATING OIL", "NATURAL GAS", "GOLD", "SILVER", "PLATINUM", "PALLADIUM", "COPPER", "SOYBEANS", "SOYBEAN MEAL", "SOYBEAN OIL", "CORN", "WHEAT", "ROUGH RICE", "COTTON", "COFFEE", "COCOA", "SUGAR", "ORANGE JUICE", "LIVE CATTLE", "FEEDER CATTLE", "LEAN HOGS", "BITCOIN", "VIX FUTURES"]

def read_csv_to_list(csv_file_path):
    data = []
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                data.extend(row)
            else:
                data.append('N/A')
    return data

def calculate_direction(long_large, short_large, total_large):
    direction_weight = (long_large - short_large) / total_large
    return direction_weight

def calculate_confidence(ratio_large, ratio_comm, direction_weight):
    confidence_factor = (ratio_large / (ratio_large + ratio_comm)) / direction_weight
    return round(confidence_factor, 3)

def build_dictionary(data, tickers):
    result_dict = {}
    num_tickers = len(tickers)
    num_data = len(data)
    
    for i in range(0, num_data, num_tickers*4):
        for j in range(num_tickers):
            ticker = tickers[j]
            long_large = int(data[i + j*4 + 2])
            short_large = int(data[i + j*4 + 3])
            total_large = long_large + short_large
            direction = calculate_direction(long_large, short_large, total_large)
            ratio_large = long_large
            ratio_comm = int(data[i + j*4 + 0])
            confidence = calculate_confidence(ratio_large, ratio_comm, direction)

            # Add direction and confidence to result_dict
            result_dict[f"{ticker} DIRECTION"] = direction
            result_dict[f"{ticker} CONFIDENCE"] = confidence

    return result_dict

# Read data from CSV file
data = read_csv_to_list(PATH_location)

# Build dictionary from data and calculate direction and confidence for each ticker
result_dict = build_dictionary(data, tickers)

# Output direction and confidence for each ticker to terminal
for ticker in tickers:
    direction = result_dict[f"{ticker} DIRECTION"]
    confidence = result_dict[f"{ticker} CONFIDENCE"]
    print(f"SYMBOL: {ticker}")
    print(f"DIRECTION: {direction}")
    print(f"CONFIDENCE: {confidence}")

