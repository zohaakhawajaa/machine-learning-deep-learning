# Machine Learning & Deep Learning

A structured, hands-on learning repository documenting my journey through classical machine learning, deep learning, computer vision, natural language processing, and time-series analysis.

The repository contains Jupyter notebooks, implementations, experiments, and practical exercises focused on understanding concepts through code.

## Repository Structure

```text
machine-learning-deep-learning/
│
├── supervised-learning/
│   ├── linear-regression/
│   ├── logistic-regression/
│   ├── decision-tree/
│   ├── random-forest/
│   └── xgboost/
│
├── unsupervised-learning/
│   ├── kmeans/
│   ├── pca/
│   ├── dbscan/
│   └── optics/
│
├── deep-learning/
│   ├── neural-networks/
│   ├── cnn/
│   ├── rnn/
│   ├── lstm/
│   └── gru/
│
├── nlp/
│   ├── tfidf/
│   ├── text-vectorization/
│   ├── embeddings/
│   └── rnn-text-classification/
│
└── time-series/
```

## Topics Covered

### Machine Learning

* Linear Regression
* Logistic Regression
* Decision Trees
* Random Forest
* XGBoost
* K-Means Clustering
* PCA
* DBSCAN
* OPTICS
* Model evaluation and preprocessing

### Deep Learning

* Neural Networks
* Multilayer Perceptrons
* MNIST Classification
* Convolutional Neural Networks (CNNs)
* Recurrent Neural Networks (RNNs)
* Long Short-Term Memory (LSTM)
* Gated Recurrent Units (GRUs)

### Computer Vision

* CNN-based image classification
* Fashion-MNIST
* Image preprocessing
* OpenCV
* YOLO-based computer vision experiments

### Natural Language Processing

* TF-IDF
* Text Vectorization
* Tokenization and vocabulary
* Word embeddings
* RNN-based text classification

### Time Series

Topics and implementations will be added as I progress through time-series analysis and forecasting.

## Learning Approach

Each notebook focuses on understanding the concept through implementation and experimentation.

Where applicable, notebooks follow:

```text
Concept
   ↓
Data Preparation
   ↓
Preprocessing
   ↓
Model Building
   ↓
Training
   ↓
Evaluation
   ↓
Conclusion
```

## Learning Roadmap

```text
Classical Machine Learning
          ↓
Deep Learning Fundamentals
          ↓
CNN
          ↓
RNN
          ↓
LSTM
          ↓
GRU
          ↓
NLP
          ↓
Time Series
```

## Setup

Create and activate a virtual environment, then install the required dependencies:

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Open the notebooks using VS Code or Jupyter and run the cells from top to bottom.

Some notebooks use TensorFlow and OpenCV and may require additional system or hardware configuration.

## Notes

* Dataset files, model checkpoints, virtual environments, and notebook runtime outputs should remain untracked.
* The notebooks are primarily educational and use small datasets for experimentation.
* Reported metrics should not be interpreted as production benchmarks.
* The repository will continue to evolve as new concepts and implementations are added.
