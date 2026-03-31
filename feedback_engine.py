from textblob import TextBlob

class FbkEngine:
    def __init__(self):
        print("[FbkEngine] NLP Init...")

    def get_sent(self, text):
        tb = TextBlob(text)
        pol = tb.sentiment.polarity
        
        if pol > 0.1:
            st = "Sat"
        elif pol < -0.1:
            st = "Stressed"
        else:
            st = "Neut"
            
        print(f"[FbkEngine] Sent: {st} ({pol:.2f})")
        return st, pol
