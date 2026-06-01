import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr


load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

client = OpenAI()

system_prompt = """
You are a helpful assistant that analyzes job descriptions and provides insights on how to improve a resume based on the job description.
You will be given a job description and a resume.
Your task is to analyze the job description and the resume and provide insights on how to improve the resume based on the job description.

Respond in markdown with the following sections:
1.Overall fit(1-2 sentences. score out of 100)
2.Strengths that match the JD
3.Gaps or missing requirements
4.Keywords to add(if any)
5.3-5 suggested resume bullet point improvements
6. Interview prep topics
7. Final recommendation: Apply, Apply after edits, or Skip
Be honest and specific. Do not invent experience that is not present in the resume. Suggested resume bullets must be based only on the candidate's existing experience.
"""



def analyze_job_description(job_description, resume):
    if not job_description or not job_description.strip():
        yield "Please enter a job description before analyzing."
        return
    if not resume or not resume.strip():
        yield "Please enter your resume before analyzing."
        return

    content =  f"""
    Analyze the job description against the candidate's resume

    ## Job description
    {job_description}
    ## Resume
    {resume}
respond in the format specified in the system instructions.
"""
    try:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.3,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": content}
            ],
            stream=True
        )
        response = ""
        for chunk in stream:
            response += chunk.choices[0].delta.content or ""
            yield response
    except Exception as e:
        yield (
            "Unable to complete the analysis. Please check your OpenAI API key, "
            "account billing, and internet connection, then try again.\n\n"
            f"Details: {e}"
        )

demo = gr.Interface(
    fn=analyze_job_description,
    inputs= [
        gr.Textbox(label="Job Description", lines=12, placeholder="Enter the job description here..."),
        gr.Textbox(label="Resume", lines=12, placeholder="Paste your resume text here...")
    ],
    outputs= gr.Markdown(label="Analysis"),
    title = "AI Job Description Analyzer",
    description= "Paste a job description and resume to get an AI-powered fit analysis and resume improvement suggestions."
)
demo.launch()