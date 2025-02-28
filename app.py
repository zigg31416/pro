import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Portfolio | Jon Daniel",
    page_icon="🎨",
    layout="wide"
)

# Custom CSS for styling
def local_css():
    css = """
    <style>
    /* Main container styling */
    .main {
        background-color: #0f121a;
        padding: 0;
        color: white;
    }
    
    /* Portfolio card styling */
    .portfolio-container {
        background-color: #0f121a;
        border-radius: 15px;
        padding: 20px;
        margin: 20px auto;
        max-width: 1200px;
    }
    
    /* Profile section styling */
    .profile-section {
        background-color: #7b68ee;
        border-radius: 10px;
        padding: 20px;
        color: white;
        position: relative;
    }
    
    .profile-image-container {
        background-color: #f8d0ff;
        border-radius: 50%;
        width: 220px;
        height: 220px;
        margin: 0 auto;
        overflow: hidden;
        border: 5px solid white;
        text-align: center;
    }
    
    .name-text {
        font-size: 3.5rem;
        font-weight: 600;
        line-height: 1;
        margin-top: 20px;
    }
    
    .first-name {
        font-weight: 300;
        font-size: 2.5rem;
    }
    
    /* Portfolio grid styling */
    .portfolio-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin-top: 15px;
    }
    
    .portfolio-item {
        border-radius: 10px;
        overflow: hidden;
        position: relative;
    }
    
    .stat-card {
        border-radius: 10px;
        padding: 20px;
        color: white;
        position: relative;
        height: 100%;
    }
    
    .stat-number {
        font-size: 2.8rem;
        font-weight: 700;
    }
    
    .stat-label {
        font-size: 1.2rem;
    }
    
    .mint-card {
        background-color: #a0e4df;
    }
    
    .purple-card {
        background-color: #9370db;
    }
    
    .dark-card {
        background-color: #333;
        color: white;
    }
    
    .orange-card {
        background-color: #ffa500;
    }
    
    .corner-icon {
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 1.5rem;
    }
    
    .vertical-nav {
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        display: flex;
        flex-direction: column;
        gap: 20px;
        padding-left: 10px;
    }
    
    .nav-item {
        writing-mode: vertical-rl;
        transform: rotate(180deg);
        text-transform: uppercase;
        font-size: 0.8rem;
        letter-spacing: 1px;
        color: white;
        opacity: 0.7;
        transition: opacity 0.3s;
    }
    
    .nav-item:hover {
        opacity: 1;
        cursor: pointer;
    }
    
    .active-nav {
        opacity: 1;
        font-weight: bold;
    }
    
    /* Email button styling */
    .email-button {
        margin-top: 20px;
        border-bottom: 1px dashed rgba(255, 255, 255, 0.5);
        padding-bottom: 5px;
        display: inline-block;
    }
    
    /* Round badge styling */
    .round-badge {
        position: absolute;
        bottom: 30px;
        right: 30px;
        width: 80px;
        height: 80px;
        background-color: black;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 0.7rem;
        text-align: center;
        padding: 10px;
    }
    
    /* Media queries for responsive design */
    @media (max-width: 768px) {
        .portfolio-grid {
            grid-template-columns: 1fr;
        }
        
        .profile-section {
            flex-direction: column;
        }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Load the portfolio page
def load_portfolio():
    # Main container
    st.markdown('<div class="portfolio-container">', unsafe_allow_html=True)
    
    # Create a two-column layout
    col1, col2 = st.columns([1, 2])
    
    # Left column - Profile section
    with col1:
        with st.container():
            # Use Streamlit components instead of HTML
            st.markdown('<div class="profile-section">', unsafe_allow_html=True)
            
            # Navigation
            st.markdown('<div class="vertical-nav"><div class="nav-item active-nav">Portfolio</div><div class="nav-item">Research</div><div class="nav-item">Clients</div><div class="nav-item">Podcast</div></div>', unsafe_allow_html=True)
            
            # About Me section
            st.markdown('<div style="padding: 20px 0 20px 40px;">', unsafe_allow_html=True)
            st.markdown('<div style="margin-bottom: 10px;">About Me</div>', unsafe_allow_html=True)
            
            # Profile image container
            st.markdown('<div class="profile-image-container">', unsafe_allow_html=True)
            st.image("https://via.placeholder.com/220", width=220)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Name text
            st.markdown('<div class="name-text"><div class="first-name">I\'m,</div>Jon<br>Daniel</div>', unsafe_allow_html=True)
            
            # Email button
            st.markdown('<div class="email-button">inquiry@jondaniel.design</div>', unsafe_allow_html=True)
            
            # Round badge
            st.markdown('<div class="round-badge">WE CODE WITH PASSION</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Right column - Portfolio grid
    with col2:
        # Portfolio title
        st.markdown('<h1 style="font-size: 5rem; font-weight: 900; margin: 20px 0; color: white;">Portfolio</h1>', unsafe_allow_html=True)
        
        # Top row of portfolio grid
        col2_1, col2_2 = st.columns([3, 1])
        
        with col2_1:
            # Feature project
            st.image("https://via.placeholder.com/800x250/ff9a8b/ffffff", use_container_width=True)
            
        with col2_2:
            # Stats cards
            st.markdown('<div class="stat-card mint-card"><div class="stat-number">251</div><div class="stat-label">Projects</div><div class="corner-icon">↗</div></div>', unsafe_allow_html=True)
            st.markdown('<div class="stat-card purple-card" style="margin-top: 15px;"><div class="stat-number">156</div><div class="stat-label">Awards</div><div class="corner-icon">↗</div></div>', unsafe_allow_html=True)
        
        # Bottom row of portfolio grid
        col2_3, col2_4 = st.columns([1, 2])
        
        with col2_3:
            # Clients card
            st.markdown('<div class="stat-card dark-card"><div style="display: flex; align-items: center; justify-content: center; height: 100px;"><span style="font-size: 42px;">⌘</span></div><div style="position: absolute; bottom: 20px; left: 20px;">Clients</div><div class="corner-icon">↗</div></div>', unsafe_allow_html=True)
            
        with col2_4:
            # Global design awards section
            col2_4_1, col2_4_2 = st.columns(2)
            
            with col2_4_1:
                st.markdown('<div style="background-color: black; height: 100px; display: flex; align-items: center; justify-content: center; border-radius: 10px;"><div style="width: 60px; height: 60px; background: linear-gradient(45deg, #ff6b6b, #6b77ff); border-radius: 50%;"></div></div>', unsafe_allow_html=True)
                
            with col2_4_2:
                st.markdown('<div class="stat-card orange-card" style="height: 100px;"><div class="stat-number">172</div><div class="stat-label">Global Design Awards</div><div class="corner-icon">↗</div></div>', unsafe_allow_html=True)
    
    # Close the main container
    st.markdown('</div>', unsafe_allow_html=True)

# Apply CSS
local_css()

# Load the portfolio page
load_portfolio()

# Optional: Debugging information
if st.checkbox("Show debugging info", value=False):
    st.write("Streamlit version:", st.__version__)
    st.write("To customize this portfolio, edit the code to replace placeholder content with your own.")
