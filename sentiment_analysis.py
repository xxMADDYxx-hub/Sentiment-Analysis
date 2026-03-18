import pandas as pd
from textblob import TextBlob

# -----------------------------
# 1. LOAD DATASET
# -----------------------------
file_path = "reviews.csv"   # Make sure this file exists

try:
    df = pd.read_csv(file_path)
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: reviews.csv not found.")
    exit()

# -----------------------------
# 2. PREVIEW DATA
# -----------------------------
print("🔹 First 5 Rows:")
print(df.head())

# -----------------------------
# 3. SENTIMENT FUNCTION
# -----------------------------
def get_sentiment(text):
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# -----------------------------
# 4. APPLY SENTIMENT ANALYSIS
# -----------------------------
df["Sentiment"] = df["review"].apply(get_sentiment)

# -----------------------------
# 5. RESULTS
# -----------------------------
print("\n🔹 Sentiment Results:")
print(df)

print("\n🔹 Sentiment Counts:")
print(df["Sentiment"].value_counts())