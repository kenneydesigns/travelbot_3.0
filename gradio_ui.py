import gradio as gr
from travelbot3.0 import load_model_and_retriever, hybrid_response, log_feedback
from datetime import datetime

llm, retriever = load_model_and_retriever()

# Store the last response shown
session_state = {"last_prompt": "", "last_response": ""}

def ask_bot(prompt):
    session_state["last_prompt"] = prompt
    response, _ = hybrid_response(prompt, llm, retriever, mode="ui")
    session_state["last_response"] = response
    return response

def submit_feedback(accuracy, helpfulness, clarity, citation, overall):
    feedback = {
        "accuracy": accuracy,
        "helpfulness": helpfulness,
        "clarity": clarity,
        "citation": citation,
        "overall": overall
    }
    log_feedback(session_state["last_prompt"], session_state["last_response"], feedback)
    return "✅ Feedback submitted!"

with gr.Blocks() as demo:
    gr.Markdown("# ✈️ AF TravelBot")
    gr.Markdown("Ask any PCS or TDY travel question.")

    prompt_input = gr.Textbox(label="Your Question", placeholder="e.g., Can I get reimbursed for using a rental car?")
    output = gr.Textbox(label="TravelBot Response", lines=10)

    submit_btn = gr.Button("Ask TravelBot")
    submit_btn.click(fn=ask_bot, inputs=prompt_input, outputs=output)

    gr.Markdown("### 📊 Rate the Response Below:")
    accuracy = gr.Slider(1, 5, step=1, label="🔍 Accuracy")
    helpfulness = gr.Slider(1, 5, step=1, label="🤝 Helpfulness")
    clarity = gr.Slider(1, 5, step=1, label="🗣️ Clarity")
    citation = gr.Slider(1, 5, step=1, label="📚 Citation Quality")
    overall = gr.Slider(1, 5, step=1, label="🌟 Overall")

    feedback_btn = gr.Button("Submit Feedback")
    feedback_output = gr.Textbox(label="", max_lines=1)

    feedback_btn.click(fn=submit_feedback, inputs=[accuracy, helpfulness, clarity, citation, overall], outputs=feedback_output)

demo.launch()
