import openai

def receive_user_input_task(user_input):
    # Validate and structure user input
    # Here, you can add more complex validation and structuring if needed
    return user_input

def extract_sentiment_and_context_task(validated_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a sentiment and context analyzer."},
            {"role": "user", "content": f"Analyze the following content and provide sentiment, tone, and keywords: {validated_input['content']}"}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def determine_blog_style_task(analysis_report):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert blog style analyzer."},
            {"role": "user", "content": f"Based on the following analysis, determine the most suitable blog style: {analysis_report}"}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def content_outlining_task(analysis_report):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a content outlining expert."},
            {"role": "user", "content": f"Based on the following analysis, create a content outline: {analysis_report}"}
        ]
    )
    return response['choices'][0]['message']['content'].strip()
