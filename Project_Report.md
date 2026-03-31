# AgriPulse: Final Project Report

**AgriPulse** is a unified AI application designed to support the modern farmer by encapsulating multiple Artificial Intelligence domains into a single, cohesive decision-making workflow. This report details how AgriPulse applies each fundamental concept from the AI Course Syllabus.

---

## 1. Goal-Based Rational Agent (Module 1)
**Concept Implemented:** The core architecture of AgriPulse is built using a Goal-Based Rational Agent (`AgriPulseAgent`).
- **Goal:** The agent’s explicit objective is to maximize the farmer's profit (`self.profit_score`). 
- **Environment:** Farm conditions represent a *Stochastic* environment, meaning that percepts (like exact weather, market price, or spontaneous pest outbreaks) cannot be predicted with 100% certainty. 
- **Rational Actions:** Instead of following static rules, the agent receives a complex percept map (comprising weather data, imagery, and audio) and sequentially evaluates predictions, calculates risk, triggers logic constraints, and subtracts cost-associated penalties (like fuel) before maximizing the finalized profit yield.

## 2. Transfer Learning via Neural Networks (Module 2 & 5)
**Concept Implemented:** In the `diagnostic_engine.py` component, the AI analyzes visual percepts of crops.
- **Implementation:** We leveraged TensorFlow/Keras and utilized **MobileNetV2**. Since training a deep CNN from scratch requires massive computation and data, *Transfer Learning* allows our agent to use pre-learned image features (weights from ImageNet) as a starting point. It then applies this rich feature extraction to identify standard ailments like 'leaf_blight' or 'mildew'.

## 3. First-Order Logic Expert System (Module 2 & 5)
**Concept Implemented:** Prolog-based Expert System using `pytholog` (found in `diagnostic_engine.py`).
- **Implementation:** If the computer vision model detects a disease, it cannot arbitrarily decide the treatment. It triggers the internal Knowledge Base containing *First-Order Logic* rules:
  ```prolog
  disease_treatment(leaf_blight, chemical, fungicide_spray).
  disease_treatment(leaf_blight, organic, neem_oil_spray).
  ```
  The agent queries the KB mapping the detected disease state and the farmer's preference (e.g., organic) to definitively resolve complex operational policy constraints.

## 4. Machine Learning: Prediction & Clustering (Module 3 & 4)
**Concept Implemented:** A suite of fundamental algorithms mapping directly to real decision branches in `prediction_engine.py`.
- **Linear Regression:** Learns a linear relationship between features (Rainfall and Soil pH) and the continuous target variable (`Crop Yield`).
- **K-Means Clustering:** Performs *Unsupervised Learning* by partitioning unlabeled 3-dimensional data (Nitrogen, Phosphorus, Potassium levels) into 3 distinct logical "Nutrient Zones", creating discrete actionable clusters out of continuous sensor data.

## 5. Bayesian Inference / Probability (Module 3 & 4)
**Concept Implemented:** Bayes' Theorem is used to compute logical uncertainty. 
- **Implementation:** In a stochastic environment, a pest attack isn't certain. The `PredictionEngine` evaluates `P(Pest | High Humidity)`. By taking the historical prior probability of pests `P(Pest) = 0.30` and the likelihood of high humidity given pests, Bayes Rule yields the exact probabilistic risk in real-time, allowing the agent to lower its projected yield dynamically if it assumes high risk and lack of preventative treatment.

## 6. A* Search Algorithm (Module 2)
**Concept Implemented:** Finding optimal transport logistics via `logistics_engine.py`.
- **Implementation:** Sending harvest to local points (Mandis) is modeled as a geographic Graph. Breadth-First-Search is too inefficient and Dijkstra doesn't have direction. **A* Search** is implemented utilizing an admissible straight-line heuristic `h(n)` to guide the search path toward the specific Mandi, minimizing the actual fuel cost `g(n)` without redundantly exploring the whole farm graph.

## 7. Natural Language Processing (Module 5)
**Concept Implemented:** NLP Sentiment Analysis interacting with Human percepts (`feedback_engine.py`).
- **Implementation:** A simple script utilizing `TextBlob` parses the semantic polarity of a farmer's voice note transcript.
- **Workflow Impact:** By evaluating unstructured text data (a complaint about unpredictable weather or bugs), the engine computes its polarity. A negative polarity overrides the agent's internal state into "low risk tolerance," proving the agent can adapt intelligently to qualitative human sentiment.

---

### Conclusion
By unifying Search, First-Order Logic, Bayesian Inference, Machine Learning, Deep Computer Vision, and NLP under the umbrella of a Rational Agent paradigm, **AgriPulse** represents a fully end-to-end holistic AI architecture. No module operates offline—every calculation dynamically shapes the final simulated profit score.
