# Insurance Claims Analytics Dashboard

A production-ready, GitHub-friendly starter for an **Insurance Claims Analytics** project. It includes:
- Synthetic dataset (`data/claims_sample.csv`)
- Reproducible ETL + KPI scripts in `src/`
- SQL DDL + analytics views in `sql/`
- Jupyter-friendly notebook starter in `notebooks/`
- Docs and sample charts in `docs/`

## 📊 KPIs Included
- Total claims, total claim amount
- Approval rate, rejection rate
- Average settlement time (days)
- Average report delay (days)
- Fraud suspicion rate (overall & by product/channel)
- Product/channel/state breakdowns

## 🚀 Quickstart

### 1) Set up environment
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Run ETL to local SQLite
```bash
python src/etl.py --csv data/claims_sample.csv --db data/claims.db
```

### 3) Build KPIs
```bash
python src/kpi_report.py --db data/claims.db --out data/kpi_summary.csv
```

### 4) Explore in Notebook
Open `notebooks/eda_and_kpis.ipynb` to see examples of EDA and visualization.

## 🗂️ Folder Structure
```
Insurance_Claims_Analytics_Dashboard/
├── data/
│   ├── claims_sample.csv
│   └── (generated) claims.db
├── docs/
│   └── sample_screenshots/
├── notebooks/
├── sql/
│   ├── schema.sql
│   └── views.sql
├── src/
│   ├── etl.py
│   └── kpi_report.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 🧰 Tech Stack
- Python (pandas, numpy, sqlalchemy, matplotlib)
- SQLite (for easy local analytics)
- Jupyter Notebook

## 📌 Notes
- Dataset is synthetic and safe to share publicly.
- Add your BI layer (Power BI/Tableau) on top of `data/claims.db` or the CSV.
