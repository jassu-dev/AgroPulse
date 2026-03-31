# AgriPulse AI

> **AgriPulse** is an intelligent, Goal-Based Rational Agent designed to maximize a farmer's net profit. It continuously simulates a stochastic agricultural environment—balancing crop yield predictions, market risks, pest logic, and intelligent transportation routing into a single terminal application.

This project was engineered to synthesize the five foundational modules of Artificial Intelligence into one cohesive application for agricultural optimization.

---

## What Does This Project Do?

Imagine a digital farming assistant that:

1. **Listens to the farmer:** Analyzes voice transcripts using NLP to gauge the farmer's risk tolerance.
2. **Predicts the yield:** Uses Linear Regression and K-Means Clustering on soil data (pH, Rainfall, N/P/K) to predict how many tons of a crop will grow and what fertilizer zone it needs.
3. **Diagnoses diseases:** Uses Deep Learning (MobileNetV2) computer vision to scan physical photos of crop leaves for diseases.
4. **Prescribes treatments:** Feeds the visual diagnosis into a Prolog (First-Order Logic) Expert System to get an exact organic or chemical treatment.
5. **Routes the delivery:** Calculates the absolute cheapest gas route to deliver the harvest to market using the A\* Graph Search Algorithm.

All of this happens autonomously in a single execution loop!

---

## Project Structure

To run this project correctly, your folder must look exactly like this:

```text
AgriPulse/
│
├── diagnostic_engine.py    # Deep Learning (MobileNetV2) & Prolog Logic
├── prediction_engine.py    # Linear Regression, K-Means, Bayes Theorem
├── logistics_engine.py     # A* Graph Search
├── feedback_engine.py      # NLP Sentiment Analysis
├── main.py                 # The Goal-Based Rational Agent (Orchestrator)
├── requirements.txt        # Python Dependencies
│
└── data/
    ├── Crop_recommendation.csv    # 2200-row Kaggle Soil/Crop database
    └── PlantVillage/              # Physical JPG leaf images for computer vision
        ├── Tomato_Late_blight/
        ├── Potato___Early_blight/
        ├── Tomato_healthy/
        └── ... (etc)
```

---

## Setup & Installation (Step-by-Step)

If you have never run this project before, follow these steps exactly:

### 1. Prerequisites

Ensure you have **Python 3.8+** installed on your system.
_(Optional but recommended): Create a virtual environment._

```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# source venv/bin/activate    # On Mac/Linux
```

### 2. Install Dependencies

Install all the required machine learning, natural language, and logic libraries using `pip`:

```bash
pip install -r requirements.txt
```

_(Note: This downloads TensorFlow. If you see a warning about GPU support on Windows, it is completely normal and the code will still run perfectly on your CPU)._

### 3. Add The Datasets

The AI models require real-world data to run! Download the following and place them in the `data/` directory:

1. **Tabular Data:** Download the [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) from Kaggle. Ensure `Crop_recommendation.csv` is actively inside the `data/` folder. The Prediction Engine will parse its rows mathematically.
2. **Image Data:** Download the [PlantVillage Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset). Extract it so the `PlantVillage` directory is placed inside the `data/` folder. The Diagnostic Engine will actively open random JPGs from these sub-folders to run real-time inference checks!

---

## How To Run

Once your dependencies and data folders are set up, run the execution orchestrator:

```bash
python main.py
```

### Understanding The Output

The terminal will print a sequence of logs as each AI sub-module completes its task. It will output a summary showing exactly what the Agent decided to do to maximize profit:

```text
[Agent] Parsing environment percepts...
[Diagnostic] Loaded: <random_leaf>.JPG (Tomato_Early_blight)
[Diagnostic] Detect: LEAF_BLIGHT
[Diagnostic] T-Rec: neem_oil_spray
[LogEngine] Best Route: Farm->C1->M1 (Cost: 40)

--- FINAL ACTIONS ---
1. Mode: high risk.
2. Zone: Zone A.
3. Treatment: neem_oil_spray.
4. Route: Farm->C1->M1.
-> Net Profit: $3601.19
```

---

## AI Module Breakdown (For Graders/Reviewers)

For a technical review of the algorithms used, here is how the syllabus directly maps to the Python code:

| AI Concept                  | Algorithm Used                   | File Location                                 | Purpose                                        |
| :-------------------------- | :------------------------------- | :-------------------------------------------- | :--------------------------------------------- |
| **Search & Optimization**   | A\* Graph Search Heuristics      | `logistics_engine.py`                         | Finds the cheapest route to market.            |
| **Logic & Expert Systems**  | First-Order Logic (Pytholog)     | `diagnostic_engine.py`                        | Queries rules to prescribe crop treatments.    |
| **Probabilistic Reasoning** | Bayesian Event Logic             | `prediction_engine.py`                        | Computes exactly P(Pest Attack \| Humidity).   |
| **Machine Learning**        | Linear Regression & K-Means      | `prediction_engine.py`                        | Regresses Yield metrics & clusters NPK zones.  |
| **Advanced AI / NLP**       | MobileNetV2 (CNN) + TextBlob NLP | `diagnostic_engine.py` & `feedback_engine.py` | Runs deep-learning perception on data streams. |
