'''
Made by Dario Gerald, 19.02.24. 

Github: https://github.com/Pinkk-Flag/

This is my algorithm that takes data from COT online, uses ratio weights and other technical indicators in order to find trades that could have good probabilities. 
'''

import subprocess

def main():
    print("Hello, and welcome to 'Silent Trend'.\nIt's a tool that utilises already online info from\nCOT data, and does complex analysis to classify specific tickers\nusing formulas to see the best trades you could make throughout the week.")
    print("\n" * 5)
    # Run data.py
    subprocess.run(["python", "data.py"])

    # Once data.py completes, run analysis.py
    import analysis

if __name__ == "__main__":
    main()