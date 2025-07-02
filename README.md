
# AI-Web-Automation-Assignment

## Overview
This repository contains a prototype implementation for an AI-driven web automation solution developed for the CloudEagle AI PM Intern assignment. The solution automates user management tasks (data scraping, provisioning, and deprovisioning) for SaaS applications without APIs, such as HubSpot, using Playwright for browser automation and LangChain for AI-driven UI navigation.

The primary deliverable is a 3-5 page PDF document (submitted separately via Google Form), which details the problem, research, proposed solution, and scalability considerations. This repository provides the optional pseudocode/prototype to demonstrate the technical approach.

## Features
- **User Data Scraping**: Extracts user details (names, emails, roles, last login) from SaaS admin portals, handling pagination and dynamic UIs.
- **Provisioning/Deprovisioning**: Automates user creation and removal via form interactions.
- **AI Resilience**: Uses LangChain to adapt to UI changes and reason about dynamic elements.
- **Scalable Design**: Supports multiple SaaS apps through configuration files.

## Repository Contents
- `scraper.py`: Python script with pseudocode for scraping user data and automating user management tasks.
- `README.md`: This file, providing setup and usage instructions.

## Prerequisites
- **Python 3.8+**
- **Playwright**: `pip install playwright`
- **LangChain**: `pip install langchain langchain-openai`
- **OpenAI API Key**: Set as an environment variable (`OPENAI_API_KEY`).
- **Node.js**: Required for Playwright’s browser dependencies (`playwright install`).

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Web-Automation-Assignment.git
   cd AI-Web-Automation-Assignment
   ```
2. Install dependencies:
   ```bash
   pip install playwright langchain langchain-openai
   playwright install
   ```
3. Set the OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   ```
4. Configure the SaaS app:
   - Update the `config` dictionary in `scraper.py` with the target app’s login URL and selectors (e.g., for HubSpot).

## Usage
1. Run the script:
   ```bash
   python scraper.py
   ```
   - The script launches a headless Chromium browser, logs into the SaaS portal, scrapes user data, and simulates provisioning tasks.
   - Output: User data as JSON (e.g., `[{"name": "John Doe", "email": "john@doe.com", ...}]`).
2. Testing:
   - The script uses mock credentials for ethical reasons. For real SaaS apps, update credentials and handle MFA/CAPTCHA as described in the PDF.
3. Customization:
   - Modify `config` in `scraper.py` to support other SaaS apps (e.g., Dropbox, Notion).
   - Add CAPTCHA-solving services (e.g., 2Captcha) for production use.

## Assignment Context
This prototype supports the CloudEagle AI PM Intern assignment, addressing the challenge of automating user management in API-less SaaS applications. The accompanying PDF document details:
- **Problem Analysis**: Why SaaS apps lack APIs and automation challenges.
- **Technologies**: Playwright, LangChain, and Robocorp for scalable RPA.
- **Workflows**: Scraping user data, provisioning/deprovisioning, and handling MFA/CAPTCHAs.
- **Scalability**: Modular configurations and AI-driven resilience for multiple SaaS apps.

## Limitations
- Uses mock data and simplified MFA handling for demonstration.
- Real-world use requires CAPTCHA-solving services and secure credential storage.
- UI changes may need updated selectors or enhanced AI reasoning.

## Future Enhancements
- Integrate a vector database (e.g., Pinecone) for navigation path storage.
- Add automated testing to detect UI changes.
- Expand support for additional SaaS platforms.

## Contact
For questions, please open a GitHub Issue.
