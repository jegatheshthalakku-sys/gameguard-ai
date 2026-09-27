# 🎮 GameGuard AI

GameGuard AI is a gaming analytics system that predicts player churn and detects toxic chat behavior.

## 🚀 Features

- 🎯 Player churn prediction
- 📊 Player behavior analysis
- 💬 Toxicity detection
- 🚨 Automatic toxicity reporting
- 🌐 Flask web dashboard

## 🛠️ Technologies

- Python
- Flask
- Pandas
- Scikit-learn
- Random Forest
- HTML
- CSS

## 🔮 Churn Prediction

The system predicts whether a player is at risk of leaving the game based on:

- Matches played
- Average session duration
- Days since last login
- Average kills
- Win rate

## 💬 Toxicity Detection

The system analyzes chat messages and detects predefined abusive or toxic words.

When toxic content is detected, the message is flagged and a toxicity report is generated.

## 📁 Project Structure

```text
gameguard-ai/
├── app.py
├── churn_model.py
├── churn_model.pkl
├── toxicity.py
├── report_generator.py
├── requirements.txt
├── data/
├── templates/
└── static/