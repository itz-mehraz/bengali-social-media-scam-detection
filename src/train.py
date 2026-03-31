import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

# Load datasets
data = pd.read_csv("data/fake_job_postings.csv")
fb_data = pd.read_csv("data/fb_job_post_dataset.csv")

# Prepare text
data["text"] = (
    data["title"].fillna("") + " " +
    data["description"].fillna("") + " " +
    data["requirements"].fillna("") + " " +
    data["company_profile"].fillna("") + " " +
    data["benefits"].fillna("")
)

fb_data["text"] = fb_data["post_text"].fillna("")

# Split Facebook dataset
fb_train, fb_test = train_test_split(
    fb_data,
    test_size=0.2,
    random_state=42,
    stratify=fb_data["label"]
)

# Final training data
final_train_data = pd.concat([
    data[["text", "fraudulent"]].rename(columns={"fraudulent": "label"}),
    fb_train[["text", "label"]]
], ignore_index=True)

# Vectorize
tfidf = TfidfVectorizer(max_features=8000, ngram_range=(1, 2))
X_train = tfidf.fit_transform(final_train_data["text"])
y_train = final_train_data["label"]

# Train model
model = LinearSVC(class_weight="balanced", max_iter=5000)
model.fit(X_train, y_train)

# Save files
with open("models/best_svm_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/final_tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(tfidf, f)

print("Training complete. Model and vectorizer saved.")
