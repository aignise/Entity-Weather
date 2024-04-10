from entity import create_thread, start, get_response
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    while True:
        # Create a thread for conversation
        thread_id = create_thread()

        user_query_prompt = "Please provide the location for weather forecast: "
        user_query = input(user_query_prompt)
        assistant_id = os.getenv("OPENAI_ASSISTANT_ID")
        
        start(thread_id, user_query)

        response = get_response(thread_id, assistant_id, user_query)

        print("Weather Forecast:", response)

        while True:
            further_assistance = input("Do you need further assistance? (yes/no): ").lower()
            if further_assistance == "no":
                print("Thank you for using the assistant. Goodbye!")
                return
            elif further_assistance == "yes":
                assistance_type = input("Do you need weather forecast again or general assistance? (weather/general): ").lower()
                if assistance_type == "weather":
                    user_query_prompt = "Please provide the location for weather forecast: "
                    user_query = input(user_query_prompt)
                    start(thread_id, user_query)
                    response = get_response(thread_id, assistant_id, user_query)
                    print("Weather Forecast:", response)
                    
                elif assistance_type == "general":
                    user_query_prompt = "How can I help you?: "
                    user_query = input(user_query_prompt)
                    start(thread_id, user_query)
                    response = get_response(thread_id, assistant_id, user_query)
                    print("General Assistance:", response)
                    
                else:
                    print("Invalid option. Please enter 'weather' or 'general'.")
            else:
                print("Invalid option. Please enter 'yes' or 'no'.")
        break
if __name__ == "__main__":
    main()
