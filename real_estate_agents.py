# Import Required Libraries:
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
from crewai.llm import LLM
import os
import json
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


# Configure Qwen LLM for deterministic output
llm = LLM(
    model="nebius/Qwen/Qwen3-235B-A22B",
    api_key=os.getenv("NEBIUS_API_KEY")
)

# Bright Data MCP server configuration
server_params = StdioServerParameters(
    command="npx",
    args=["@brightdata/mcp"],
    env={
        "API_TOKEN": os.getenv("BRIGHT_DATA_API_TOKEN"),
        "WEB_UNLOCKER_ZONE": os.getenv("WEB_UNLOCKER_ZONE"),
        "BROWSER_ZONE": os.getenv("BROWSER_ZONE"),
    },
)

def build_scraper_agent(mcp_tools):
    return Agent(
        role="Senior Real Estate Data Extractor",
        goal=(
            "Return a JSON object with snake_case keys containing: address, price, "
            "bedrooms, bathrooms, square_feet, lot_size, year_built, property_type, "
            "listing_agent, days_on_market, mls_number, description, image_urls, "
            "and neighborhood for the target property listing page. Ensure strict schema validation."
        ),
        backstory=(
            "Veteran real estate data engineer with years of experience extracting "
            "property information from Zillow, Realtor.com, and Redfin. Skilled in "
            "Bright Data MCP, proxy rotation, CAPTCHA avoidance, and strict "
            "JSON-schema validation for real estate data."
        ),
        tools=mcp_tools,
        llm=llm,
        max_iter=3,
        verbose=True,
    )

def build_scraping_task(agent):
    return Task(
        description=(
            "Extract property data from https://www.zillow.com/homedetails/123-Main-St-City-State-12345/123456_zpid/ "
            "and return it as structured JSON."
        ),
        expected_output="""{
            "address": "123 Main Street, City, State 12345",
            "price": "$450,000",
            "bedrooms": 3,
            "bathrooms": 2,
            "square_feet": 1850,
            "lot_size": "0.25 acres",
            "year_built": 1995,
            "property_type": "Single Family Home",
            "listing_agent": "John Doe, ABC Realty",
            "days_on_market": 45,
            "mls_number": "MLS123456",
            "description": "Beautiful home with updated kitchen...",
            "image_urls": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
            "neighborhood": "Downtown Historic District"
        }""",
        agent=agent,
    )


def scrape_property_data():
    """Assembles and runs the scraping crew."""
    with MCPServerAdapter(server_params) as mcp_tools:
        scraper_agent = build_scraper_agent(mcp_tools)
        scraping_task = build_scraping_task(scraper_agent)

        crew = Crew(
            agents=[scraper_agent],
            tasks=[scraping_task],
            process=Process.sequential,
            verbose=True
        )
        return crew.kickoff()

if __name__ == "__main__":
    try:
        result = scrape_property_data()
        print("\n[SUCCESS] Scraping completed!")
        print("Extracted property data:")
        print(result)
    except Exception as e:
        print(f"\n[ERROR] Scraping failed: {str(e)}")