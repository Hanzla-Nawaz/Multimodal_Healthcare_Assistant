# Multimodal Health Assistant

Welcome to the Multimodal Health Assistant, a sophisticated Streamlit-based chatbot application designed to assist with various healthcare needs. This assistant utilizes GPT-4 to provide insights and support for symptom checking, medical image analysis, consultation summaries, and patient support.

## Features

- **Symptom Checker**: Input symptoms via text, voice, or video, and get professional insights.
- **Medical Image Analysis**: Upload medical images and receive analysis.
- **Consultation Summaries**: Enter consultation details to generate concise summaries.
- **Patient Support**: Ask health-related questions and get expert advice.

## Installation

To set up the Multimodal Health Assistant on your local machine, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/multimodal-health-assistant.git
    cd multimodal-health-assistant
    ```

2. **Install Dependencies**:
    Ensure you have Python 3.7 or higher. Install the required packages using pip:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up OpenAI API Key**:
    Obtain an API key from OpenAI and set it as an environment variable:
    ```sh
    export OPENAI_API_KEY='your-openai-api-key'
    ```

4. **Run the Application**:
    Launch the Streamlit application:
    ```sh
    streamlit run app.py
    ```

## Usage

Navigate through the application using the sidebar. Choose between Symptom Checker, Medical Image Analysis, Consultation Summaries, and Patient Support. Each section provides a user-friendly interface for input and interaction.

### Symptom Checker
1. Provide symptoms via text, upload a voice recording (WAV format), or upload a video (MP4 format).
2. Click "Check Symptoms" to get an analysis.

### Medical Image Analysis
1. Upload a medical image in JPG, JPEG, or PNG format.
2. Click "Analyze Image" to process and display the analysis.

### Consultation Summaries
1. Enter the details of your consultation in the provided text area.
2. Click "Generate Summary" to get a concise summary.

### Patient Support
1. Type your health-related question in the text area.
2. Click "Get Support" to receive advice and answers.

