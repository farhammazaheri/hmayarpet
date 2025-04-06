import streamlit as st
from openai import OpenAI

# API Key Setup
Api_key = "tpsg-me7QIY0nhv36LVYz6b5NpFBWVczObI3"

# Main App Title and Introduction
st.title("🐾 HamyarPet - همیار پت")
st.markdown("<h2 style='color:#4A90E2;text-align:center;'>Your Smart AI Assistant for Pet Wellness</h2>", unsafe_allow_html=True)
st.markdown("""
    <div style='background-color:#F5F5F5;padding:20px;border-radius:10px;text-align:center;'>
        🌟 Explore tailored solutions for your pet's health, education, and wellness. 
        Choose between <b>Free</b> or <b>Premium</b> plans for advanced features.
    </div>
""", unsafe_allow_html=True)

# Navigation Menu
selected_view = st.radio("Navigate through the features below:", [
    "Home",
    "Meal Plan (Free & Premium)",
    "Pet Education",
    "24/7 Vet Support",
    "Medical Advice"
])

# Client Initialization for OpenAI
client = OpenAI(base_url="https://api.metisai.ir/openai/v1", api_key=Api_key)

# Home View
if selected_view == "Home":
    st.markdown("<h2 style='color:#4A90E2;'>Welcome to HamyarPet</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color:#FFF3E6;padding:20px;border-radius:10px;">
            HamyarPet empowers you with personalized AI solutions to improve pet care and education. 
            Upgrade to <b>Premium</b> for in-depth insights and exclusive features.
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<h3>Pricing Plans</h3>", unsafe_allow_html=True)
    st.markdown("""
        <ul style="list-style-type:disc;padding-left:20px;">
            <li><b>Free:</b> Access basic meal plans and general pet advice.</li>
            <li><b>Premium:</b> Unlock advanced meal plans, 24/7 vet consultations, and detailed medical insights.</li>
        </ul>
    """, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

# Meal Plan View
elif selected_view == "Meal Plan (Free & Premium)":
    st.markdown("<h2 style='color:#4A90E2;'>🍽 AI-Powered Meal Plan</h2>", unsafe_allow_html=True)
    plan_type = st.radio("Select Plan Type:", ["Free", "Premium"])
    pet_name = st.text_input("Pet's Name:")
    pet_age = st.number_input("Pet's Age (in years):", min_value=0)
    pet_weight = st.number_input("Pet's Weight (in kg):", min_value=0.0)
    pet_type = st.selectbox("Pet Type:", ["Dog", "Cat", "Bird", "Other"])

    if st.button("Generate Meal Plan"):
        plan_details = f"{plan_type} meal plan for a {pet_type} named {pet_name}, aged {pet_age} years, weighing {pet_weight} kg."
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": plan_details}]
        )
        meal_plan = response.choices[0].message.content
        st.markdown(f"<div style='background-color:#E0F7FA;padding:15px;border-radius:10px;'>"
                    f"**Meal Plan for {pet_name}:**\n{meal_plan}</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

# Pet Education View
elif selected_view == "Pet Education":
    st.markdown("<h2 style='color:#4A90E2;'>📚 Pet Education (Interactive Chat)</h2>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:#F9F9F9;padding:15px;border-radius:10px;'>Ask questions about pet care and training.</div>", unsafe_allow_html=True)
    query = st.text_area("Type your question:")
    if st.button("Get Educational Advice"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": query}]
        )
        education_response = response.choices[0].message.content
        st.markdown(f"<div style='background-color:#E0F7FA;padding:15px;border-radius:10px;'>**Advice:**\n{education_response}</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

# 24/7 Vet Support View
elif selected_view == "24/7 Vet Support":
    st.markdown("<h2 style='color:#4A90E2;'>🕒 24/7 Vet Support</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color:#F9F9F9;padding:20px;border-radius:10px;">
            This feature is under development. Soon, you’ll have real-time access to veterinary experts for personalized pet consultations.
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

# Medical Advice View
elif selected_view == "Medical Advice":
    st.markdown("<h2 style='color:#4A90E2;'>💊 Medical Advice</h2>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:#FFF3E6;padding:15px;border-radius:10px;'>Provide your pet's symptoms to get detailed insights and advice.</div>", unsafe_allow_html=True)
    health_issue = st.text_area("Describe your pet's health concern:")
    if st.button("Get Medical Insights"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Provide advice for: {health_issue}"}]
        )
        medical_response = response.choices[0].message.content
        st.markdown(f"<div style='background-color:#E0F7FA;padding:15px;border-radius:10px;'>**Medical Advice:**\n{medical_response}</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background: #4A90E2;
        color: white;
        text-align: center;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    <div class="footer">
        🌟 HamyarPet | Designed by Farham | Powered by AI 🌟
    </div>
""", unsafe_allow_html=True)