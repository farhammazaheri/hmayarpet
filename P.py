import streamlit as st
from openai import OpenAI

# API Key Setup
Api_key = "tpsg-me7QIY0nhv36LVYz6b5NpFBWVczObI3"

# Custom CSS Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    :root {
        --primary: #4A90E2;
        --secondary: #6C5CE7;
        --accent: #FF7D4D;
        --background: #F8F9FA;
        --text: #2D3436;
    }
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    body {
        background-color: var(--background);
    }
    
    .stRadio > div {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stButton button {
        background: var(--primary) !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 12px 24px !important;
        transition: all 0.3s !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(74,144,226,0.3);
    }
    
    .response-box {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        margin: 20px 0;
        border-left: 4px solid var(--primary);
    }
    
    .feature-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        margin: 15px 0;
    }
    
    .footer {
        text-align: center;
        padding: 20px;
        color: white;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        margin-top: 40px;
        border-radius: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Client Initialization for OpenAI
client = OpenAI(base_url="https://api.metisai.ir/openai/v1", api_key=Api_key)

# Sidebar Navigation
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/616/616430.png", width=80)
selected_view = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🍽 Meal Plan", "📚 Education", "🩺 Medical Advice", "⚕️ Vet Support"],
    help="Select your desired service"
)

# Main Content Area
st.title("🐾 HamyarPet - همیار پت")
st.markdown("<h3 style='text-align: center; color: var(--text); margin-bottom: 30px;'>Your Smart AI Assistant for Pet Wellness</h3>", unsafe_allow_html=True)

# Home View
if selected_view == "🏠 Home":
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
            <div class="feature-card">
                <h3 style='color: var(--primary);'>🌟 Premium Features</h3>
                <ul style='list-style: none; padding-left: 0;'>
                    <li>✅ Advanced meal planning</li>
                    <li>✅ Priority vet support</li>
                    <li>✅ Detailed health analytics</li>
                    <li>✅ Emergency care guides</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="feature-card">
                <h3 style='color: var(--secondary);'>✨ Free Features</h3>
                <ul style='list-style: none; padding-left: 0;'>
                    <li>✅ Basic meal plans</li>
                    <li>✅ General pet care tips</li>
                    <li>✅ Community support</li>
                    <li>✅ Educational resources</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="feature-card">
            <h3 style='text-align: center;'>📈 Pricing Plans</h3>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;'>
                <div style='padding: 20px; border-radius: 10px; background: #E3F2FD;'>
                    <h4>Free Plan</h4>
                    <p>Start your pet care journey</p>
                    <h2 style='color: var(--primary);'>$0/mo</h2>
                </div>
                <div style='padding: 20px; border-radius: 10px; background: #EDE7F6;'>
                    <h4>Premium Plan</h4>
                    <p>Advanced care features</p>
                    <h2 style='color: var(--secondary);'>$9.99/mo</h2>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Meal Plan View
elif selected_view == "🍽 Meal Plan":
    st.markdown("<h2 style='color: var(--text);'>🍽 AI-Powered Meal Plan</h2>", unsafe_allow_html=True)
    
    with st.form("meal_plan_form"):
        col1, col2 = st.columns(2)
        with col1:
            pet_name = st.text_input("Pet's Name 🐶")
            pet_age = st.number_input("Age (years) 🎂", min_value=0)
        with col2:
            pet_type = st.selectbox("Pet Type 🐾", ["Dog", "Cat", "Bird", "Other"])
            pet_weight = st.number_input("Weight (kg) ⚖️", min_value=0.0)
        
        plan_type = st.radio("Plan Type 💎", ["Free", "Premium"], horizontal=True)
        submitted = st.form_submit_button("Generate Meal Plan 🚀")
        
    if submitted:
        with st.spinner("🧠 Creating the perfect meal plan..."):
            plan_details = f"{plan_type} meal plan for a {pet_type} named {pet_name}, aged {pet_age} years, weighing {pet_weight} kg."
           try:
                response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": plan_details}],
                timeout=60)            
                meal_plan = response.choices[0].message.content
               
                except Exception as e:
                
                    meal_plan = f"❌ An error occurred while generating the meal plan: {str(e)}"

            st.markdown(f"""
                <div class="response-box">
                    <h4 style='color: var(--primary);'>🍗 Meal Plan for {pet_name}</h4>
                    <div style='margin-top: 15px;'>{meal_plan}</div>
                </div>
            """, unsafe_allow_html=True)

# Pet Education View
elif selected_view == "📚 Education":
    st.markdown("<h2 style='color: var(--text);'>📚 Pet Education Hub</h2>", unsafe_allow_html=True)
    
    with st.form("education_form"):
        query = st.text_area("Ask your pet care question ❓", height=150)
        submitted = st.form_submit_button("Get Expert Advice 🦉")
        
    if submitted and query:
        with st.spinner("🔍 Searching for the best answers..."):
            response2 = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": query}]
                stream=True
            )
            education_response = response2.choices[0].message.content
            st.markdown(f"""
                <div class="response-box">
                    <h4 style='color: var(--secondary);'>📖 Expert Advice</h4>
                    <div style='margin-top: 15px;'>{education_response}</div>
                </div>
            """, unsafe_allow_html=True)

# Medical Advice View
elif selected_view == "🩺 Medical Advice":
    st.markdown("<h2 style='color: var(--text);'>🩺 AI-Powered Medical Insights</h2>", unsafe_allow_html=True)
    
    with st.form("medical_form"):
        health_issue = st.text_area("Describe your pet's symptoms 🩹", height=150)
        submitted = st.form_submit_button("Get Medical Advice 💊")
        
    if submitted and health_issue:
        with st.spinner("⏳ Analyzing symptoms..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": f"Provide advice for: {health_issue}"}]
            )
            medical_response = response.choices[0].message.content
            st.markdown(f"""
                <div class="response-box">
                    <h4 style='color: var(--primary);'>📋 Medical Report</h4>
                    <div style='margin-top: 15px;'>{medical_response}</div>
                </div>
            """, unsafe_allow_html=True)

# Vet Support View
elif selected_view == "⚕️ Vet Support":
    st.markdown("<h2 style='color: var(--text);'>⚕️ 24/7 Veterinary Support</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="feature-card">
            <div style='text-align: center; padding: 30px;'>
                <h3 style='color: var(--accent);'>🚀 Coming Soon!</h3>
                <p>Our team of certified veterinarians is getting ready to assist you 24/7!</p>
                <div style='margin: 20px 0;'>⏳</div>
                <p>Subscribe to our newsletter for updates:</p>
                <input type="email" placeholder="Enter your email" style='padding: 10px; border-radius: 25px; border: 1px solid #ddd; width: 60%; margin: 10px auto;'>
                <button style='background: var(--primary); color: white; border: none; padding: 10px 25px; border-radius: 25px; margin: 10px;'>Notify Me</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>🌟 HamyarPet | Designed with ❤️ by Farham | Powered by AI 🤖</p>
        <div style='margin-top: 10px;'>
            <small>📧 support@hamyarpet.com | 📱 +98 123 456 7890</small>
        </div>
    </div>
""", unsafe_allow_html=True)
