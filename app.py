import streamlit as st  

# Streamlit App Title  
st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")  

# Custom Styling  
st.markdown(
    """
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stTextInput, .stNumberInput, .stButton>button {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
        }
    </style>
    
    """, 
    unsafe_allow_html=True
)

# Title and Description  
st.title("📏 Modern Unit Converter")  
st.subheader("Convert *Meters* to *Centimeters* Easily")  

# Input Field for Meters  
meters = st.number_input("Enter value in meters:", min_value=0.0, format="%.2f")  

# Convert Button  
if st.button("Convert to Centimeters 🚀"):  
    cm = meters * 100  
    st.success(f"{meters} meters is *{cm} centimeters*")