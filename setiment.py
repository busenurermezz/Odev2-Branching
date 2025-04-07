def analyze_sentiment(text):
    positive_words = ["good", "happy", "great", "love", "awesome", "fantastic", "excellent"]
    negative_words = ["bad", "sad", "terrible", "hate", "awful", "worst", "poor"]

    words = text.lower().split()
    score = 0
    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    # Normalize score
    if len(words) > 0:
        score = score / len(words)

    if score > 0.1:
        return "Pozitif"
    elif score < -0.1:
        return "Negatif"
    else:
        return "Nötr"

# Örnek
if __name__ == "__main__":
    print(analyze_sentiment("This is the worst project I have ever seen."))
