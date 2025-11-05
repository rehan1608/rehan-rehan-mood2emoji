import streamlit as st
from textblob import TextBlob
from better_profanity import profanity

# --- Configuration ---
st.set_page_config(page_title="Text-Mood Detector", page_icon="😀")

# --- Safety & Analysis Logic ---

@st.cache_resource
def load_profanity_filter():
    """Loads the profanity filter once and caches it."""
    profanity.load_censor_words()
    return profanity

def is_safe(sentence: str) -> bool:
    """Checks if a sentence contains profanity."""
    filter = load_profanity_filter()
    return not filter.contains_profanity(sentence)

def get_mood(sentence: str) -> (str, str):
    """
    Analyzes a sentence and returns a kid-friendly emoji and explanation.
    """
    # 1. Handle empty or very short input
    if not sentence or len(sentence.split()) < 2:
        return ("😐", "Please type a full sentence so I can understand the feeling.")

    # 2. Safety Check
    if not is_safe(sentence):
        return ("😐", "Hmm, I'm not sure about those words. Let's try another sentence!")

    # 3. Sentiment Analysis
    try:
        blob = TextBlob(sentence)
        # Polarity is a score from -1.0 (very negative) to 1.0 (very positive)
        polarity = blob.sentiment.polarity

        # 4. Convert score to emoji
        if polarity >= 0.2:
            return ("😀", "That sounds happy!")
        elif polarity <= -0.2:
            return ("😞", "That sounds a bit sad or angry.")
        else:
            return ("😐", "That sounds neutral.")
            
    except Exception as e:
        print(f"Error: {e}")
        return ("😐", "I'm having a little trouble understanding. Please try again.")

def show_teacher_mode():
    """Displays the 'How it Works' diagram and explanation."""
    st.subheader("How does this app 'feel' emotions?")
    st.write("""
    This app doesn't *feel* anything! It's just very good at math.
    It uses a library called **TextBlob** which has a built-in dictionary
    where many words are already given a "polarity" score.
    
    * Positive words (like "happy", "great", "love") have a score **> 0**.
    * Negative words (like "sad", "bad", "angry") have a score **< 0**.
    * Neutral words (like "table", "the", "is") have a score of **0**.
    
    The app averages the scores of all the words in your sentence to get a
    final score. Then, it uses simple `if/else` logic to pick an emoji.
    """)
    
    # A simple diagram using Graphviz
    st.graphviz_chart('''
    digraph G {
        rankdir="TB";
        node [shape=box, style=rounded, fontname="Arial"];
        
        "Your Sentence" [shape=ellipse];
        "Safety Check" [shape=diamond];
        "Analyze Polarity (TextBlob)" [shape=box];
        "Result Emoji" [shape=ellipse, style=filled, fillcolor=lightblue];
        
        "Your Sentence" -> "Safety Check";
        "Safety Check" -> "Analyze Polarity (TextBlob)" [label="  Safe Words "];
        "Safety Check" -> "Result Emoji" [label="  Bad Words  "];
        
        subgraph cluster_logic {
            label = "Decision Logic";
            fontname="Arial";
            "Score > 0.2" [shape=diamond];
            "Score < -0.2" [shape=diamond];
            
            "Analyze Polarity (TextBlob)" -> "Score > 0.2";
            "Score > 0.2" -> "Result Emoji" [label=" Yes (Happy 😀)"];
            "Score > 0.2" -> "Score < -0.2" [label=" No"];
            
            "Score < -0.2" -> "Result Emoji" [label=" Yes (Sad 😞)"];
            "Score < -0.2" -> "Result Emoji" [label=" No (Neutral 😐)"];
        }
    }
    ''')

# --- Main Web App UI ---

# 1. Header
st.title("😀😐😞 Text-Mood Detector")
st.write("Type a sentence below and I'll guess the mood! (Great for students 12-16)")

# 2. Input Box
user_input = st.text_input("How are you feeling today?", "I love learning about code!")

# 3. Analyze Button
if st.button("Analyze Mood"):
    if user_input:
        # Get the mood
        emoji, explanation = get_mood(user_input)
        
        # Display the result
        st.markdown(f"<h1 style='text-align: center; font-size: 6em;'>{emoji}</h1>", unsafe_allow_html=True)
        st.subheader(f"**Explanation:** {explanation}")
    else:
        st.warning("Please type a sentence first.")

# 4. Optional Teacher Mode
st.divider()
if st.checkbox("Show 'Teacher Mode' (How it works)"):
    show_teacher_mode()