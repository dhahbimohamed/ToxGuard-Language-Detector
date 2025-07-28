# 🔥ToxGuard :  Flame Detector for Games

## 🎮 Why I Built This

As a regular **League of Legends** player, I’ve seen how fast chat can turn toxic — insults, rage, and hate speech can ruin the experience. I wanted to build something **useful and real**: a **Flame Detector** that analyzes chat messages and flags offensive or hateful content in real time. 

This project uses **Machine Learning** to detect:
- 🟥 Hate Speech
- 🟧 Offensive Language
- 🟩 Neutral or Friendly Text

Whether you're a game developer, a mod, or just someone tired of toxicity — this tool can help make games safer and chats cleaner.


## 🚀 How to Run :  [Click here to open the live app](https://toxguard-language-detector-qmke9pkvajz5by9idkhezj.streamlit.app/)


---

## 🧠 What It Does

- Takes a text input (like an in-game chat message)
- Cleans and processes it using **TF-IDF** vectorization
- Uses a **Logistic Regression** model trained on a real hate speech dataset
- Predicts whether it's:
  - **Hate Speech** (very toxic)
  - **Offensive** (mild flame, insults, aggressive tone)
  - **Neutral** (normal or friendly)

---

## 🛠️ How I Built It

### 1. Dataset
- **Source**: [Hate Speech and Offensive Language Dataset (Davidson et al.)](https://github.com/t-davidson/hate-speech-and-offensive-language)
- Cleaned raw tweets
- Focused on the `class` column with 3 values:  
  `0 = hate speech`, `1 = offensive`, `2 = neither`

### 2. Preprocessing
- Lowercased all text
- Removed links, mentions, hashtags, punctuation, and extra spaces
- Used `TF-IDF Vectorizer` for text representation

### 3. Model Training
- Trained a **Logistic Regression** classifier
- Used **oversampling** to balance underrepresented classes (e.g. hate speech)
- Achieved:
  - **87% Accuracy**
  - **Great recall for hate & offensive content**

### 4. Web App
- Built with **Streamlit**
- Custom **dark modern-inspired theme**
- Interactive interface with smooth styling and clean feedback messages

---

### 🧩 Requirements
```bash
pip install streamlit scikit-learn joblib pandas numpy
