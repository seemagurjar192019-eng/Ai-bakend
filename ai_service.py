import google.generativeai as genai
from config import Config

class GeminiService:
    def __init__(self):
        # API Configure
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(Config.MODEL_NAME)

    def get_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            if response and response.text:
                return response.text
            return "AI khamosh hai, shayad net slow hai."
        except Exception as e:
            return f"Gemini Service Error: {str(e)}"

# Instance create karke export karo
gemini_ai = GeminiService()
