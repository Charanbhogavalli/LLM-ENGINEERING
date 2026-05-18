import os

from dotenv import load_dotenv
from openai import OpenAI

from scraper import scrape_website


# Load API key
load_dotenv()




# Create OpenAI client
client = OpenAI(base_url="http://localhost:11434/v1",api_key="ollama")


# Function to generate GPT response
def generate_response(prompt):

    response = client.chat.completions.create(
        model="llama3.2:1b",

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