import streamlit as st
import time
from PIL import Image

def show_loader():
    with st.spinner("Loading..."):
        time.sleep(2)  # Simulates loading time

def home_page():
    st.title("Welcome to Face Detection App")
    
    st.markdown(
        """
        <style>
        .home-title {
            text-align: center;
            color: #ff6347;
            font-size: 2.8rem;
            margin-top: 20px;
            font-weight: bold;
        }
        .home-header {
            text-align: center;
            color: #4b4b4b;
            font-size: 1.8rem;
            margin-bottom: 20px;
        }
        .home-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 15px;
            max-width: 100%;
        }
        .home-text {
            text-align: center;
            color: #555555;
            font-size: 1.2rem;
            margin-top: 20px;
            line-height: 1.6;
        }
        .home-content {
            text-align: center;
            margin-top: 20px;
        }
        .home-button {
            display: inline-block;
            padding: 10px 20px;
            margin-top: 20px;
            font-size: 1.2rem;
            color: white;
            background-color: #ff6347;
            border-radius: 5px;
            text-decoration: none;
            border: none;
        }
        .home-button:hover {
            background-color: #e55347;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<h1 class="home-title">Welcome to Face Detection App</h1>', unsafe_allow_html=True)
    
    st.image("https://via.placeholder.com/800x300?text=Face+Detection+App", caption="Face Detection App", use_column_width=True)
    
    st.markdown(
        '''
        <div class="home-text">
        This app leverages advanced technology to detect and analyze faces in images with high accuracy.
        <br><br>
        You can upload images for detection, view results, and explore detailed analytics.
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '''
        <div class="home-content">
        <h2 class="home-header">Features:</h2>
        <ul>
            <li>🔍 **Accurate Face Detection**: Detect faces with high precision.</li>
            <li>📈 **Real-time Analysis**: Get instant feedback on uploaded images.</li>
            <li>📊 **Detailed Results**: Explore comprehensive results and analytics.</li>
        </ul>
        <h2 class="home-header">How to Use:</h2>
        <p>Use the sidebar to navigate through the app and start detecting faces.</p>
        <a href="https://example.com" target="_blank" class="home-button">Learn More</a>
        </div>
        ''',
        unsafe_allow_html=True
    )

def predict_page():
    st.title("Face Detection Prediction")
    st.write("This page will allow users to upload images for face detection.")

def result_page():
    st.title("Detection Results")
    st.write("This page will show the results of face detection.")

def analytics_page():
    st.title("Analytics")
    st.write("This page will provide analytics and visualizations.")

def main():
    # Set page configuration
    st.set_page_config(page_title="Face Detection App", layout="wide", initial_sidebar_state="expanded")
    
    # Sidebar styling
    st.markdown(
        """
        <style>
        .sidebar {
            background-color: #282c34;
            color: #ffffff;
        }
        .sidebar .sidebar-content {
            padding: 2rem;
        }
        .sidebar a {
            color: #61dafb;
            text-decoration: none;
        }
        .sidebar a:hover {
            text-decoration: underline;
        }
        .sidebar .sidebar-menu {
            font-size: 1.2rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar navigation
    page = st.sidebar.radio("Navigate", ["Home", "Predict", "Result", "Analytics"], key="sidebar")

    show_loader()

    if page == "Home":
        home_page()
    elif page == "Predict":
        predict_page()
    elif page == "Result":
        result_page()
    elif page == "Analytics":
        analytics_page()

if __name__ == "__main__":
    main()
