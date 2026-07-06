# 🚗 Smart Route Optimization System using Graph Theory

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Theory-orange)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-red)

## 📌 Project Overview

Finding the shortest route between two cities based only on distance is often not sufficient in real-world transportation systems. Travelers usually consider several factors before choosing a route, including travel time, fuel expenses, toll charges, and traffic conditions.

This project presents a **Smart Route Optimization System** that recommends the optimal route between two cities using **Dijkstra's Shortest Path Algorithm** while allowing optimization based on multiple transportation parameters.

---

## 🎯 Problem Statement

Develop a transportation route optimization system capable of identifying the best route between two cities by considering multiple optimization criteria instead of only geographical distance.

Optimization Parameters include:

- Distance
- Travel Time
- Fuel Cost
- Toll Tax

---

## 📊 Dataset

The original transportation dataset contained only:

- Source City
- Destination City
- Distance

Since these three features were insufficient for real-world route optimization, the dataset was enhanced through **feature engineering**.

Additional attributes include:

- Road Type
- Average Speed
- Traffic Condition
- Travel Time
- Fuel Cost
- Toll Tax
- Carbon Emission

Transportation-related attributes were generated using realistic assumptions and standard transportation formulas to simulate practical routing conditions.

---

# ⚙️ Feature Engineering

The following features were created:

| Feature | Method |
|----------|---------|
| Fuel Cost | Distance ÷ Mileage × Fuel Price |
| Toll Tax | Distance × Toll Rate |
| Carbon Emission | Distance × Emission Factor |
| Travel Time | Converted from HH:MM format into numerical hours |

---

# 🧠 Algorithm Used

The transportation network was modeled as an **undirected weighted graph** where:

- Cities represent Nodes
- Roads represent Edges
- Different optimization parameters act as Edge Weights

The shortest path is computed using:

**Dijkstra's Shortest Path Algorithm**

The algorithm allows optimization based on:

- Shortest Distance
- Fastest Route
- Lowest Fuel Cost
- Lowest Toll Tax

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NetworkX
- Matplotlib
- Jupyter Notebook

---

# 📈 Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Graph Construction
5. Dijkstra's Algorithm
6. Multi-Criteria Route Optimization
7. Route Visualization
8. Exploratory Data Analysis

---

# 🚀 Features

✔ Smart Route Recommendation

✔ Multi-Criteria Optimization

✔ Graph Based Transportation Network

✔ Route Visualization

✔ Interactive User Input

✔ Transportation Cost Estimation

---

# 📷 Sample Output

The project displays:

- Best Route
- Total Distance
- Travel Time
- Fuel Cost
- Toll Tax
- Highlighted Route Visualization

---

# 📂 Project Structure

```
smart-route-optimization/

│── data/

│── notebook/

│── images/

│── README.md

│── requirements.txt
```

---

# 📌 Future Improvements

- Live Google Maps Integration
- Real-Time Traffic
- Weather-Based Routing
- Electric Vehicle Optimization
- Streamlit Web Application
- Multi-Stop Route Planning

---

# 👨‍💻 Author

**Vibhav Keshar**

B.Tech Computer Science (Data Science)

University of Petroleum and Energy Studies (UPES)

---

## ⭐ If you found this project useful, consider giving it a Star.
