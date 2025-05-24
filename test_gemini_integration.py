import sys
import os
# Add Agent-S directory to path to allow imports
agent_s_dir = "/home/ubuntu/Agent-S"
sys.path.insert(0, agent_s_dir)

# Set environment variable if needed (though engine.py now hardcodes the key as fallback)
# os.environ["GEMINI_API_KEY"] = "AIzaSyALQLpiVYzzwIYdE-kDDh1bxPOyHMRmaHA"

try:
    # Import the modified engine class
    from gui_agents.s2.core.engine import LMMEngineGemini
    print("Successfully imported LMMEngineGemini.")

    # Instantiate the engine
    print("Instantiating LMMEngineGemini...")
    # Use the model name without 'models/' prefix as the class adds it
    engine = LMMEngineGemini(model="gemini-1.5-flash") # API key is handled internally now
    print("LMMEngineGemini instantiated successfully.")

    # Prepare a simple message list (OpenAI format, will be converted internally)
    messages = [
        {"role": "system", "content": [{"type": "text", "text": "You are a helpful assistant."}]},
        {"role": "user", "content": [{"type": "text", "text": "Hello! Can you tell me a short joke?"}]}
    ]
    print(f"Prepared messages: {messages}")

    # Call the generate method
    print("Calling engine.generate...")
    response = engine.generate(messages=messages, temperature=0.7, max_new_tokens=100)

    # Print the response
    print("\n--- Gemini API Response ---")
    print(response)
    print("--- End of Response ---")

    if isinstance(response, str) and "Error:" in response:
        print("\nTest Failed: An error occurred during generation.")
    elif isinstance(response, str) and len(response.strip()) > 0:
        print("\nTest Passed: Successfully received response from Gemini API.")
    else:
        print("\nTest Failed: Received an empty or unexpected response.")

except ImportError as e:
    print(f"Import Error: {e}. Check if the path is correct and __init__.py files exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    import traceback
    traceback.print_exc()

