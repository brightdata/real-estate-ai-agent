<p align="center">
  <a href="https://brightdata.com/">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/brightdata/logo/light.svg" width="300" alt="Bright Data Logo">
  </a>
</p>

# Real Estate AI Agent System

**AI-Powered Solution for Real Estate Data Extraction**

<div align="center">
  <img src="https://img.shields.io/badge/python-3.9+-blue"/>
  <img src="https://img.shields.io/badge/License-MIT-blue"/>
</div>

---

## 🌟 Overview

Real Estate AI Agent System is a Python-based solution that leverages AI agents and Bright Data's Model Context Protocol (MCP) server to extract, process, and deliver structured real estate property data from multiple sources.

- Automates property data extraction from real estate websites like [Zillow](https://brightdata.com/products/web-scraper/zillow), [Realtor.com](https://brightdata.com/products/web-scraper/realtor), Redfin, and more  
- Integrates with Bright Data proxies for robust anti-bot and geo-unblocking  
- Uses Nebius Qwen LLM for adaptive, schema-validated property data extraction  
- Outputs results as structured JSON for analytics or downstream applications

---

## Table of Contents

- ✨ Features
- 🚀 Quickstart
- 🔧 Environment Setup
- 💡 Usage Example
- 📈 Key Capabilities
- 🔒 Security Best Practices

---

## ✨ Features

- **Intelligent AI Agents:** Uses CrewAI and LLM for adaptive data extraction and property detail parsing.
- **Bright Data Integration:** Seamless support for proxy rotation, CAPTCHA solving via MCP server.
- **Strict JSON Schema:** Always returns result in snake_case, schema-validated JSON.
- **Plug-and-Play:** Spin up an advanced real estate data pipeline in minutes.
- **Cross-Platform:** Python 3.9; requires Node.js for Bright Data MCP server.

---

## 🚀 Quickstart

1. Clone this repository

   ~~~sh
   git clone https://github.com/brightdata-com/real-estate-ai-agents.git
   cd real-estate-ai-agents
   ~~~

---

## 🔧 Environment Setup

### Prerequisites

- Python 3.9+
- Node.js + npm (for Bright Data MCP server)
- Bright Data account with API token
- Nebius AI API key

### Virtual Environment

macOS/Linux
~~~sh
python3.9 -m venv venv
source venv/bin/activate
~~~

Windows
~~~sh
python3.9 -m venv venv
.\venv\Scripts\activate
~~~

### Install Dependencies

~~~sh
pip install "crewai-tools[mcp]" crewai mcp python-dotenv pandas
~~~

### Add Environment Variables

Create a `.env` file in your project directory with the following:

~~~env
BRIGHT_DATA_API_TOKEN="your_api_token_here"
WEB_UNLOCKER_ZONE="your_web_unlocker_zone"
BROWSER_ZONE="your_browser_zone"
NEBIUS_API_KEY="your_nebius_api_key"
~~~

---

## 💡 Usage Example

To run the agent:

~~~sh
python real_estate_agents.py
~~~

If successful, the script will extract property data from a real estate listing and output result like:

~~~json
{
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
}
~~~

---

## 📈 Key Capabilities

- Extracts address, price, bedrooms, bathrooms, square footage, lot size, year built, property type, listing agent, days on market, MLS number, description, image URLs, and neighborhood.
- Strict JSON schema validation: always outputs snake_case keys.
- Handles [proxy rotation](https://brightdata.com/solutions/rotating-proxies), [CAPTCHAs](https://brightdata.com/products/web-unlocker/captcha-solver), and anti-bot protections using Bright Data’s MCP stack.
- Easily extendable for more data fields and custom sources.

---

## 🔒 Security Best Practices

- Store all API keys and credentials securely in your `.env` file.
- Always validate and sanitize extracted data before use.
- Respect robots.txt and website terms of service.

---

<p align="center">
  <a href="https://brightdata.com/">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/brightdata/logo/light.svg" width="200" alt="Bright Data Logo">
  </a>
</p>
