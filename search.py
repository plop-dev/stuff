import requests
from bs4 import BeautifulSoup

def get_summary(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'
    }
    response = requests.get(url, headers=headers)

    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        answer = soup.select_one(".Z0LcW.t2b5Cf")
        description = soup.select_one(".hgKElc")

        if answer:
            if len(answer.find_all()) > 0:
                answer = answer.findChild().get_text()
            else:
                answer = answer.get_text()
            
            if description:
                description = description.get_text()
            else:
                description = None
            
            return {
                "answer": answer,
                "description": description
            }
    return None

# Get the summary of a user query
# user_query = input("Enter your search query: ")
user_query = "Who is the UK's prime minister?"
info = get_summary(user_query)
print(info)

# Print the summary
if info:
    print(f"Answer: {info['answer']}\nDescription: {info['description']}")
else:
    print("No info available")
