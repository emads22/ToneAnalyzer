from pathlib import Path
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px
import fitz  # PyMuPDF


# Initialize SentimentIntensityAnalyzer
ANALYZER = SentimentIntensityAnalyzer()


def get_diaries_data(diaries_files):
    """
    Retrieves sentiment analysis data for diary entries.

    Parameters:
        diaries_files (list): The list of uploaded diary files.

    Returns:
        list: A list of dictionaries containing sentiment analysis data for each diary entry.
    """
    data = []
    for diary_file in diaries_files:
        # Read each diary file and perform sentiment analysis
        diary_text = diary_file.read().decode("utf-8")
        score = ANALYZER.polarity_scores(diary_text)

        # Extract date from the filename (assuming filenames represent dates)
        diary_path = Path(diary_file.name)
        element = {
            'date': diary_path.stem,
            'pos_score': score['pos'],
            'neg_score': score['neg']
        }

        data.append(element)

    return data


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.

    Parameters:
        pdf_file (UploadedFile): The uploaded PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text


def analyze_pdf_text(text):
    """
    Performs sentiment analysis on the extracted PDF text.

    Parameters:
        text (str): The extracted text from the PDF.

    Returns:
        dict: Sentiment scores (positive, negative, neutral, compound).
    """
    return ANALYZER.polarity_scores(text)


def render_home():
    st.markdown("""
        <p>
            <span style="display: inline; font-size: 3em; font-weight: bold;">ToneAnalyzer:&nbsp;&nbsp;</span>
            <span style="display: inline; font-size: 2em; font-weight: normal;">Diary and eBook Sentiment Analysis</span>
        </p>
    """, unsafe_allow_html=True)
    st.write("Choose an analysis to perform using the sidebar.")


def render_diary_page():
    st.title("Diary Tone Analysis")
    uploaded_files = st.file_uploader(
        "Upload Diary Files", accept_multiple_files=True, type=['txt'])

    if uploaded_files:
        # Lists to store data for plotting
        dates = []
        positive_scores = []
        negative_scores = []

        # Get sentiment analysis data for diary entries
        diary_data = get_diaries_data(uploaded_files)

        # Extract dates and sentiment scores for plotting
        for element in diary_data:
            dates.append(element['date'])
            positive_scores.append(element['pos_score'])
            negative_scores.append(element['neg_score'])

        # Display positivity chart
        st.subheader("Positivity Over Time")
        positivity_figure = px.line(x=dates, y=positive_scores, labels={
            'x': 'Date', 'y': 'Positivity Score'}, title='Positivity Trend')
        st.plotly_chart(positivity_figure)

        # Display negativity chart
        st.subheader("Negativity Over Time")
        negativity_figure = px.line(x=dates, y=negative_scores, labels={
            'x': 'Date', 'y': 'Negativity Score'}, title='Negativity Trend')
        st.plotly_chart(negativity_figure)
    else:
        st.write("Please upload diary files to analyze.")


def render_pdf_page():
    st.title("PDF eBook Tone Analysis")
    uploaded_pdf_file = st.file_uploader("Upload PDF eBook", type=['pdf'])

    if uploaded_pdf_file:
        # Extract text from the uploaded PDF
        ebook_text = extract_text_from_pdf(uploaded_pdf_file)

        # Perform sentiment analysis on the extracted text
        pdf_sentiment_scores = analyze_pdf_text(ebook_text)

        # Display sentiment scores for the PDF
        st.subheader(f'"{uploaded_pdf_file.name}" eBook Sentiment Analysis:')
        st.write("- Positive Score:", pdf_sentiment_scores['pos'])
        st.write("- Negative Score:", pdf_sentiment_scores['neg'])
        st.write("- Neutral Score:", pdf_sentiment_scores['neu'])
        st.write("- Compound Score:", pdf_sentiment_scores['compound'])

        # Determine if the eBook is positive or negative
        # The compound score is a normalized score ranging from -1 to 1, where values closer to 1 indicate a positive sentiment, values closer to -1 indicate a negative sentiment, and values around 0 indicate a neutral sentiment
        if pdf_sentiment_scores['compound'] >= 0.05:
            st.success("This eBook has an overall positive tone.")
        elif pdf_sentiment_scores['compound'] <= -0.05:
            st.warning("This eBook has an overall negative tone.")
        else:
            st.info("This eBook has a neutral tone.")
    else:
        st.write("Please upload a PDF eBook to analyze.")


# Main application
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to", ["Home", "Diary Tone Analysis", "PDF eBook Tone Analysis"])

if page == "Diary Tone Analysis":
    render_diary_page()
elif page == "PDF eBook Tone Analysis":
    render_pdf_page()
else:
    render_home()
