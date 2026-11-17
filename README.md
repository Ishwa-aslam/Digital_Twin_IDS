# Digital Twin-Based Intrusion Detection System for Industrial Control Systems

## Project Overview
This project presents a simulated Digital Twin-Based Intrusion Detection System (DT-IDS) for an Industrial Control System (ICS).

A water tank system is used as a digital twin to generate normal and abnormal sensor readings. Machine learning models are trained to classify system behaviour as Normal or Anomaly.

The project also demonstrates Operating System concepts such as process management, multithreading, synchronization, CPU scheduling, memory monitoring, and Inter-Process Communication (IPC).

**Note:** This is an academic simulation using locally generated data. It does not connect to or perform attacks against real industrial control systems.

## Objectives
- Develop a simulated water tank Digital Twin.
- Generate normal and simulated anomalous sensor data.
- Apply machine learning for anomaly detection.
- Compare different supervised machine learning classifiers.
- Demonstrate Operating System concepts.
- Evaluate model performance and resource usage.

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Psutil
- Git and GitHub

## Machine Learning Models
The following supervised learning models are implemented:
1. Logistic Regression
2. Decision Tree
3. Random Forest

## Simulated Anomaly Types
- Sensor Spike
- Abnormal Flow
- Valve Mismatch

## Operating System Concepts
- Process Management
- Multithreading
- Synchronization using Locks
- Inter-Process Communication (IPC)
- FCFS CPU Scheduling Simulation
- CPU and Memory Monitoring
- File Handling and Logging

## Experiments
The project includes six experiment areas:

1. Normal operation of the simulated water tank.
2. Generation and analysis of simulated anomalies.
3. Comparison of supervised machine learning models.
4. Comparison of process, control, and combined feature groups.
5. Evaluation of training time, inference time, CPU time, and memory usage.
6. Robustness evaluation using noisy data, missing values, and imbalanced training data.

## Project Structure

```text
Digital_Twin_IDS/
│
├── data/
├── figures/
├── logs/
├── results/
├── src/
│   ├── digital_twin.py
│   ├── prepare_dataset.py
│   ├── preprocessing.py
│   ├── train_models.py
│   ├── feature_experiment.py
│   ├── resource_experiment.py
│   ├── robustness_experiment.py
│   ├── os_monitor.py
│   ├── os_concepts.py
│   ├── cpu_scheduling.py
│   ├── eda.py
│   ├── plot_data.py
│   └── main.py
│
└── .gitignore
```

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/Ishwa-aslam/Digital_Twin_IDS.git
```

### 2. Open the project folder

```bash
cd Digital_Twin_IDS
```

### 3. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install required libraries

```bash
pip install numpy pandas matplotlib scikit-learn psutil
```

### 5. Run the project

```bash
python src/main.py
```

Follow the menu displayed in the terminal to run individual modules.

## Results
The experiments generate evaluation results, comparison tables, resource measurements, and graphs.

The model evaluation includes:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Training Time
- Inference Time
- CPU and Memory Usage

All reported results are based on the project's simulated dataset and experimental environment.

## Limitations
- The dataset is relatively small and synthetically generated.
- The system has not been tested on a real industrial control system.
- Results may differ with larger and more diverse datasets.
- The experiments demonstrate an academic prototype, not a production-ready security solution.

## Project Type
Academic Assignment based on Operating-system concepts integrated with AI/ML — BE Computer Systems Engineering, 5th Semester.

## Author
Ishwa Aslam
