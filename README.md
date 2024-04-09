# Weather Forecast Bot

# Fetch Weather Forecast Function

This Python function `fetch_weather_forecast` retrieves the hourly weather forecast for a specified location.

## Parameters

- `location` (str): The location for which the weather forecast is requested.

## Returns

The function returns the hourly weather forecast data as a list of dictionaries if the request is successful. Otherwise, it returns None.

# Main Program

This Python script interacts with the OpenAI API to provide weather forecast assistance and general queries.

## Setup

- The environment variables required for the OpenAI API key are loaded using `load_dotenv`.
- The `entity` module is imported to use functions for creating threads, starting conversations, and getting responses.

## Main Function

The `main` function:
1. Creates a thread for conversation.
2. Prompts the user to provide the location for the weather forecast.
3. Sets up the OpenAI assistant.
4. Starts the conversation with the user and retrieves the weather forecast response.
5. Asks the user if further assistance is needed.
6. Based on the user's response, either requests the weather forecast again or provides general assistance.


## Description
This is a Flask web application that serves as a weather forecast bot. It allows users to explore weather forecasts based on their specific criteria.

## Features
- Initiate conversation with the bot
- Gather user input for location and date preferences
- Validate user input
- Fetch weather forecast data using a weather forecast API
- Display weather forecast results to the user
- Provide feedback or suggestions based on user interactions
  
## Setting Up OpenAI Assistant Using OpenAI API

Follow these steps to set up your OpenAI assistant using the OpenAI API:

1. **Sign Up for OpenAI API**:
   - Visit the OpenAI website and sign up for an account if you haven't already.
   - Subscribe to the OpenAI API plan that suits your needs.

2. **Get API Key**:
   - Once subscribed, you'll receive an API key. This key is essential for authenticating your requests.

3. **Install OpenAI Python Library**:
   - Use pip to install the OpenAI Python library:
     ```
     pip install openai
     ```

4. **Import OpenAI Library**:
   - In your Python script or environment, import the OpenAI library:
     ```python
     import openai
     ```

5. **Set API Key**:
   - Set your API key using the `openai.api_key` attribute:
     ```python
     openai.api_key = 'YOUR_API_KEY'
     ```

6. **Invoke OpenAI API**:
   - Use the OpenAI API to interact with the language model. For example:
     ```python
     response = openai.Completion.create(
         engine="text-davinci-003",
         prompt="Once upon a time",
         max_tokens=50
     )
     print(response.choices[0].text.strip())
     ```

7. **Explore API Documentation**:
   - Refer to the official OpenAI API documentation for detailed information on endpoints, parameters, and usage examples.

8. **Understand API Usage and Billing**:
   - Familiarize yourself with usage limits and billing details to avoid exceeding quotas and unexpected charges.

9. **Experiment and Develop**:
   - Start experimenting with the OpenAI models, explore prompts, and develop your applications.

10. **Handle Errors and Exceptions**:
    - Implement error handling mechanisms in your code to gracefully handle any errors during API requests.

By following these steps, you can set up and start using the OpenAI API to interact with powerful language models and build innovative applications leveraging artificial intelligence capabilities.

## Setup
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up environment variables:
   - `WEATHER_API_KEY`: Your API key for the weather forecast service from the official RAPID API Website.
4. 
4. Run the Flask application using `python app.py`.
5. Access the application in your web browser at `http://localhost:5000`.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript

