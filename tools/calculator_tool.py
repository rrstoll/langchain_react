from langchain.tools import Tool

def calculator(query):
    try:
        result = eval(query)
        return f"The result is {result}."
    except Exception as e:
        return f"Error: {str(e)}"

calculator_tool = Tool.from_function(
    func=calculator,
    name="Calculator",
    description="Perform basic math calculations."
)
