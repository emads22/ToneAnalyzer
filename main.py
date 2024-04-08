from pathlib import Path
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px


# Initialize SentimentIntensityAnalyzer
ANALYZER = SentimentIntensityAnalyzer()
# Define the directory where diary files are stored
DIARY_DIR = Path("./assets") / "diary"


def get_diaries_data(diaries_directory):
    """
    Retrieves sentiment analysis data for diary entries.

    Parameters:
        diaries_directory (Path): The directory containing diary files.

    Returns:
        list: A list of dictionaries containing sentiment analysis data for each diary entry.
    """
    # Get sorted list of diary files
    diary_files = sorted(diaries_directory.glob("*.txt"))

    data = []
    for diary_path in diary_files:
        # Open each diary file and perform sentiment analysis
        with open(diary_path) as f:
            diary_text = f.read()
            score = ANALYZER.polarity_scores(diary_text)

        # Extract date and sentiment scores
        element = {
            'date': diary_path.stem,
            'pos_score': score['pos'],
            'neg_score': score['neg']
        }

        data.append(element)

    return data


# Set up Streamlit app title
st.title("Diary Tone")

# Lists to store data for plotting
dates = []
positive_scores = []
negative_scores = []

# Get sentiment analysis data for diary entries
diary_data = get_diaries_data(DIARY_DIR)

# Extract dates and sentiment scores for plotting
for element in diary_data:
    dates.append(element['date'])
    positive_scores.append(element['pos_score'])
    negative_scores.append(element['neg_score'])

# Display positivity chart
st.subheader("Positivity")
positivity_figure = px.line(x=dates, y=positive_scores, labels={
    'x': 'Date', 'y': 'Positivity'})
st.plotly_chart(positivity_figure)

# Display negativity chart
st.subheader("Negativity")
negativity_figure = px.line(x=dates, y=negative_scores, labels={
    'x': 'Date', 'y': 'Negativity'})
st.plotly_chart(negativity_figure)
