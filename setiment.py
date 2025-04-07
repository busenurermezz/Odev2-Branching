def analyze_sentiment(text):
    positive_words = ["good", "happy", "great", "love", "awesome"]
    negative_words = ["bad", "sad", "terrible", "hate", "awful"]

    score = 0
    for word in text.lower().split():
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    if score > 0:
        return "Pozitif"
    elif score < 0:
        return "Negatif"
    else:
        return "Nötr"

# Örnek kullanım
if __name__ == "__main__":
    print(analyze_sentiment("I love this project, it is awesome!"))
