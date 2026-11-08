# DSF Group Project — User Guide

**Project:** Supermarket Demand Forecasting and Food Waste Reduction  
**Dataset:** FreshRetailNet-50K  
**Development environment:** Python, VS Code, Jupyter Notebook  
**Collaboration:** Git and GitHub

---

## 1. Introduction

This guide explains how to set up the project and collaborate with other team members.

It assumes that you have already:

- Installed Git, Python and Visual Studio Code.
- Installed the Python and Jupyter extensions in VS Code.
- Cloned the GitHub repository onto your computer.

**Important:** All terminal commands in this guide should be executed from the root directory of `DSF_Group_Project`, unless otherwise specified.

The main objective is to ensure that everyone can reproduce the same analysis without manually exchanging large datasets.

## 2. Project Structure

The repository is organized as follows:

```text
DSF_Group_Project/
│
├── .venv/                         # Local Python environment
│
├── code/
│   └── 01_data_exploration.ipynb  # Data exploration notebook
│
├── data/
│   ├── download_data.py           # Download original dataset
│   ├── read_dataset.py            # Convert dataset into CSV
│   │
│   ├── raw/                       # Original TsFile datasets
│   └── processed/                 # Processed CSV datasets
│
├── output/                        # Generated results and figures
│
├── .gitignore
├── requirements.txt
├── README.md
└── USER_GUIDE.md
```

Some folders and files, such as `.venv/`, `data/raw/`, and `data/processed/`, may not exist immediately after cloning because they are generated locally and excluded from Git tracking.

### Important rules

- **`code/`:** Store notebooks and analysis scripts here.
- **`data/raw/`:** Store original downloaded datasets. Do not modify them manually.
- **`data/processed/`:** Store converted or cleaned datasets.
- **`output/`:** Store generated plots, tables, and model results.
- **`.venv/`:** Contains your local Python environment. Never upload it to GitHub.

## 3. Set Up the Python Environment

Each team member must create their own virtual environment.

A virtual environment isolates the project's Python packages from other projects on the computer.

### Step 3.1 — Open the project in VS Code

Open VS Code and select:

**File → Open Folder → DSF_Group_Project**

Open a terminal using:

**Terminal → New Terminal**

Check that the terminal is in the project root.

On macOS or Linux:

```bash
pwd
```

The path should end with `DSF_Group_Project`.

### Step 3.2 — Create the virtual environment

Run:

```bash
python3 -m venv .venv
```

This creates a `.venv` folder in the project directory.

You only need to create the environment once.

### Step 3.3 — Activate the virtual environment

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

After activation, the terminal should display `(.venv)` at the beginning of the command line.

Always activate the environment before running project scripts or installing packages.

### Step 3.4 — Install the required packages

The project dependencies are listed in `requirements.txt`.

Run:

```bash
python -m pip install -r requirements.txt
```

Wait until the installation finishes.

Verify the installation:

```bash
python -m pip check
```

If everything is compatible, the terminal should display:

```text
No broken requirements found.
```

**Important:** If the installation fails, check your Python version and the error message. Do not independently change `requirements.txt` without coordinating with the team.

## 4. Download the Dataset

The project uses **FreshRetailNet-50K**, available from Hugging Face:

https://huggingface.co/datasets/THUlab/freshretailnet_50k

The original dataset is not stored on GitHub because of its size.

Each team member must download it locally.

### Step 4.1 — Run the download script

Make sure the virtual environment is activated.

From the project root, run:

```bash
python data/download_data.py
```

The script is intended to download the original dataset files into `data/raw/`.

The expected files are:

```text
data/raw/freshretailnet_50k_train.tsfile
data/raw/freshretailnet_50k_eval.tsfile
```

The files are approximately 658 MB and 355 MB, respectively, based on the original downloads.

Make sure you have sufficient free disk space for both the original files and the processed CSV.

### Step 4.2 — Verify the download

Expand `data/raw/` in the VS Code Explorer.

Confirm that both files are present.

If either file is missing, inspect the terminal output before continuing.

Do not attempt to open the `.tsfile` files as ordinary text files. They are stored in Apache TsFile format and must be read using the appropriate Python library.

## 5. Convert the Dataset into CSV

The project uses CSV files for data exploration and modeling.

