from langchain.tools import Tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

city_to_country = {
    # China
    "Shanghai": "cn", "Beijing": "cn", "Chongqing": "cn",
    # India
    "Mumbai": "in", "Delhi": "in", "Bengaluru": "in",
    # United States
    "New York City": "us", "Los Angeles": "us", "Chicago": "us",
    # Indonesia
    "Jakarta": "id", "Surabaya": "id", "Bandung": "id",
    # Pakistan
    "Karachi": "pk", "Lahore": "pk", "Faisalabad": "pk",
    # Brazil
    "São Paulo": "br", "Rio de Janeiro": "br", "Salvador": "br",
    # Nigeria
    "Lagos": "ng", "Kano": "ng", "Ibadan": "ng",
    # Bangladesh
    "Dhaka": "bd", "Chittagong": "bd", "Gazipur": "bd",
    # Russia
    "Moscow": "ru", "Saint Petersburg": "ru", "Novosibirsk": "ru",
    # Mexico
    "Mexico City": "mx", "Guadalajara": "mx", "Monterrey": "mx",
    # Japan
    "Tokyo": "jp", "Yokohama": "jp", "Osaka": "jp",
    # Ethiopia
    "Addis Ababa": "et", "Dire Dawa": "et", "Mekelle": "et",
    # Philippines
    "Quezon City": "ph", "Manila": "ph", "Davao City": "ph",
    # Egypt
    "Cairo": "eg", "Alexandria": "eg", "Giza": "eg",
    # Vietnam
    "Ho Chi Minh City": "vn", "Hanoi": "vn", "Hai Phong": "vn",
    # DR Congo
    "Kinshasa": "cd", "Lubumbashi": "cd", "Mbuji-Mayi": "cd",
    # Turkey
    "Istanbul": "tr", "Ankara": "tr", "Izmir": "tr",
    # Iran
    "Tehran": "ir", "Mashhad": "ir", "Isfahan": "ir",
    # Germany
    "Berlin": "de", "Hamburg": "de", "Munich": "de",
    # Thailand
    "Bangkok": "th", "Nonthaburi": "th", "Nakhon Ratchasima": "th",
    # United Kingdom
    "London": "gb", "Birmingham": "gb", "Manchester": "gb",
    # France
    "Paris": "fr", "Marseille": "fr", "Lyon": "fr",
    # Italy
    "Rome": "it", "Milan": "it", "Naples": "it",
    # South Africa
    "Johannesburg": "za", "Cape Town": "za", "Durban": "za",
    # Tanzania
    "Dar es Salaam": "tz", "Mwanza": "tz", "Arusha": "tz",
    # Myanmar
    "Yangon": "mm", "Mandalay": "mm", "Naypyidaw": "mm",
    # South Korea
    "Seoul": "kr", "Busan": "kr", "Incheon": "kr",
    # Colombia
    "Bogotá": "co", "Medellín": "co", "Cali": "co",
    # Kenya
    "Nairobi": "ke", "Mombasa": "ke", "Kisumu": "ke",
    # Spain
    "Madrid": "es", "Barcelona": "es", "Valencia": "es",
}

def get_news(city):
    url = f"https://newsapi.org/v2/everything?q={city}&language=en&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    articles = res.get("articles", [])
    if not articles:
        return f"Sorry, I don't have news for {city}."

    return "\n".join([f"{i+1}. {a.get('title')} ({a.get('source', {}).get('name')})" for i, a in enumerate(articles[:3])])

news_tool = Tool.from_function(
    func=get_news,
    name="GetCityNews",
    description="Get recent English-language news headlines for a city."
)
