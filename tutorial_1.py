from groq import Groq
# Make sure your config.py has GROQ_API_KEY defined
from config import Config

# Initialize the Groq client
client = Groq(api_key=Config.GROQ_API_KEY)

def generate_text_with_groq(prompt):
    try:
        # Groq uses the 'chat.completions' pattern
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            # Recommended fast models: 
            # 'llama-3.3-70b-versatile' or 'llama-3.1-8b-instant'
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Execution
if __name__ == "__main__":
    user_prompt = "Explain closures in JavaScript in 2 lines"
    
    print("--- Requesting Groq (Llama 3.3) ---")
    result = generate_text_with_groq(user_prompt)
    print("\nResult:")
    print(result)