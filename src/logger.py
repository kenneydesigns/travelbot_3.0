def log_response(prompt, response, sources, feedback_score):
    log_dir = "/home/travelbot/travelbot_3.0/logs"
    os.makedirs(log_dir, exist_ok=True)  # ✅ Creates the logs folder if missing
    log_path = os.path.join(log_dir, "response_log.jsonl")

    with open(log_path, "a") as logfile:
        logfile.write(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "prompt": prompt,
            "response": response,
            "sources": sources,
            "feedback": feedback_score
        }) + "\n")