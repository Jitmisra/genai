# Intelligent EV Charging Demand Prediction & Agentic Infrastructure Planning

## Project Overview

This project focuses on building an AI-driven analytics system for electric vehicle (EV) infrastructure planning.

This repository contains the deliverables for **Milestone 1**, where we used classical machine learning techniques to predict EV charging demand using historical charging station usage, time, and location data. We built a data preprocessing pipeline, calibrated a macroscopic demand model, and designed an interactive dashboard to visualize demand usage trends and predictive simulations.

The project addresses a real-world sustainability problem and demonstrates applied machine learning and system deployment.

## Key Features (Milestone 1)

- **Analytics Dashboard**: Interactive visualizations showing Hourly Trends, City-wise Demand, Weekly Distribution, Weather Impact, Load Variance, and a Correlation Heatmap.
- **ML Pipeline**: A robust `RandomForestRegressor` trained on aggregated macroscopic data (Time, Weather, Battery Capacity) to predict total charging `Total_Demand`.
- **Predictive Simulation**: An interactive forecasting tool allowing users to simulate aggregate hourly load based on specific environmental and temporal scenarios.

## Tech Stack

- **Language**: Python
- **UI Framework**: Streamlit
- **Machine Learning**: Scikit-Learn
- **Data Visualization**: Plotly
- **Data Manipulation**: Pandas, NumPy

## Team Members

- **Anwesha Adhikari** (2401010091) - _Leader_
- **Anusha Prathapani** (2401010344)
- **Kartikey Gupta** (2401010214)
- **Agnik Misra** (2401010044)

## Demo & Verification

- **Live Application**: [Streamlit Community Cloud Deployment](https://7yfhuhascbpnkozy5amork.streamlit.app/)
- **Video Link**: [Watch the Presentation](https://drive.google.com/file/d/1R0HBjQRMv0RDgfnWBIUpA4S4B2I11B7H/view?usp=sharing)
