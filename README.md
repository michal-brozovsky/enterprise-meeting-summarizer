# Enterprise Meeting Summarizer

An AI-powered web application designed to streamline project management by converting unstructured, chaotic meeting notes into clean, actionable dashboards. Built with Python, Streamlit, and the OpenAI API.

## Features

* **Automated Structuring**: Uses OpenAI's JSON mode to reliably extract specific data points.
* **Interactive Dashboard**: Splits outputs into easy-to-read tabs (Executive Summary, Action Items, Risks).
* **Smart Tables**: Automatically formats tasks, assignees, and deadlines into an organized matrix.
* **One-Click Export**: Download the generated report as a Markdown (`.md`) file for easy sharing in Jira, Confluence, or GitHub.

## Tech Stack

* **Frontend**: Streamlit
* **Backend logic**: Python
* **LLM**: OpenAI API (`gpt-4o-mini` model)


## Screenshots
Clean UI Waiting for Input(screenshots/01_dashboard_input.png)
Structured Dashboard Output(screenshots/02_structured_output.png)

## Installation & Setup

1. **Clone the repository**
```bash
   git clone [https://github.com/yourusername/meeting-summarizer.git](https://github.com/yourusername/meeting-summarizer.git)
   cd meeting-summarizer
