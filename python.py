from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Apply the API Key
openai.api_key = "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"

# Generate a response using OpenAI GPT-3
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form["input_text"]
        response = generate_response(input_text)
        return render_template("index.html", response=response)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run()