The conversion is performed by `data/read_dataset.py`.

### Step 5.1 — Run the conversion script

From the project root, run:

```bash
python data/read_dataset.py
```

Wait until the conversion finishes.

The script should create:

```text
data/processed/freshretailnet_train.csv
```

In the original project setup, the export reported:

```text
Export completed!
Total rows exported: 4,500,000
```

### Step 5.2 — Verify the processed dataset

Open the VS Code Explorer and expand:

```text
data/
    processed/
```

Confirm that `freshretailnet_train.csv` exists.

You can verify the file using Python:

```python
import pandas as pd

df = pd.read_csv(
    "data/processed/freshretailnet_train.csv",
    nrows=5
)

print(df.shape)
print(df.columns.tolist())
```

The sample should contain five rows and 65 columns if the same dataset structure has been reproduced.

**Note:** The 4.5-million-row figure is the output observed during the initial extraction. The team should separately verify that the conversion script processes all intended source data.

### Step 5.3 — Avoid repeated downloads

You do not need to download and convert the dataset every time you work on the project.

Repeat these steps only if:

- You are setting up the project for the first time.
- The local files have been deleted or corrupted.
- The team has updated the dataset version or conversion procedure.

## 6. Open and Run the Jupyter Notebook

The exploratory analysis is stored in:

```text
code/01_data_exploration.ipynb
```

### Step 6.1 — Open the notebook

In VS Code:

1. Expand the `code/` folder.
2. Open `01_data_exploration.ipynb`.
3. Click **Select Kernel** in the top-right corner.
4. Choose **Python Environments**.
5. Select the interpreter inside the project's `.venv` folder.

Make sure you do not accidentally select a global Python installation.

### Step 6.2 — Check the working directory

The notebook must locate the CSV file correctly.

A notebook may execute from the project root or the `code/` folder, depending on the VS Code configuration.

Use the following pattern to locate the project root:

```python
from pathlib import Path
import pandas as pd

project_dir = Path.cwd().resolve()

if not (project_dir / "data").is_dir():
    project_dir = project_dir.parent

csv_path = (
    project_dir
    / "data"
    / "processed"
    / "freshretailnet_train.csv"
)

df = pd.read_csv(csv_path)

print("Dataset shape:", df.shape)
```

If the file cannot be found, check the working directory and verify that the conversion step was completed.

### Step 6.3 — Run the notebook

Select **Restart** to clear the previous kernel state, then select **Run All**.

Check that:

- All cells execute successfully.
- Tables appear correctly.
- Graphs are displayed.
- No file-path or missing-package errors occur.

For the original exported training CSV, the expected dataset shape was:

```text
(4500000, 65)
```

The dataset is large. Loading the entire CSV into memory requires sufficient RAM.

If your computer cannot handle the complete dataset, coordinate with the team before creating a smaller working dataset or changing the loading procedure.

## 7. Understand the Dataset

FreshRetailNet-50K contains supermarket sales observations and additional information relevant to demand forecasting.

Important columns include:

| Column | Description |
|---|---|
| `time` | Observation timestamp |
| `store_id` | Store identifier |
| `product_id` | Product identifier |
| `sale_amount` | Recorded sales amount |
| `discount` | Discount information |
| `holiday_flag` | Holiday indicator |
| `activity_flag` | Activity indicator |
| `avg_temperature` | Average temperature |
| `avg_humidity` | Average humidity |
| `precpt` | Precipitation-related field |
| `hours_sale_00`–`23` | Hourly sales information |
| `hours_stock_status_00`–`23` | Hourly stock-status information |

The original training CSV contained observations from March 28 to June 25, 2024.

The dataset also includes categorical identifiers and stock-related information.

**Important methodological distinction:** Recorded sales are not necessarily equal to unconstrained customer demand. Products that are out of stock may have lower observed sales because customers cannot purchase them.

The team must consider stock availability when interpreting forecasting results.

Similarly, the dataset does not directly establish the quantity of food physically discarded. Any estimated food-waste reduction will require explicit assumptions or additional information.

## 8. GitHub Collaboration Workflow

The repository is shared by multiple team members.

GitHub stores the project code, notebooks, documentation, and other approved files.

Each member works on a local copy and contributes changes through Git.

