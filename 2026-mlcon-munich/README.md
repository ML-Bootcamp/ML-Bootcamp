# MLcon '26 - ML Bootcamp Labs

Hands-on, guided Jupyter notebooks for the MLcon '26 ML Bootcamp. Each lab walks
through a complete machine learning workflow with short tasks to complete as you
go. No prior ML experience is required.

## Labs

| # | Lab | Topic | Notebook |
|---|-----|-------|----------|
| 01 | Feature Engineering & Visualisation | Explore the Titanic dataset, visualise patterns, train a baseline model, and engineer new features to improve it. | [`labs/01-feature-engineering/lab_features_guided.ipynb`](labs/01-feature-engineering/lab_features_guided.ipynb) |
| 02 | Deep Learning | Build intuition for how a neural network is defined, trained, and debugged by classifying handwritten MNIST digits with PyTorch. | [`labs/02-deep-learning/lab_mnist_guided.ipynb`](labs/02-deep-learning/lab_mnist_guided.ipynb) |

### Lab 01 - Feature Engineering & Visualisation

Work through a complete ML workflow on the Titanic dataset:

1. Load and inspect the data
2. Visualise patterns and form hypotheses about useful features
3. Train a baseline model
4. Engineer a new feature and compare results
5. Reflect on what you learned

Built with `pandas`, `seaborn`, `matplotlib`, and `scikit-learn`. The dataset is
loaded directly via `seaborn`, no download required.

### Lab 02 - Deep Learning

Train a small neural network to recognise handwritten digits and learn how deep
learning models work in practice:

- How a model is defined and how many parameters it has
- What a loss function measures
- How a training loop works in code
- How to visualise training and inspect predictions
- The effect of hyperparameters (learning rate, epochs, batch size)
- Common failure modes: diverging training, overfitting, and underfitting

Built with `PyTorch` (`torch`, `torchvision`), `numpy`, and `matplotlib`. The
MNIST dataset is downloaded automatically by `torchvision` on first run.

---

## How to run the labs

You can run the labs in **Google Colab**, **locally**, or with **Docker**. Colab
requires no installation and is the fastest way to get started.

### Option 1 - Run in Google Colab

No installation needed, just click a link below, then run the cells top to
bottom. Colab already includes all required packages.

- **Lab 01 - Feature Engineering & Visualisation:**
  [Open in Colab](https://colab.research.google.com/github/davencyw/mlcon26-mlbootcamp-labs/blob/main/labs/01-feature-engineering/lab_features_guided.ipynb)
- **Lab 02 - Deep Learning:**
  [Open in Colab](https://colab.research.google.com/github/davencyw/mlcon26-mlbootcamp-labs/blob/main/labs/02-deep-learning/lab_mnist_guided.ipynb)

To open any notebook in Colab manually, prefix its GitHub URL with
`https://colab.research.google.com/github/`. Changes in Colab are not saved back
to the repository unless you explicitly save a copy to your own Google Drive or
GitHub.

> **Tip:** For faster training in Lab 02, enable a GPU in Colab via
> *Runtime → Change runtime type → Hardware accelerator → GPU* (optional; the lab
> runs fine on CPU).

### Option 2 - Run locally

**Prerequisites:** Python 3.10 or newer and `git`.

1. Clone the repository:

```bash
git clone https://github.com/davencyw/mlcon26-mlbootcamp-labs.git
cd mlcon26-mlbootcamp-labs
```

2. Create and activate a virtual environment:

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install the dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Launch Jupyter and open a lab:

```bash
jupyter lab
# or, if you prefer the classic interface:
jupyter notebook
```

Then open one of the notebooks in `labs/` and run the cells top to bottom.

> **Note:** The labs are CPU-friendly and do not require a GPU.

### Option 3 - Run with Docker

A `Dockerfile` is included that installs all dependencies and runs a JupyterLab
server, so you don't need to manage a local Python environment.

**Prerequisites:** [Docker](https://docs.docker.com/get-docker/) installed and running.

1. Build the image (run from the `2026-mlcon-munich/` directory):

```bash
docker build -t mlcon26-labs .
```

2. Run the container, mounting the current directory so notebook changes are
   saved back to your machine:

```bash
docker run -it --rm -v "$(pwd)":/app -p 8888:8888 mlcon26-labs
```

3. Open the JupyterLab URL printed in the terminal (it includes a login token,
   e.g. `http://127.0.0.1:8888/lab?token=...`) in your browser, then open a
   notebook in `labs/` and run the cells top to bottom.

> **Tip:** To get an interactive shell inside the container instead of launching
> JupyterLab directly, append `bash` to the run command and start the server
> manually with
> `jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root`.
