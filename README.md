# 😀😐😞 Kid-Safe Text-Mood Detector

A simple Streamlit web app designed for students (ages 12-16) to learn the basics of Sentiment Analysis, web development, and digital safety. The app takes a user's sentence and returns a simple, kid-friendly emoji (😀, 😐, or 😞) with a one-line explanation.

**Live App Link:** [https://rehan1608-rehan-rehan-mood2emoji-app-mgi5ji.streamlit.app/](https://rehan1608-rehan-rehan-mood2emoji-app-mgi5ji.streamlit.app/)

---

## 🛠️ Setup and Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rehan1608/rehan-rehan-mood2emoji.git](https://github.com/rehan1608/rehan-rehan-mood2emoji.git)
    cd rehan-rehan-mood2emoji
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    Your app will open in your web browser!

---

## 📚 What This Project Teaches (Learning Notes)

This project is a great entry point for several key computer science concepts:

* **Sentiment Analysis:** This is the core idea of "Natural Language Processing" (NLP). Students learn that computers don't "understand" text but can be taught to classify it based on patterns and pre-defined scores.
* **How Computers "Read":** We use the **TextBlob** library, which simplifies this process. It works like a giant dictionary where words have been pre-scored for positivity/negativity (this is called "polarity").
    * `"happy"` has a score of `+0.8`
    * `"bad"` has a score of `-0.7`
* **Conditional Logic (If/Else):** The app's entire "brain" is just a simple `if/elif/else` statement. Students can see exactly how we turn a number (the polarity score) into a decision (an emoji).
* **Digital Safety:** The app includes a profanity filter. This is a crucial, non-negotiable step in building public-facing apps, especially for kids. It teaches the importance of "failing safely" by providing a neutral response instead of processing bad words.
* **Basic Web Development:** Students see how a simple Python script (`app.py`) can be instantly turned into an interactive website using **Streamlit**.

---

## 👨‍🏫 How to Teach This in 60 Minutes

Here is a sample lesson plan for a 60-minute class or workshop:

**1. (10 mins) Intro: "Can a computer have feelings?"**
* Show the live app. Let 2-3 students try it with different sentences (one happy, one sad, one neutral).
* Ask the class: "How does it work? Is it magic? Is it *thinking*?"
* Discuss that it's not "feeling," it's "calculating."

**2. (15 mins) Core Concept: "The 'Score' of a Word"**
* On a whiteboard, draw a number line from -1 to +1.
* Ask students to place words on it. Where does "great" go? (+0.8). Where does "angry" go? (-0.7). Where does "computer" go? (0.0).
* Explain this is called **Polarity**, and a library called `TextBlob` has already scored thousands of words for us.
* Show this line of code from `app.py`: `polarity = blob.sentiment.polarity`

**3. (20 mins) Code-Along: "The Emoji Brain" (The `if/else` logic)**
* Focus on the `get_mood` function in `app.py`.
* Ask the class: "If our score is `0.9`, what emoji should we show?" (Happy 😀)
* "What if the score is `> 0.2`?" (Happy 😀)
* "What if the score is `< -0.2`?" (Sad 😞)
* "What about everything else in the middle?" (Neutral 😐)
* Live-code or review this `if/elif/else` block so they see how their logic becomes Python code.

**4. (10 mins) The "Teacher Mode" & Safety First**
* Toggle on the "Teacher Mode" checkbox in the app.
* Walk through the flowchart.
* Point to the "Safety Check" step. Ask: "Why do we check for bad words *first*? What happens if we don't?" This opens a good discussion on digital citizenship.

**5. (5 mins) Wrap-up: "How can we trick it?"**
* Ask students for sentences that might "trick" the app.
* **Sarcasm** is the best example: *"Oh, great. I just failed my test."*
* The app will see "great" and think it's happy, but a human knows it's sad.
* This teaches the app's biggest limitation.

---

## ⚠️ Known Limitations

This simple app is great for learning but has clear limitations:

1.  **It can't understand sarcasm:** A sentence like "I *love* getting homework" will be seen as positive.
2.  **It doesn't get context:** It scores word by word. It doesn't understand the complex relationship *between* words.
3.  **The word list is limited:** `TextBlob`'s dictionary is good but basic. It may not understand new slang or complex academic words.
4.  **The safety filter is basic:** A simple profanity filter can be bypassed with creative spelling (e.g., "sh!t").