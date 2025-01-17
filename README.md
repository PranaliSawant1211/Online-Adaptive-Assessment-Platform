# SMART QUIZ: AI-powered Adaptive Assessment Platform

An intelligent platform built using Flask that delivers an adaptive assessment experience. The platform dynamically adjusts question difficulty based on user performance, ensuring a personalized and engaging testing process. The platform also incorporates a **Decision Tree** model for question selection, optimizing the assessment experience.

## 🚀 Features

- **Dynamic Difficulty Adjustment**: Questions are categorized as `easy`, `medium`, or `hard`, and the difficulty level adapts based on user responses.
- **Question Categorization**: Logical, reasoning, and aptitude questions are managed efficiently from a CSV dataset.
- **Real-time Scoring**: Scores are updated dynamically as users answer questions.
- **Performance Insights**: The platform supports tracking user performance to fine-tune difficulty.
- **Automation with Flask**: Backend powered by Flask, enabling a seamless user experience.

## 🛠️ Technologies Used
- **Model**: Decision Tree for adaptive question selection
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Data Storage**: CSV files for storing and categorizing questions
- **Libraries**: Flask, Python `csv` module
- **Deployment**: Local server with Flask (Debug Mode)

## 💡 Getting Started

### Prerequisites

- Python 3.x installed
- Flask installed (`pip install flask`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Online-Adaptive-Assessment-Platform.git
   cd Online-Adaptive-Assessment-Platform
2. Install dependencies:
   pip install -r requirements.txt
3.Run the application:
    python main.py
4. Access the platform:
     Open your browser and navigate to http://127.0.0.1:5000.
### Datasets
diff_data.csv: Contains questions with difficulty levels (easy, medium, hard) and categories (logical, reasoning, aptitude).
cat_data.csv: Provides predictions for categories to guide question selection.

