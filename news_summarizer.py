import requests
from bs4 import BeautifulSoup
import openai

# OpenAI API Key
openai.api_key = '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'
def fetch_news():
    url = 'https://www.cricbuzz.com/cricket-news/latest-news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Latest 3 news fetch karo
    headlines = soup.find_all('div', class_='cb-nws-intr')[:3]
    news_list = [headline.text.strip() for headline in headlines]

    return news_list
def summarize_news(news):
    prompt = f"Summarize this news: {news}"
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=100
    )
    
    summary = response['choices'][0]['text'].strip()
    return summary
def main():
    print("Fetching latest news...")
    try:
        news_list = fetch_news()
    except Exception as e:
        print(f"Error fetching news: {e}")
        return
    
    for i, news in enumerate(news_list, 1):
        print(f"\nNews {i}: {news}")
        try:
            summary = summarize_news(news)
            print(f"Summary: {summary}")
        except Exception as e:
            print(f"Error summarizing news: {e}")

if __name__ == "__main__":
    main()