# Real Estate AI System

A Python-based solution for extracting and processing real estate property data using AI agents.

## Environment Setup

### Prerequisites
- Python 3.11+
- Node.js + npm (for Bright Data MCP server)
- Bright Data account with API token
- Nebius AI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/icode247/real-estate-agent.git
   cd real-estate-ai-system
   ```

2. Create and activate a virtual environment:
   ```bash
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install "crewai-tools[mcp]" crewai mcp python-dotenv pandas
   ```

4. Create a `.env` file with your API credentials:
   ```
   BRIGHT_DATA_API_TOKEN="your_api_token_here"
   WEB_UNLOCKER_ZONE="your_web_unlocker_zone"
   BROWSER_ZONE="your_browser_zone"
   NEBIUS_API_KEY="your_nebius_api_key"
   ```

## real_estate_agents.py

This script implements a web scraping system for real estate property data using CrewAI and Bright Data's MCP server.

### Key Features
- Extracts property details from real estate websites
- Returns structured JSON data
- Uses AI agents for intelligent data extraction
- Handles proxy rotation and CAPTCHAs

### Usage
1. Ensure your `.env` file is properly configured
2. Run the script:
   ```bash
   python real_estate_agents.py
   ```

The script will output property data in JSON format.