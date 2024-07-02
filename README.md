# ToneAnalyzer: Diary and eBook Sentiment Analysis

## Overview
ToneAnalyzer: Diary and eBook Sentiment Analysis is a Streamlit web application designed to analyze the emotional tone of diary entries and eBooks. It evaluates the positivity and negativity of each entry or eBook and visualizes the results over time.

## Features
- **Sentiment Analysis**: Analyzes the sentiment of diary entries using NLTK's Vader Sentiment Intensity Analyzer.
- **Interactive Interface**: Provides a user-friendly interface for viewing sentiment analysis results.
- **Visualization**: Generates line charts to visualize the positivity and negativity trends over time.

## Technologies Used
- **nltk**: Natural Language Toolkit, used for performing sentiment analysis on text data.
- **plotly**: A graphing library that makes interactive, publication-quality graphs online.
- **PyMuPDF**: A lightweight PDF viewer and toolkit, used for extracting text from PDF files.
- **streamlit**: An open-source app framework used for creating and sharing beautiful, custom web apps for machine learning and data science.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Place your diary text files inside the `assets/diary` folder.
5. No additional configuration required.
6. Run the script using `streamlit run main.py`.

## Usage
1. **Run the Application**:
   - Execute the script using `streamlit run main.py` in your terminal.

2. **Diary Tone Analysis**:
   - **Prepare Your Files**: Ensure your diary entries are saved as text files with the `.txt` extension.
   - **Naming Convention**: Name your diary files in the format `YYYY-MM-DD.txt` (e.g., `2023-10-21.txt`). This format is important because the application extracts the date from the filename to visualize the sentiment over time.
   - **Upload Files**: In the sidebar, navigate to "Diary Tone Analysis" and upload your diary files.
   - **View Analysis**: The application will analyze the sentiment of each diary entry and display the positivity and negativity trends over time.
   - **Gain Insights**: Explore the positivity and negativity trends of your diary over time to gain insights into your emotional journey.

3. **PDF eBook Tone Analysis**:
   - **Upload PDF**: In the sidebar, navigate to "PDF eBook Tone Analysis" and upload your PDF eBook.
   - **View Analysis**: The application will extract the text from the PDF and analyze its sentiment.
   - **Sentiment Scores**: Sentiment scores for the entire eBook will be displayed, showing the overall positivity, negativity, neutrality, and compound score.
   - **Demonstration eBook**: A PDF eBook has been provided for demonstration purposes in the `assets/ebook` directory. You can use this eBook to see how the analysis works.

4. **Navigation**:
   - **Sidebar Navigation**: Use the sidebar to navigate between "Home", "Diary Tone Analysis", and "PDF eBook Tone Analysis".
   - **Home Page**: The "Home" page provides an overview and options to choose between diary or eBook analysis.

5. **Gain Insights**:
   - **Diary Insights**: Understand the emotional trends in your diary entries over time.
   - **eBook Insights**: Analyze the overall emotional tone of your eBooks to understand their sentiment.

By following these steps, you can effectively use the ToneAnalyzer to analyze and visualize the emotional tone of both your diary entries and eBooks.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.