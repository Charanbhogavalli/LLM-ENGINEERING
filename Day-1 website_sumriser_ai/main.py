import os

from dotenv import load_dotenv
from openai import OpenAI

from scraper import scrape_website


# Load API key
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


# Create OpenAI client
client = OpenAI(api_key=openai_api_key)


# Function to generate GPT response
def generate_response(prompt):

    response = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# Main function
def main():

    # Get URL from user
    url = input("Enter the URL of the website to scrape: ")

    # Scrape website
    scraped_data = scrape_website(url)

    # Create prompt
    prompt = f"""
    Analyze the following website data
    and provide a summary:

    {scraped_data}
    """

    # Generate AI response
    summary = generate_response(prompt)

    # Print summary
    print("\nWebsite Summary:\n")

    print(summary)


# Run main function
main()