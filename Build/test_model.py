from predict import predict_news
print("Testing prediction...")
try:
    label, conf = predict_news("This is a test news article.")
    print(f"Success! Label: {label}, Confidence: {conf}")
except Exception as e:
    print(f"Error during prediction: {e}")
