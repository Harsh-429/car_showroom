# Expanded list of emotions
fear_emotions = ["panic", "terror", "apprehension", "dread", "unease", "worry", "phobia", "alarm", "nervousness", "horror",
                 "anxiety", "horror", "distress", "shock", "confusion"]

happy_emotions = ["joy", "gratitude", "hope", "love", "contentment", "happiness", "excitement", "satisfaction", "pride", "relief",
                  "euphoria", "delight", "elation", "cheer", "bliss"]

sad_emotions = ["melancholy", "grief", "heartache", "despair", "loneliness", "hopelessness", "mourning", "regret", "sorrow", "loss",
                "sadness", "misery", "anguish", "depression", "boredom"]

anger_emotions = ["rage", "wrath", "irritation", "fury", "disgust", "annoyance", "frustration", "resentment", "hostility", "outrage",
                  "indignation", "violence", "hatred", "vexation", "grudge"]

calm_emotions = ["peace", "serenity", "calmness", "relaxation", "tranquility", "soothing", "comfort", "satisfaction", "quietude", "content",
                 "balance", "composure", "repose", "ease", "harmony"]

# Function to respond to different emotions
def respond_to_emotion(emotion):
    if emotion.lower() in fear_emotions:
        return "I'm here for you. It sounds like you're feeling fearful, and I want you to know you're not alone."
    elif emotion.lower() in happy_emotions:
        return "Congratulations! I'm so glad to hear you're feeling happy!"
    elif emotion.lower() in sad_emotions:
        return "I'm really sorry you're feeling this way. It's okay to feel sad sometimes, and I'm here if you need support."
    elif emotion.lower() in anger_emotions:
        return "It seems like you're feeling angry. Take a deep breath; I'm here to listen if you need to talk."
    elif emotion.lower() in calm_emotions:
        return "It's wonderful that you're feeling calm. Stay relaxed and enjoy the peace."
    else:
        return "Thank you for sharing how you're feeling. I'm here for you no matter what emotion you're experiencing."

# Get emotion input from user
user_emotion = input("Please enter an emotion: ")

# Respond to the user's emotion
response = respond_to_emotion(user_emotion)
print(response)