### Step 8.1 — Before starting work

Open the VS Code terminal in the project root.

Check the current state:

```bash
git status
```

If you have uncommitted changes, save or commit them before switching branches or pulling updates.

To update your local `main` branch:

```bash
git switch main
git pull --ff-only origin main
```

This downloads and incorporates changes from the shared repository, provided the update can be fast-forwarded.

### Step 8.2 — Create a branch for your task

To avoid interfering with other people's work, create a separate branch for each task.

For example:

```bash
git switch -c feature/demand-forecasting
```

Other possible branch names include:

```text
feature/data-cleaning
feature/time-series-analysis
feature/model-evaluation
feature/visualizations
docs/update-user-guide
```

Each branch should represent a specific piece of work.

### Step 8.3 — Make your changes

You can now edit the relevant notebooks, scripts, or documentation.

Before committing:

1. Save all modified files.
2. Run the relevant Python scripts or notebook cells.
3. Check that the outputs are correct.
4. Check that no large dataset files are being added.
5. Confirm that your changes do not unintentionally overwrite a teammate's work.

### Step 8.4 — Commit your changes

Check the modified files:

```bash
git status
```

Add only the files relevant to your task.

For example:

```bash
git add code/01_data_exploration.ipynb
```

Create a descriptive commit:

```bash
git commit -m "Add exploratory sales analysis"
```

A commit saves a version of your work in your local Git history. It does not automatically upload it to GitHub.

### Step 8.5 — Push your branch to GitHub

Run:

```bash
git push -u origin feature/demand-forecasting
```

Replace `feature/demand-forecasting` with your actual branch name.

This uploads the branch and its commits to GitHub.

### Step 8.6 — Create a pull request

On GitHub:

1. Open the repository.
2. Navigate to **Pull requests**.
3. Click **New pull request**.
4. Select your branch as the source.
5. Select `main` as the destination.
6. Explain what you changed.
7. Request a review from another team member.

The reviewer should check that the code works and that the changes do not conflict with the project's methodology or structure.

Once approved, merge the pull request into `main`.

### Step 8.7 — Update your local repository after a merge

Return to the main branch:

```bash
git switch main
```

Download the latest changes:

```bash
git pull --ff-only origin main
```

Your local `main` branch should now contain the merged changes.

For a new task, create a new feature branch from this updated `main`.

## 9. Working on Shared Jupyter Notebooks

Jupyter Notebooks require special care during collaboration because they contain code, metadata, and sometimes saved outputs.

If two people edit the same notebook simultaneously, Git may encounter merge conflicts.

To minimize problems:

- Assign clear responsibility for each notebook.
- Prefer separate notebooks for independent tasks.
- Use descriptive filenames.
- Avoid committing unnecessary large outputs.
- Restart the kernel and run all cells before submitting a pull request.
- Review notebook changes before merging.

A possible future structure is:

```text
code/
├── 01_data_exploration.ipynb
├── 02_data_preprocessing.ipynb
├── 03_baseline_forecasting.ipynb
├── 04_model_development.ipynb
└── 05_model_evaluation.ipynb
```

These additional notebooks are proposed future work, not files that necessarily exist in the current repository.

## 10. Rules for Working with Data

The original dataset and generated CSV files are intentionally excluded from Git tracking.

This prevents the repository from becoming excessively large.

### Do not upload

- Original `.tsfile` datasets.
- Generated full-size CSV datasets.
- The `.venv` environment.
- Temporary Python files.
- Jupyter checkpoints.
- Large generated outputs unless explicitly approved by the team.

### Do upload

- Python scripts.
- Jupyter Notebooks.
- Project documentation.
- `requirements.txt`.
- `.gitignore`.
- Small, approved figures or tables that are needed for the final report.

Before pushing changes, check:

```bash
git status
```

You can also inspect tracked data files:

```bash
git ls-files data/raw data/processed
```

Ideally, no large dataset files should appear.

**Important:** `.gitignore` does not remove files that Git is already tracking. If a large dataset has been committed previously, coordinate with the team before modifying Git history.

## 11. Troubleshooting

### Problem: `ModuleNotFoundError`

Possible cause: The required package is missing or VS Code is using the wrong Python environment.

Solution:

