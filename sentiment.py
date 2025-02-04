import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
   
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:  # Adjust thresholds as needed
        return "Positive"
    elif polarity < -0.1: # Adjust thresholds as needed
        return "Negative"
    else:
        return "Neutral"

def process_csv(csv_file):
    try:
        df = pd.read_csv(csv_file,encoding='unicode_escape')
        if 'text' not in df.columns:
            print("Error: 'text' column not found in the CSV file.")
            return

        for index, row in df.iterrows():
            text = str(row['text'])  # Ensure text is a string
            sentiment = analyze_sentiment(text)
            print(f"Text: {text}\nSentiment: {sentiment}\n---")

    except FileNotFoundError:
        print(f"Error: File not found: {csv_file}")
    except pd.errors.EmptyDataError:
        print(f"Error: CSV file is empty: {csv_file}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
   
    choice = input("Choose an option:\n1. Analyze text input\n2. Run dataset tests\nEnter your choice (1 or 2): ")

    if choice == "1":
        text = input("Enter text to analyze: ")
        analyze_sentiment(text)
        sentiment = analyze_sentiment(text)
        print(f"Text: {text}\nSentiment: {sentiment}\n---")     
    elif choice == "2":
        process_csv("./train.csv")
    else:
        print("Invalid choice. Please enter 1 or 2.")
    


