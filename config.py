import os

class Config:
    # Render se API Key uthayega
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    
    # Latest Stable Model
    MODEL_NAME = "gemini-1.5-flash"
    
    # Port Setting
    PORT = int(os.environ.get("PORT", 10000))
