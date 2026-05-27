# Enterprise Meeting Summarizer

AI-powered web application for summarizing meeting notes, extracting action items, and organizing key information into a structured dashboard.

Built with Python, Streamlit, and the OpenAI API.

---

## Features

- AI-generated meeting summaries
- Automatic action item extraction
- Interactive Streamlit dashboard
- Structured output for improved workflow organization
- Markdown export support

---

## Tech Stack

- Python
- Streamlit
- OpenAI API
- python-dotenv

---

## Screenshots

### Main Dashboard
<p align="center">
  <img src="screenshots/dashboard.png" alt="Main Dashboard" width="800">
</p>

### Analysis & Tabs
<p align="center">
  <img src="screenshots/analysis + tabs.png" alt="Analysis and Tabs" width="800">
</p>

### Executive Summary
<p align="center">
  <img src="screenshots/exec summary.png" alt="Executive Summary" width="800">
</p>

### Action Items
<p align="center">
  <img src="screenshots/action items.png" alt="Action Items" width="800">
</p>

### Project Risks
<p align="center">
  <img src="screenshots/Risks.png" alt="Project Risks" width="800">
</p>

---

### Main Interface
![Main Interface](01_dashboard_input.png)

### Generated Summary Dashboard
![Dashboard](02_structured_output.png)

---

## Installation & Setup

```bash
# Clone repository
git clone https://github.com/michal-brozovsky/enterprise-meeting-summarizer.git

# Navigate into project
cd enterprise-meeting-summarizer

# Create virtual environment
python -m venv venv

# Activate virtual environment

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Future Improvements

- PDF export support
- Multi-language summaries
- Meeting transcript upload
- Improved dashboard analytics
