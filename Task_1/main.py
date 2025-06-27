import random
import streamlit as st
import re
class Hotelbot:
    def __init__(self):

       #To identify common patterns

        self.patterns ={
            "greeting": re.compile(r"\b(hello|hi|hey)\b", re.IGNORECASE),
            "farewell": re.compile(r"\b(bye|goodbye|see you)\b", re.IGNORECASE),
            "booking": re.compile(r"\b(room|available|book)\b", re.IGNORECASE),
            "room_pricing": re.compile(r"\b(price|cost|charges)\b", re.IGNORECASE),
            "facilities": re.compile(r"\b(service|services|wifi|pool|gym|breakfast)\b", re.IGNORECASE),
            "check": re.compile(r"\b(check-in|check-out|time)\b", re.IGNORECASE),
            "cancellation": re.compile(r"\b(cancel|cancellation)\b", re.IGNORECASE),
            "inquiry": re.compile(r"\b(contact|phone|email)\b", re.IGNORECASE)
        }
        
        #To provide responses based on identified patterns

        self.responses = {
            "greeting": ["Hi there! How can I assist you with your hotel booking today?",
                         "Hello! Welcome to our hotel booking service. How can I help you?",
                         "Hi! I'm here to assist you with your hotel needs. What can I do for you?"],
            "farewell": ["Goodbye! If you need any further assistance, feel free to reach out.",
                         "Thank you for chatting with us! Have a wonderful day ahead!","See you next time! If you have any more questions, don't hesitate to ask.",
                         "It was a pleasure assisting you! Have a great day!"],
            "booking": ["Sure! I can help you with that. What type of room are you looking for?",
                        "I can assist you with booking a room. What dates are you interested in?",
                        "Let's get started with your room booking. Can you provide the details?"],
            "room_pricing": ["Our room prices vary based on the type and season. Can you specify the dates?",
                             "The cost of our rooms depends on the type and availability. What dates are you looking at?",
                             "We have competitive pricing for our rooms. Can you tell me the dates you are interested in?",
                             "Our rooms start from ₹2500 per night."],
            "facilities": ["We offer various facilities including free Wi-Fi, a swimming pool, a gym, and complimentary breakfast.",
                           "Our hotel features a range of amenities such as Wi-Fi, a pool, a gym, and breakfast included.",
                           "You can enjoy our facilities like free Wi-Fi, a swimming pool, a gym, and breakfast during your stay."],
            "check": ["Check-in is at 3 PM and check-out is at 11 AM. Do you need help with anything else?",
                      "Check-in is from 2 PM. Check-out is until 11 AM.",
                      "You can check in after 2 PM and check out by 11 AM. Let me know if you need more information."],
            "cancellation": ["You can cancel your booking up to 24 hours before check-in without any charges.",
                             "Our cancellation policy allows you to cancel up to 24 hours before check-in without any fees.",
                             "You can cancel your booking without any charges up to 24 hours before check-in."],
            "inquiry": ["You can contact us at +123456789 or email us at support@hotel.com",
                        "You can contact us at 98765123XX or email info@xyzhotel.com.",
                        "For inquiries, you can reach us at +91-9876543210 or email us at inquiries@hotel.com"]
        }

    #function to respond to user input based on identified patterns

    def respond(self, user_input):
        user_input = user_input.lower()
        for key, pattern in self.patterns.items():
            if pattern.search(user_input):
                response = random.choice(self.responses[key])
                return response
        return "I'm sorry, I didn't understand that. Can you please rephrase your question?"
    
# Streamlit app to interact with the Hotelbot

st.set_page_config(page_title="Hotel Booking Assistant", page_icon="🏨")
st.title("Hotel Booking Assistant")
st.write("Welcome to the Hotel Booking Assistant! Type your query below:")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
user_input = st.text_input("Your query:")
if user_input:
    hotel = Hotelbot()
    response = hotel.respond(user_input)
    st.session_state.chat_history.append({"user": user_input, "bot": response})
    st.subheader("Chat History:")
    for chat in st.session_state.chat_history:
        st.write(f"User: {chat['user']}")
        st.write(f"Bot: {chat['bot']}")