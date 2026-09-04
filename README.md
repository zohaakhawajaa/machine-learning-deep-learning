# Machine Learning and Deep Learning Algorithms

A hands-on notebook repository for learning machine learning, deep learning,
computer vision, natural language processing, and time-series algorithms.
The layout follows a progression from classical machine learning to neural
networks and sequence models.

## Repository Structure

```text
machine-learning-deep-learning/
|
|-- supervised-learning/
|   |-- linear-regression/
|   |-- logistic-regression/
|   |-- decision-tree/
|   |-- random-forest/
|   |-- xgboost/
|
|-- unsupervised-learning/
|   |-- kmeans/
|   |-- pca/
|   |-- dbscan/
|   |-- optics/
|
|-- deep-learning/
|   |-- neural-networks/
|   |-- cnn/
|   |-- rnn/
|   |-- lstm/
|   |-- gru/
|
|-- nlp/
|   |-- tfidf/
|   |-- text-vectorization/
|   |-- embeddings/
|   |-- rnn-text-classification/
|
|-- time-series/
```

## Current Implementations

### Deep learning

- `deep-learning/neural-networks/`: a first neural network, multilayer
  perceptron, and MNIST classification notebooks.
- `deep-learning/cnn/`: CNN examples for image classification, Fashion-MNIST,
  and OpenCV camera workflows.
- `deep-learning/rnn/`: SimpleRNN examples and an imbalanced classification
  experiment.

### NLP

- `nlp/text-vectorization/`: text preprocessing and vectorization experiments.
- `nlp/rnn-text-classification/`: binary text classification using a
  `TextVectorization` layer and recurrent models.
- `nlp/tfidf/` and `nlp/embeddings/`: reserved for focused implementations of
  TF-IDF and learned word representations.

### Classical machine learning and time series

The classical machine-learning and time-series directories are intentionally
present as an organized roadmap. Add one notebook per algorithm with sections
for the idea, data preparation, training, evaluation, and a short conclusion.
This keeps unfinished topics visible without presenting them as implemented.

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv

# Windows PowerShell
.venv\\Scripts\\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Open the notebooks in VS Code or Jupyter and run cells from top to bottom.
Some notebooks use TensorFlow and OpenCV, so a compatible Python environment
and camera permissions may be required.

## Learning Order

1. Start with `deep-learning/neural-networks/`.
2. Continue with `deep-learning/cnn/` for image data.
3. Study `nlp/text-vectorization/` before the text-classification notebook.
4. Continue with `deep-learning/rnn/` and the NLP recurrent classifier.
5. Fill the classical ML and time-series roadmap as new notebooks are added.

## Notes

- Dataset files, model checkpoints, virtual environments, and notebook runtime
  output should remain untracked.
- The examples are educational and use small datasets; their metrics should
  not be treated as production benchmarks.
