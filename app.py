import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Portfolio | Jon Daniel",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
def local_css():
    css = """
    <style>
    /* Main container styling */
    .main {
        background-color: #0f121a;
        color: white;
    }
    
    /* Custom container */
    .custom-container {
        background-color: #7b68ee;
        border-radius: 10px;
        padding: 30px;
        color: white;
    }
    
    /* Profile image */
    .profile-img {
        border-radius: 50%;
        width: 220px;
        height: 220px;
        background-color: #f8d0ff;
        border: 5px solid white;
        margin: 0 auto;
        display: block;
    }
    
    /* Text styles */
    .header-text {
        font-size: 5rem;
        font-weight: 900;
        color: white;
    }
    
    .name-text {
        font-size: 3.5rem;
        font-weight: 700;
        line-height: 1.2;
        margin-top: 20px;
    }
    
    .first-name {
        font-weight: 300;
        font-size: 2.5rem;
    }
    
    /* Card styles */
    .card {
        border-radius: 10px;
        padding: 20px;
        height: 100%;
        position: relative;
        margin-bottom: 15px;
    }
    
    .stat-card {
        padding: 20px;
        border-radius: 10px;
        color: white;
        height: 100%;
    }
    
    .mint-bg {
        background-color: #a0e4df;
    }
    
    .purple-bg {
        background-color: #9370db;
    }
    
    .dark-bg {
        background-color: #333;
    }
    
    .orange-bg {
        background-color: #ffa500;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .navigation {
        margin-bottom: 30px;
    }
    
    .nav-item {
        padding: 8px 16px;
        color: rgba(255, 255, 255, 0.7);
        text-transform: uppercase;
        font-size: 0.8rem;
        display: inline-block;
        margin-right: 10px;
    }
    
    .nav-active {
        color: white;
        font-weight: bold;
    }
    
    .email-button {
        margin-top: 20px;
        border-bottom: 1px dashed rgba(255, 255, 255, 0.5);
        padding-bottom: 5px;
        display: inline-block;
    }
    
    .badge {
        background-color: black;
        color: white;
        padding: 15px;
        border-radius: 50%;
        display: inline-block;
        width: 80px;
        height: 80px;
        text-align: center;
        line-height: 1.2;
        font-size: 0.7rem;
        position: absolute;
        bottom: 30px;
        right: 30px;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Apply CSS
local_css()

# Main layout
col1, col2 = st.columns([1, 2])

# Left column - Profile
with col1:
    # Profile card with purple background
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    
    # Navigation bar (simplified to horizontal)
    st.markdown("""
    <div class="navigation">
        <span class="nav-item nav-active">Portfolio</span>
        <span class="nav-item">Research</span>
        <span class="nav-item">Clients</span>
        <span class="nav-item">Podcast</span>
    </div>
    """, unsafe_allow_html=True)
    
    # About Me section
    st.markdown('<div style="margin-bottom: 10px;">About Me</div>', unsafe_allow_html=True)
    
    # Profile image - using Streamlit's image component
    st.markdown('<img src="https://via.placeholder.com/220" class="profile-img">', unsafe_allow_html=True)
    
    # Name section
    st.markdown("""
    <div class="name-text">
        <div class="first-name">I'm,</div>
        Jon<br>Daniel
    </div>
    """, unsafe_allow_html=True)
    
    # Email contact
    st.markdown('<div class="email-button">inquiry@jondaniel.design</div>', unsafe_allow_html=True)
    
    # Badge
    st.markdown('<div class="badge">WE CODE WITH PASSION</div>', unsafe_allow_html=True)
    
    # Close container
    st.markdown('</div>', unsafe_allow_html=True)

# Right column - Portfolio content
with col2:
    # Portfolio header
    st.markdown('<h1 class="header-text">Portfolio</h1>', unsafe_allow_html=True)
    
    # Top row
    top_col1, top_col2 = st.columns([3, 1])
    
    with top_col1:
        # Feature image/project
        st.image("https://via.placeholder.com/800x250/ff9a8b/ffffff", use_column_width=True)
    
    with top_col2:
        # Stats cards
        st.markdown("""
        <div class="stat-card mint-bg">
            <div class="stat-number">251</div>
            <div>Projects</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="stat-card purple-bg" style="margin-top: 15px;">
            <div class="stat-number">156</div>
            <div>Awards</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Bottom row
    bot_col1, bot_col2 = st.columns([1, 2])
    
    with bot_col1:
        # Client card
        st.markdown("""
        <div class="stat-card dark-bg">
            <div style="font-size: 36px; text-align: center; margin: 10px 0;">⌘</div>
            <div style="position: absolute; bottom: 20px;">Clients</div>
        </div>
        """, unsafe_allow_html=True)
    
    with bot_col2:
        # Using a single HTML block instead of nested columns
        st.markdown("""
        <div style="display: flex; gap: 15px;">
            <div style="flex: 1; background-color: black; border-radius: 10px; height: 140px; display: flex; align-items: center; justify-content: center;">
                <div style="width: 60px; height: 60px; background: linear-gradient(45deg, #ff6b6b, #6b77ff); border-radius: 50%;"></div>
            </div>
            <div style="flex: 1;" class="stat-card orange-bg">
                <div class="stat-number">172</div>
                <div>Global Design<br>Awards</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
