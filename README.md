# Containerized Machine Learning Inference API
**Project 2 for CS346 - January 2026**

## Project Overview
This project demonstrates an end-to-end Machine Learning pipeline. I developed a script to train a model, serialized it for production, and wrapped it in a Flask API served via a Docker container. This showcases the transition from "Data Science" to "Production Engineering."

## File Structure
* **`train_model.py`:** The training pipeline that pre-processes data and fits the algorithm (likely Scikit-Learn).
* **`model.pkl`:** The serialized model artifact, saved using Pickle for efficient loading.
* **`app.py`:** A Flask web server that loads the model and provides an API endpoint for real-time predictions.
* **`Dockerfile`:** Packages the Python environment, dependencies, and model into a portable image.

## Technical Skills
* **Model Serialization:** Saving trained models for persistence (`pickle`/`joblib`).
* **API Development:** Exposing ML capabilities via RESTful endpoints using **Flask**.
* **Containerization:** ensuring the model runs consistently across different environments using **Docker**.

## How to Run
1. **Train the Model:**
   Generates the `model.pkl` file using the training script.
   ```bash
   python train_model.py
