from langchain.tools import Tool

def simple_search(query):
    return f"Pretend search result for '{query}'."

search_tool = Tool.from_function(
    func=simple_search,
    name="SimpleSearch",
    description="Search for general knowledge topics not specific to a location or city."
)
