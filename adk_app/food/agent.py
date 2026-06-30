import csv
from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# 1. The Low-Token Data Engineering Tool
def get_dish_reviews(dish_name: str) -> str:
    """Reads the local CSV and extracts only rows matching the specific dish."""
    matched_reviews = []
    
    try:
        with open('reviews.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['dish'].lower() == dish_name.lower():
                    matched_reviews.append(row['review'])
    except FileNotFoundError:
        return "Error: reviews.csv file missing."

    if not matched_reviews:
        return f"No review data found for '{dish_name}'."
        
    # Standardize into a clean list for the model
    return "\n".join([f"- {rev}" for rev in matched_reviews])

# Wrap the CSV reader into an ADK tool
csv_tool = FunctionTool(get_dish_reviews)

# 2. The Agent Layer
root_agent = Agent(
    name="dish_analyst_agent",
    model="gemini-2.5-flash", # Or your local ollama/llama3.2:3b to save your API quota entirely!
    instruction="""
    You are a casual restaurant dashboard assistant. 
    Use the 'get_dish_reviews' tool to look up feedback for the requested dish. 
    Give a quick, 2-sentence summary of what people like and dislike.
    """,
    tools=[csv_tool]
)