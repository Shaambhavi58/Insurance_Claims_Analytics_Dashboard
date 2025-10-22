# Power BI Template Setup

1) Open Power BI Desktop → **Get Data → Blank Query** → **Advanced Editor** → paste contents of `query.m`, then rename the query to **claims**.
2) Close & Apply. In Model view, set **claim_date** to Data type: Date.
3) Create measures from `measures.md` (Model view → New measure) to power your cards/visuals.
4) Build report visuals:
   - Card: Total Claims, Total Claim Amount, Approval Rate, Fraud Rate
   - Clustered bar: product vs Total Claim Amount
   - Column: channel vs Avg Settlement Days
   - Pie/Donut: status share
   - Line: claim_date (month) vs Total Claim Amount
5) Save as **Insurance_Claims_Dashboard.pbit** to reuse as a template.
