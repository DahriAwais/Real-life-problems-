import re

def comment_analyze(comment):
    # Define lists of keywords for sentiment analysis
    bad_keywords = ["bad", "not", "not good", "ugly", "worst"]
    good_keywords = ["good", "nice", "yes", "wow", "cool", "beautiful"]
    neutral_keywords = ["huh", "what", "idk"]

    # Check for sentiment
    sentiment = None
    for word in comment.split():
        if word.lower() in bad_keywords:
            sentiment = "negative"
            break
        elif word.lower() in good_keywords:
            sentiment = "positive"
            break
        elif word.lower() in neutral_keywords:
            sentiment = "neutral"
            break

    if sentiment:
        print(f"Your comment is {sentiment} :) ")
    else:
        print("Unable to determine sentiment. Can you provide more context?")

    # Extract keywords
    keywords = [word for word in comment.split() if word.lower() in (bad_keywords + good_keywords + neutral_keywords)]

    if keywords:
        print("Keywords found:", keywords)
    else:
        print("No specific keywords identified.")

    # Identify emojis
    emojis = re.findall(r'[^\w\s,]', comment)
    
    if emojis:
        print("Emojis found:", emojis)
    else:
        print("No emojis found.")

    # Potential trends (simple check for hashtags)
    hashtags = re.findall(r'#\w+', comment)
    
    if hashtags:
        print("Trends identified:", hashtags)
    else:
        print("No trends identified.")

# Example usage
user_comment = input("Enter your comment: ")
comment_analyze(user_comment)

