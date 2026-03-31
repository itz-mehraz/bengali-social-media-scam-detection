import pickle

with open("models/best_svm_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/final_tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

def predict_post(text):
    text_vec = tfidf.transform([text])
    pred = model.predict(text_vec)[0]
    return "Fake Job Scam" if pred == 1 else "Real Job"

# Example
sample_text = "Earn money from home. No experience needed. Inbox now."
print("Prediction:", predict_post(sample_text))
