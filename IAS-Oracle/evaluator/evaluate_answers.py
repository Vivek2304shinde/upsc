import os
import openai

def evaluate_answer(user_answer, model_answer):
    """
    Evaluates user answers using AI and provides detailed feedback.
    This function compares the user's answer with a model answer and gives
    specific suggestions for improvement.
    """
    # Set up OpenAI API key (ensure you have your key in .env)
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Add your API key here

    # Prepare the prompt for evaluation
    prompt = f"""
    You are an examiner. Evaluate the following answer based on its relevance, completeness, and specificity.
    
    User Answer:
    {user_answer}
    
    Model Answer:
    {model_answer}

    Provide feedback on how the user can improve their answer, specifying if it is too negative, brief, or lacking in details.
    """

    # Make the API call to OpenAI
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or any other model you prefer
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        feedback = response['choices'][0]['message']['content']
        return feedback
    except Exception as e:
        return f"Error evaluating answer: {e}"
