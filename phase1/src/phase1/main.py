import os
import openai
from dotenv import load_dotenv
from phase1.crew import receive_user_input_task, extract_sentiment_and_context_task, determine_blog_style_task, content_outlining_task

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def receive_user_input():
    return {
        'topic': input("Enter the topic: "),
        'audience': input("Enter the audience: "),
        'tone': input("Enter the tone: "),
        'content': input("Enter the content or brief description: ")
    }

def main():
    # Step 1: Collect and Validate User Input
    user_input = receive_user_input()
    validated_input = receive_user_input_task(user_input)
    
    # Step 2: Extract Sentiment, Tone, and Keywords
    analysis_report = extract_sentiment_and_context_task(validated_input)
    
    # Step 3: Determine the Most Suitable Blog Style
    blog_style = determine_blog_style_task(analysis_report)
    
    # Step 4: Create a Content Outline
    content_outline = content_outlining_task(analysis_report)
    
    print(f"Selected Blog Style: {blog_style}")
    print(f"Content Outline:\n{content_outline}")

if __name__ == "__main__":
    main()
