# 🤖 Autonomous School Agent

A high-reliability, text-driven execution agent for automating Schoology, Outlook, and other school-related tasks. Built for students who want to automate the mundane and focus on the meaningful.

## 🏗 Features
- **Schoology Integration**: Dynamic course discovery, assignment crawling, and automated submission.
- **Outlook Automation**: Background email monitoring and feedback retrieval with Microsoft SSO bypass.
- **Human-Mimicking Behavior**: Uses hardened Playwright patterns to avoid bot detection.
- **Modular Skills**: 18+ specialized skills including `doc-generator`, `visual-pro` (image sourcing), and `research-navigator`.
- **Cross-Platform**: Designed to run seamlessly on both Linux and Windows.

## 📂 Project Structure
- `core/`: Central logic, controllers, and prompt builders.
- `browser/`: Playwright-based web automation clients.
- `config/`: Environment configuration and dependencies.
- `skills/`: Modular capabilities for specific tasks.
- `scripts/`: Implementation examples for various missions.
- `generated_docs/`: Workspace for synthesized assignments.

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.10+**
- **Node.js** (for Playwright browser engines)

### 2. Installation

#### 🐧 Linux
```bash
# Clone the repository
git clone https://github.com/yourusername/autonomous-school-agent.git
cd autonomous-school-agent

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r config/requirements.txt
playwright install chromium
```

#### 🪟 Windows
```powershell
# Clone the repository
git clone https://github.com/yourusername/autonomous-school-agent.git
cd autonomous-school-agent

# Create a virtual environment
python -m venv venv
.\venv\Scripts\Activate

# Install dependencies
pip install -r config/requirements.txt
playwright install chromium
```

### 3. Configuration
Rename `config/.env.example` to `config/.env` and fill in your institutional credentials:
```env
SCHOOLOGY_DOMAIN=your-school.schoology.com
SCHOOLOGY_EMAIL=your-email@school.ca
SCHOOLOGY_PASSWORD=your-password
HEADLESS=True
```

### 4. Running
To run the default autonomous mission:
```bash
python main.py
```

## 🛠 Advanced Usage

### Monitoring Emails
Run the background email action engine to stay on top of notifications:
```bash
python scripts/email_action_engine.py
```

### Generating Documents
Use the `doc-generator` skill to synthesize research into professional formats:
```python
from core.controller import HWBotController
bot = HWBotController()
# Implement your logic here...
```

## 📝 Safety & Privacy
This agent is designed for **Autonomy with Integrity**. 
- **Secrets Management**: Always use the `.env` file; never hardcode credentials.
- **Hardened Login**: Handles Microsoft SSO and institutional redirect loops automatically.
- **Session Profiles**: Browser profiles are stored in `browser/profiles/` to minimize redundant logins.

## ⚖️ License
MIT License - See [LICENSE](LICENSE) for details.
