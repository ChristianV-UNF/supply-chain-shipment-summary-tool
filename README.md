# Supply Chain Shipment Summary Tool

## Project Overview

This project is a small Python-based supply chain analysis tool developed as part of an Agile sprint. The tool reads, cleans, summarizes, and optionally visualizes shipment delivery data from the provided `supply_delivery_history.csv` dataset.

The goal of the project is to create a modular and reusable Python codebase that can generate meaningful shipment summaries and operational insights. The tool is designed so its functions could later be reused in a dashboard, report, or analytics application.

---

## Sprint Goal

Build a modular Python tool that loads, cleans, summarizes, and visualizes supply chain shipment data using reusable functions and Agile collaboration practices.

---

## Project Structure

```text
supply-chain-tool/
│
├── data/
│   └── supply_delivery_history.csv
│
├── src/
│   ├── load_data.py
│   ├── cleaning.py
│   ├── summaries.py
│   ├── visualizations.py
│   └── main.py
│
├── outputs/
│
├── README.md
├── requirements.txt
└── .gitignore 
```

---

## Features

- Load shipment data from a CSV file.
- Clean missing and inconsistent values.
- Convert date and numeric columns into usable formats.
- Generate shipment summary metrics.
- Summarize data by country, vendor, product group, and shipment mode.
- Create reusable visualization functions for future reporting.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd supply-chain-tool
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Make sure the dataset is located in the `data/` folder:

```text
data/supply_delivery_history.csv
```

Run the main script:

```bash
python src/main.py
```

---

## Agile Collaboration

This project follows a one-week Agile sprint. The team uses:

- GitHub for version control.
- Feature branches for each user story.
- Pull requests for peer review.
- Taiga for sprint backlog and task tracking.
- Story IDs in commits and PRs for traceability.

---

## Main User Stories

- US-01: Set up project repository structure.
- US-02: Load shipment dataset.
- US-03: Clean shipment data.
- US-04: Generate shipment summary metrics.
- US-05: Generate country and vendor summaries.
- US-06: Generate product and shipment mode insights.
- US-07: Create visualization functions.
- US-08: Document and finalize the tool.