1. Activate `.venv`.
2. Check the notebook kernel.
3. Run:

```bash
python -m pip install -r requirements.txt
```

### Problem: `FileNotFoundError`

Possible cause: The dataset has not been downloaded or converted, or the script is using an incorrect path.

Solution:

1. Confirm that the dataset exists in `data/raw/`.
2. Confirm that the CSV exists in `data/processed/`.
3. Check the current working directory.
4. Rerun the relevant download or conversion script if necessary.

### Problem: Notebook does not display results

Possible causes include an incorrect kernel, a cell that has not been executed, or an earlier cell that failed.

Solution:

1. Select the correct `.venv` kernel.
2. Restart the kernel.
3. Run the notebook from the beginning.
4. Inspect the first error message.

### Problem: Git push is rejected

Possible causes include:

- The remote branch contains changes you have not incorporated.
- You do not have permission to push.
- The repository contains a file that exceeds the hosting platform's limits.
- Authentication has failed.

Solution:

Read the complete Git error message before taking action.

Do not use `git push --force` to bypass a rejected push.

If you are working on a feature branch, update your work from the latest `main` branch and resolve any conflicts before pushing again.

### Problem: Git reports a merge conflict

This means Git cannot automatically combine some changes.

Open the affected files in VS Code, review the conflicting changes, and coordinate with the relevant teammate.

Do not blindly accept one version of a file if both contributors have made important changes.

### Problem: The CSV is too large for memory

Instead of loading the entire CSV, read a subset:

```python
import pandas as pd

df = pd.read_csv(
    "data/processed/freshretailnet_train.csv",
    nrows=100_000
)
```

Alternatively, process the file in chunks:

```python
for chunk in pd.read_csv(
    "data/processed/freshretailnet_train.csv",
    chunksize=100_000
):
    print(chunk.shape)
```

These approaches reduce memory requirements. However, the team must ensure that any sampling strategy is appropriate for the forecasting task and does not unintentionally break the time-series structure.

## 12. Recommended Daily Workflow

Each time you work on the project:

1. Open `DSF_Group_Project` in VS Code.
2. Activate your virtual environment.
3. Run `git status` to check for local changes.
4. Update your local `main` branch using `git pull --ff-only origin main`.
5. Create a new feature branch, or switch to your existing task branch.
6. Work on your assigned task.
7. Save your files and run the relevant code.
8. Check `git status` and stage only the intended files.
9. Commit with a descriptive message.
10. Push your branch to GitHub.
11. Open or update a pull request.
12. Have a teammate review the changes before merging.

**Do not download or convert the dataset every day.** Those steps are normally required only during initial setup or when the dataset-processing procedure changes.

## 13. Team Collaboration Principles

To keep the project organized and reproducible:

- **Communicate before changing shared files.** Avoid multiple people editing the same notebook simultaneously.
- **Keep `main` stable.** Merge only changes that have been tested and reviewed.
- **Document important decisions.** Explain dataset transformations, modeling assumptions, and evaluation procedures.
- **Use consistent paths and filenames.** Do not create personal absolute paths in shared code.
- **Preserve the original dataset.** Make transformations in separate scripts or notebooks.
- **Avoid data leakage.** Forecasting models must not use information that would be unavailable at prediction time.
- **Use chronological evaluation.** Do not randomly split time-series observations when assessing future forecasting performance.
- **Make results reproducible.** A teammate should be able to reproduce the analysis from the repository and the documented dataset source.

## 14. First-Time Setup Checklist

Before beginning project work, confirm that:

- [ ] The repository is cloned and open in VS Code.
- [ ] Python and the VS Code Python/Jupyter extensions are installed.
- [ ] A local `.venv` has been created.
- [ ] The virtual environment is activated.
- [ ] All packages from `requirements.txt` are installed.
- [ ] `python -m pip check` reports no broken dependencies.
- [ ] The FreshRetailNet-50K dataset has been downloaded.
- [ ] Both original TsFile files are available in `data/raw/`.
- [ ] The processed CSV has been generated in `data/processed/`.
- [ ] The CSV can be read successfully using pandas.
- [ ] The correct Python kernel is selected in VS Code.
- [ ] The exploratory notebook runs without errors.
- [ ] The team member understands the Git branching and pull-request workflow.

