from ollama import Client
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
ollama_host = os.getenv("ollama_host")

client = Client(host=ollama_host)
model = "qwen2.5:14b"

def main():
    st.set_page_config(
        page_title="SafeSpace",
        page_icon="🌟",
        layout="wide"
    )
    
    st.title("SafeSpace - Your Mental Health Companion")
    
    # Navigation
    tab1, tab2, tab3 = st.tabs([
        "💭 Supportive Chat",
        "📔 Guided Journal",
        "🤝 Community"
    ])

    # Footer with crisis resources
    st.markdown("---")
    with st.expander("Crisis Resources", expanded=False):
        st.markdown("""
        ### Crisis Resources (India)
        
        **1. National Helpline:**
        - **Number:** 9152987821
        - **Service:** 24/7 mental health support and counseling.
        
        **2. Snehi:**
        - **Number:** 91-22-2772 6771
        - **Service:** Emotional support and mental health counseling.
        
        **3. iCALL:**
        - **Number:** 9152987821
        - **Service:** Free and confidential mental health counseling via phone, email, and chat.
        
        **4. AASRA:**
        - **Number:** 91-22-2772 6771
        - **Service:** 24/7 helpline for individuals in distress.
        
        **5. Vandrevala Foundation:**
        - **Number:** 9999666555
        - **Service:** 24/7 mental health helpline.
        
        **6. Fortis Stress Helpline:**
        - **Number:** 08376804102
        - **Service:** 24/7 helpline for stress and mental health issues.
        
        **7. COOJ Mental Health Foundation:**
        - **Number:** 91-832-2252525
        - **Service:** Helpline for emotional support and suicide prevention.
        
        **8. The MINDS Foundation:**
        - **Website:** [mindsfoundation.org](https://www.mindsfoundation.org)
        - **Service:** Mental health education and support.
        
        **9. YourDOST:**
        - **Website:** [yourdost.com](https://www.yourdost.com)
        - **Service:** Online counseling and emotional support.
        
        **10. Manas Foundation:**
        - **Website:** [manas.org](https://www.manas.org)
        - **Service:** Mental health awareness and support.
        """)

if __name__ == "__main__":
    main()