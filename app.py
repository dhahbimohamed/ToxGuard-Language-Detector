import streamlit as st
import joblib
import re

# Load model
model = joblib.load("hate_speech_model.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|@\w+|#\w+|[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Set page config with gaming style
st.set_page_config(
    page_title="ToxGuard - Gaming Content Moderation",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Gaming-inspired CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oxanium:wght@400;600;700&family=Rajdhani:wght@500;600;700&display=swap');
    
    :root {
        --primary: #6e40ff;
        --primary-light: #8d6aff;
        --danger: #ff4d6d;
        --warning: #ffaa00;
        --success: #00d4aa;
        --text-light: #ffffff;
        --text-lighter: rgba(255, 255, 255, 0.8);
        --bg-dark: #0f0f13;
        --section-bg: rgba(20, 20, 40, 0.6);
    }
    
    body {
        font-family: 'Oxanium', sans-serif;
        background-color: var(--bg-dark);
        color: var(--text-light);
        margin: 0;
        padding: 0;
    }
    
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    .feature-section {
        margin-bottom: 4rem;
    }
    
    .section-title {
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        color: var(--text-light);
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
    }
    
    .section-title:after {
        content: '';
        position: absolute;
        width: 60px;
        height: 4px;
        bottom: -10px;
        left: 0;
        background: var(--primary);
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .feature-card {
        background: var(--section-bg);
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid var(--primary);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(110, 64, 255, 0.3);
    }
    
    .feature-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: var(--primary-light);
    }
    
    .feature-desc {
        font-size: 0.95rem;
        color: var(--text-lighter);
        line-height: 1.6;
    }
    
    .analysis-section {
        display: flex;
        gap: 3rem;
        margin-bottom: 4rem;
    }
    
    .analysis-content {
        flex: 1;
    }
    
    .stTextArea textarea {
        background: rgba(30, 30, 60, 0.7) !important;
        color: var(--text-light) !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        padding: 1.2rem !important;
        font-size: 1rem !important;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.8rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(110, 64, 255, 0.4) !important;
    }
    
    .result-box {
        padding: 1.5rem;
        border-radius: 8px;
        margin-top: 1.5rem;
        font-weight: 600;
        font-size: 1.1rem;
        background: rgba(30, 30, 60, 0.7);
        border-left: 4px solid;
    }
    
    .hate {
        border-color: var(--danger);
        color: var(--danger);
    }
    
    .offensive {
        border-color: var(--warning);
        color: var(--warning);
    }
    
    .neutral {
        border-color: var(--success);
        color: var(--success);
    }
    
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding-top: 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        color: var(--text-lighter);
        font-size: 0.9rem;
    }
    
    @media (max-width: 768px) {
        .analysis-section {
            flex-direction: column;
        }
        
        .section-title {
            font-size: 2rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main container
st.markdown("""<div class="main-container">""", unsafe_allow_html=True)

# Feature section
st.markdown("""<div class="feature-section">""", unsafe_allow_html=True)
st.markdown("""<div class="section-title">ToxGuard Features</div>""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-title">Real-time Analysis</div>
            <div class="feature-desc">
                Instantly scans gaming chats for toxic content with high accuracy, 
                keeping your community safe during gameplay.
            </div>
        </div>
        <div class="feature-card">
            <div class="feature-title">Advanced Detection</div>
            <div class="feature-desc">
                Trained on millions of gaming interactions to understand gaming-specific 
                slang and context across multiple languages.
            </div>
        </div>
        <div class="feature-card">
            <div class="feature-title">Community Shield</div>
            <div class="feature-desc">
                Flags harmful content while allowing healthy competitive banter, 
                maintaining the perfect gaming atmosphere.
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("""</div>""", unsafe_allow_html=True)

# Analysis section
st.markdown("""<div class="analysis-section">""", unsafe_allow_html=True)

# Content Analysis
st.markdown("""<div class="analysis-content">""", unsafe_allow_html=True)
st.markdown("""<div class="section-title">Content Analysis</div>""", unsafe_allow_html=True)

# User input
user_input = st.text_area("Enter gaming chat to analyze", height=180, 
                         placeholder="Paste game chat or message to scan for toxicity...")

if st.button("Analyze Chat"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze")
    else:
        cleaned = clean_text(user_input)
        prediction = model.predict([cleaned])[0]

        labels = {
            0: "Toxic Speech Detected",
            1: "Offensive Language",
            2: "Clean Chat"
        }

        classes = {
            0: "hate",
            1: "offensive",
            2: "neutral"
        }

        st.markdown(
            f"<div class='result-box {classes[prediction]}'>{labels[prediction]}</div>",
            unsafe_allow_html=True
        )

        # Additional feedback
        if prediction == 0:
            st.markdown("<p style='color: var(--text-lighter);'>This content violates gaming community standards.</p>", unsafe_allow_html=True)
        elif prediction == 1:
            st.markdown("<p style='color: var(--text-lighter);'>This language may offend other players.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: var(--text-lighter);'>This chat is appropriate for gaming.</p>", unsafe_allow_html=True)

st.markdown("""</div>""", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        <p>© 2025 ToxGuard | Created by Dhahbi Mohamed</p>
        <p>keep gaming communities safe and respectfull</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""</div>""", unsafe_allow_html=True)  # Close main-container
