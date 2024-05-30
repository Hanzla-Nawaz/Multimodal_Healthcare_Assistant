import streamlit as st
import os
import openai

# Set page configuration
st.set_page_config(
    page_title="Multimodal Health Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate responses using GPT-4o
def generate_response(query):
    response = openai.Completion.create(
        model="gpt-4o",
        prompt=query,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Define sidebar navigation and page title
st.sidebar.title("Navigation")
st.sidebar.markdown("Welcome to Multimodal Health Assistant Chatbot")

# Function for Symptom Checker with voice and video inputs
def symptom_checker():
    st.markdown('<div class="background-symptom-checker">', unsafe_allow_html=True)
    st.subheader("Symptom Checker")
    st.markdown("Please provide details about your symptoms:")

    # Text input
    symptom_input = st.text_area("Symptoms (Text)", "")

    # Voice input
    st.write("Symptoms (Voice):")
    voice_symptom = st.file_uploader("Upload voice recording (WAV format)", type=["wav"])

    # Video input
    st.write("Symptoms (Video):")
    video_symptom = st.file_uploader("Upload video recording (MP4 format)", type=["mp4"])

    if st.button("Check Symptoms"):
        query = "Symptom checker:"
        if symptom_input:
            query += f" Text: {symptom_input}"
        if voice_symptom:
            query += f" Voice: {voice_symptom.name}"
        if video_symptom:
            query += f" Video: {video_symptom.name}"

        if query != "Symptom checker:":
            response = generate_response(query)
            st.success(response)
        else:
            st.warning("Please provide symptoms.")
    st.markdown('</div>', unsafe_allow_html=True)

# Function for Medical Image Analysis
def image_analysis():
    st.markdown('<div class="background-medical-image">', unsafe_allow_html=True)
    st.subheader("Medical Image Analysis")
    uploaded_image = st.file_uploader("Upload Medical Image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
    if st.button("Analyze Image"):
        if uploaded_image:
            # Process the uploaded image (You can add AI-powered analysis here)
            st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
        else:
            st.warning("Please upload a medical image.")
    st.markdown('</div>', unsafe_allow_html=True)

# Function for Consultation Summaries
def consultation_summaries():
    st.markdown('<div class="background-consultation">', unsafe_allow_html=True)
    st.subheader("Consultation Summaries")
    consultation_input = st.text_area("Enter consultation details:", "")
    if st.button("Generate Summary"):
        if consultation_input:
            query = f"Consultation summary: {consultation_input}"
            response = generate_response(query)
            st.success(response)
        else:
            st.warning("Please enter consultation details.")
    st.markdown('</div>', unsafe_allow_html=True)

# Function for Patient Support
def patient_support():
    st.markdown('<div class="background-patient-support">', unsafe_allow_html=True)
    st.subheader("Patient Support")
    question_input = st.text_area("Ask a question:", "")
    if st.button("Get Support"):
        if question_input:
            query = f"Patient support: {question_input}"
            response = generate_response(query)
            st.success(response)
        else:
            st.warning("Please ask a question.")
    st.markdown('</div>', unsafe_allow_html=True)

# Main function to run the application
def main():
    st.markdown('<div class="background">', unsafe_allow_html=True)
    st.title("Multimodal Health Assistant Chatbot")
    selected_option = st.sidebar.selectbox("Select an Option", ["Symptom Checker", "Medical Image Analysis", "Consultation Summaries", "Patient Support"])

    if selected_option == "Symptom Checker":
        symptom_checker()
    elif selected_option == "Medical Image Analysis":
        image_analysis()
    elif selected_option == "Consultation Summaries":
        consultation_summaries()
    elif selected_option == "Patient Support":
        patient_support()
    st.markdown('</div>', unsafe_allow_html=True)

# Execute the main function
if __name__ == "__main__":
    main()