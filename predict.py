import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Folder containing the trained model
MODEL_PATH = "fake_news_model"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()

def predict_news(text):

    # Tokenize the input
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    # Get model prediction
    with torch.no_grad():
        outputs = model(**inputs)

    # Convert logits to probabilities
    probs = torch.softmax(outputs.logits, dim=1)[0]

    fake_prob = probs[0].item()
    real_prob = probs[1].item()

    # Decide label
    if real_prob > fake_prob:
        label = "REAL"
        confidence = real_prob
    else:
        label = "FAKE"
        confidence = fake_prob

    return label, confidence