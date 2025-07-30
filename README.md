<p align="center">
  <a href="https://brightdata.com/">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/brightdata/logo/light.svg" width="300" alt="Bright Data Logo">
  </a>
</p>

# Real Estate AI Agent System

**AI-Powered Solution for Real Estate Data Extraction**

<div align="center">
  <img src="https://img.shields.io/badge/python-3.11+-brightgreen"/>
  <img src="https://img.shields.io/badge/License-MIT-blue"/>
</div>

---

## 🌟 Overview

Real Estate AI Agent System is a Python-based solution that uses advanced AI agents and Bright Data's ecosystem (including the MCP server) to extract, process, and deliver structured real estate property data from multiple sources.

- Automates property data extraction from real estate websites
- Integrates with Bright Data proxies for robust anti-bot and geo-unblocking
- AI-powered data parsing and normalization
- Outputs results as structured JSON for downstream analytics or application use

---

## Table of Contents

- ✨ Features
- 🚀 Quickstart
- 🔧 Environment Setup
- 💡 Usage Example
- 📈 Key Capabilities
- 🔒 Security Best Practices
- 🤝 Contributing
- 📞 Support

---

## ✨ Features

- **Intelligent AI Agents:** Leverages CrewAI and LLMs for adaptive data extraction and property detail parsing.
- **Bright Data Integration:** Supports proxy rotation, CAPTCHA solving, and full anti-bot bypass.
- **Multi-Platform Support:** Works with Python 3.11+ and Node.js (for MCP server).
- **Customizable Workflows:** Easy integration into data pipelines and analytics platforms.
- **Plug-and-Play Configuration:** Stand up your own property crawler in minutes.

---

## 🚀 Quickstart

1. Clone this repository

   ~~~sh
   git clone https://github.com/brightdata-com/real-estate-ai-agents.git
   cd real-estate-ai-agents
   ~~~

---

## 🔧 Environment Setup

**Prerequisites:**

- Python 3.11+
- Node.js + npm (for Bright Data MCP server)
- Bright Data account with API token
- Nebius AI API key

**Create and activate a virtual environment:**

macOS/Linux

~~~sh
python -m venv venv
source venv/bin/activate
~~~

Windows

~~~sh
python -m venv venv
.\venv\Scripts\activate
~~~

**Install dependencies:**

~~~sh
pip install "crewai-tools[mcp]" crewai mcp python-dotenv pandas
~~~

**Create a `.env` file** with your API credentials:

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

The script will extract property data from real estate websites and output it in structured JSON format. Example output:

~~~json
{
  "address": "123 Example St, Los Angeles, CA",
  "price": "$900,000",
  "bedrooms": 3,
  "bathrooms": 2,
  "size_sqft": 1800,
  "listing_url": "https://www.example.com/listing/123"
}
~~~

---

## 📈 Key Capabilities

- Extracts property details such as address, price, square footage, bedrooms, bathrooms, and more
- Supports property data normalization and enrichment for cross-site comparisons
- Handles proxy rotation, CAPTCHA challenges, and anti-bot detection using Bright Data’s infrastructure
- Easily extendable to support additional real estate data sources and custom use cases

---

## 🔒 Security Best Practices

- Always store API tokens and credentials securely, such as in a `.env` file.
- Validate and sanitize all extracted data before further analytics or storage.
- Respect website terms of service and robots.txt directives when scraping.

---

<p align="center">
  <a href="https://brightdata.com/">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/brightdata/logo/light.svg" width="200" alt="Bright Data Logo">
  </a>
</p>
