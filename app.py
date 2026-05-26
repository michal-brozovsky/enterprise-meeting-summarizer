import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# 1. Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 2. Page Configuration
st.set_page_config(page_title="Enterprise Meeting Summarizer", layout="wide")
st.title("Enterprise Meeting Summarizer")

if not api_key:
    st.error("🔴 ERROR: OpenAI API key not found. Check your .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

# 3. User Interface
st.markdown("Convert raw, unstructured meeting notes into professional, actionable insights.")
meeting_notes = st.text_area(
    "Raw Meeting Notes", 
    height=200,
    placeholder="Paste the raw text of your meeting discussion here..."
)

# 4. Processing Logic
if st.button("Generate Dashboard", type="primary"):
    if meeting_notes.strip() == "":
        st.warning("⚠️ Please enter meeting notes first.")
    else:
        with st.spinner("Analyzing meeting data and extracting action items..."):
            try:
                system_prompt = """
                You are an enterprise AI assistant. Analyze the meeting notes and extract the core information.
                You MUST return ONLY a valid JSON object with the exact following structure. Do not add markdown blocks around the JSON.
                
                {
                    "executive_summary": "A 2-3 sentence overview of the meeting.",
                    "risks": ["Risk 1", "Risk 2"],
                    "action_items": [
                        {"Task": "Task description", "Assignee": "Name", "Deadline": "Date"}
                    ]
                }
                If there are no risks, return an empty array [].
                """

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    response_format={ "type": "json_object" },
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": meeting_notes}
                    ],
                    temperature=0.2
                )

                # Parse JSON
                result = json.loads(response.choices[0].message.content)
                
                st.success("✅ Analysis Complete!")
                st.divider()

                # 5. Dashboard Layout (Splitting the data)
                tab1, tab2, tab3 = st.tabs(["📋 Executive Summary", "✅ Action Items", "⚠️ Risks & Blockers"])
                
                with tab1:
                    st.write(result.get("executive_summary", "No summary available."))
                
                with tab2:
                    action_items = result.get("action_items", [])
                    if action_items:
                        st.table(action_items) # Native Streamlit table
                    else:
                        st.info("No action items identified.")
                        
                with tab3:
                    risks = result.get("risks", [])
                    if risks:
                        for risk in risks:
                            st.warning(risk)
                    else:
                        st.success("No critical risks identified.")
                
                st.divider()

                # 6. Export Functionality
                # Prepare a markdown string for download
                md_export = f"# Meeting Report\n\n## Executive Summary\n{result.get('executive_summary', '')}\n\n## Action Items\n"
                for item in action_items:
                    md_export += f"- **{item['Task']}** (Assignee: {item['Assignee']}, Deadline: {item['Deadline']})\n"
                
                md_export += "\n## Risks\n"
                for risk in risks:
                    md_export += f"- {risk}\n"

                st.download_button(
                    label="💾 Download Report (Markdown)",
                    data=md_export,
                    file_name="meeting_report.md",
                    mime="text/markdown"
                )

            except json.JSONDecodeError:
                st.error("🔴 Failed to parse AI response. Please try again.")
            except Exception as e:
                st.error(f"🔴 API Error: {e}")