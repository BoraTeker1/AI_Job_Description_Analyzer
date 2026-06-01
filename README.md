# AI Job Description Analyzer

An LLM-powered web app that compares a job description against a candidate's resume and generates practical feedback to improve job application quality.

## What It Does

Users paste a job description and their resume text. The app analyzes both and returns a structured markdown report with:

* Overall fit score and summary
* Strengths that match the job description
* Missing or weak requirements
* Keywords to add
* Resume bullet improvement suggestions
* Interview prep topics
* Final recommendation: Apply, apply after edits, or skip

The app streams the response in real time for a smoother user experience.

## Tech Stack

* Python
* OpenAI API
* Gradio
* python-dotenv

## Why I Built This

As a recent Computer Science graduate applying to software engineering and AI-adjacent roles, I wanted to build a practical LLM application that solves a real job-search problem. This project helped me practice prompt engineering, API integration, streaming responses, input validation, and building a simple user-facing AI product.

## Features

* Resume-to-job fit analysis
* Markdown-formatted AI feedback
* Streaming output
* Basic input validation
* API error handling
* Clean Gradio interface

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-job-description-analyzer.git
cd ai-job-description-analyzer
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Run the app:

```bash
python app.py
```

Open the local Gradio URL in your browser.

## Future Improvements

* Add job URL scraping
* Support PDF resume upload
* Add model selection
* Save past analyses
* Deploy the app publicly

## Demo

![AI Job Description Analyzer — inputs and analysis start](docs/demo-1.png)

![AI Job Description Analyzer — keywords and resume suggestions](docs/demo-2.png)

![AI Job Description Analyzer — interview prep and final recommendation](docs/demo-3.png)
