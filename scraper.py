from langchain_openai import ChatOpenAI
from langchain_community.tools.playwright.utils import create_sync_playwright_browser
from langchain.agents import AgentExecutor, create_openai_tools_agent

# Initialize Playwright and LangChain
browser = create_sync_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(sync_browser=browser)
llm = ChatOpenAI(model="gpt-4", api_key="YOUR_OPENAI_KEY")
agent = create_openai_tools_agent(llm, toolkit.get_tools(), prompt="Navigate and extract user data")

# Configuration for SaaS app (e.g., HubSpot)
config = {
    "app": "HubSpot",
    "login_url": "https://app.hubspot.com/login",
    "user_list_selector": "table.users",
    "next_button": "button.next"
}

# Login and scrape data
def scrape_users():
    page = browser.new_page()
    page.goto(config["login_url"])
    page.fill("input#username", "user@example.com")
    page.fill("input#password", "password")
    page.click("button#loginBtn")
    
    # Handle MFA (simplified)
    if page.query_selector("div.mfa"):
        code = get_mfa_code()  # Integrate with 2Captcha or manual input
        page.fill("input#mfaCode", code)
        page.click("button#verify")
    
    # Navigate to user list
    page.goto("https://app.hubspot.com/users")
    users = []
    while True:
        rows = page.query_selector_all(config["user_list_selector"] + " tr")
        for row in rows:
            user = {
                "name": row.query_selector("td.name").inner_text(),
                "email": row.query_selector("td.email").inner_text(),
                "role": row.query_selector("td.role").inner_text(),
                "last_login": row.query_selector("td.last_login").inner_text()
            }
            users.append(user)
        if not page.query_selector(config["next_button"]):
            break
        page.click(config["next_button"])
    
    return users

# Provisioning example
def add_user(name, email, role):
    page = browser.new_page()
    page.goto("https://app.hubspot.com/users/add")
    page.fill("input#name", name)
    page.fill("input#email", email)
    page.select_option("select#role", role)
    page.click("button#submit")
    return page.query_selector("div.success") is not None

# Execute agent for dynamic tasks
agent_executor = AgentExecutor(agent=agent, tools=toolkit.get_tools())
result = agent_executor.run("Extract all users from HubSpot and add a new user")
print(result)
