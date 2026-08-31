# 🥗 Diet Recommendation App

A Python-based diet recommendation application developed as part of my learning journey with **Core Python**.

The application uses structured food and health-condition data to provide food recommendations based on user-selected health conditions and nutritional rules.

## ✨ Features

* Select one or multiple health conditions
* Rule-based food recommendations
* Nutrition-based food filtering
* Find common food recommendations across multiple conditions
* Search and filter recommended foods
* Display nutritional information
* Input validation
* Interactive interface using Streamlit
* Food and condition data stored separately using JSON

## 🛠️ Technologies Used

* **Python**
* **JSON**
* **Streamlit**

## 📂 Project Structure

```text
diet_app/
│
├── data/
│   ├── conditions.json
│   └── foods.json
│
├── diet_app/
│   └── recommendation.py
│
├── ui/
│   ├── __init__.py
│   ├── cards.py
│   ├── common_foods.py
│   ├── filters.py
│   ├── search.py
│   ├── sidebar.py
│   └── statistics.py
│
├── .gitignore
├── main.py
└── streamlit_app.py
```

## ⚙️ How It Works

The application follows a rule-based recommendation approach:

```text
User selects health conditions
            ↓
Condition rules are loaded
            ↓
Food data is loaded
            ↓
Foods are checked against the rules
            ↓
Matching foods are recommended
            ↓
Common foods are identified
            ↓
Results are displayed
```

For multiple selected conditions, the application identifies foods that satisfy the rules for all selected conditions.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nithyasreeb27-ai/diet_app.git
```

### 2. Navigate to the project

```bash
cd diet_app
```

### 3. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install streamlit
```

### 5. Run the application

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

## 📌 Project Status

This is the current **initial version** of the application, developed to apply and strengthen Core Python concepts through a practical project.

## 🔮 Future Plans

I plan to further develop this application by adding:

* BMI calculation
* More personalized meal planning
* Dietary preference and allergy filtering
* More comprehensive real-world nutrition data
* Backend integration
* Frontend development
* AI-assisted features

## ⚠️ Disclaimer

This application is a learning project and provides general food recommendations based on predefined rules and data. It is **not intended to provide medical diagnosis or replace professional medical or dietary advice**.

## 👩‍💻 Author

**Nithyasree B**

Built as part of my journey from learning Python fundamentals to developing practical applications.
