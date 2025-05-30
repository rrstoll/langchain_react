---

# 🌍 City Info

**City Info** is an interactive AI-powered assistant that provides real-time information about cities worldwide. Built with [LangChain](https://www.langchain.com/) and [Streamlit](https://streamlit.io/), it integrates tools for:

* 📰 City-specific news headlines
* 🌤️ Real-time weather updates
* ➗ Math calculations
* 🔍 General search queries

Ask natural language questions like:

* “What’s the latest news in Tokyo?”
* “What’s the weather in Paris?”
* “What is 45 \* 23?”
* “Tell me about the Eiffel Tower’s history.”

---

## 🚀 Features

* **Conversational Interface**: Engages users in a chat-like experience.
* **Tool Integration**: Utilizes multiple tools for comprehensive responses.
* **Responsive Design**: Optimized for various devices using Streamlit.
* **Customizable**: Easily extendable with additional tools or features.

---

## 🛠️ Installation

### Prerequisites

* Python 3.8 or higher
* [pip](https://pip.pypa.io/en/stable/installation/)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/city-info.git
   cd city-info
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file in the root directory and add your API keys:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   NEWS_API_KEY=your_newsapi_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   ```

5. **Run the application**:

   ```bash
   streamlit run app.py
   ```

---

## 🧪 Usage

1. Open your browser and navigate to `http://localhost:8501`.
2. Enter your query in the input box, such as:

   * “What's the weather in New York?”
   * “Latest news from Berlin.”
   * “Calculate 123 \* 456.”
3. View the AI-generated response in the chat interface.

---

## 📁 Project Structure

```
city-info/
├── tools/
│   ├── calculator_tool.py
│   ├── news_tool.py
│   ├── search_tool.py
│   └── weather_tool.py
├── app.py
├── requirements.txt
└── .env.example
```

* `tools/`: Contains individual tool integrations.
* `app.py`: Main application script.
* `requirements.txt`: Python dependencies.
* `.env.example`: Sample environment variables file.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

* [LangChain](https://www.langchain.com/) for the ReAct framework.
* [Streamlit](https://streamlit.io/) for the user interface.
* [OpenAI](https://openai.com/) for the language model.
* [NewsAPI](https://newsapi.org/) for news data.
* [WeatherAPI](https://www.weatherapi.com/) for weather information.

---