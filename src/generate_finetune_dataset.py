import json

def create_finetune_data(input_path, output_path, min_score=4):
    with open(input_path, 'r') as infile:
        data = [json.loads(line) for line in infile]

    training_data = []
    for item in data:
        feedback = item.get("feedback", {})
        if feedback.get("overall", 0) >= min_score:
            training_data.append({
                "prompt": item["prompt"],
                "completion": item["response"]
            })

    with open(output_path, 'w') as outfile:
        for example in training_data:
            outfile.write(json.dumps(example) + "\n")

    print(f"✅ Saved {len(training_data)} examples to {output_path}")
