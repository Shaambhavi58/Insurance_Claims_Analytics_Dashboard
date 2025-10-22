#!/usr/bin/env python3
import argparse
import pandas as pd
from sqlalchemy import create_engine

def main():
    parser = argparse.ArgumentParser(description="Compute KPI summary from SQLite DB and export CSV.")
    parser.add_argument("--db", required=True, help="Path to SQLite DB (e.g., data/claims.db)")
    parser.add_argument("--out", required=True, help="Output CSV path (e.g., data/kpi_summary.csv)")
    args = parser.parse_args()

    engine = create_engine(f"sqlite:///{args.db}")

    # Load KPIs from view
    kpis = pd.read_sql("SELECT * FROM vw_claims_kpis", con=engine)
    # More breakdowns
    by_product = pd.read_sql("""
        SELECT product,
               COUNT(*) AS claims,
               ROUND(AVG(settlement_days),2) AS avg_settlement_days,
               ROUND(AVG(report_delay_days),2) AS avg_report_delay_days,
               ROUND(AVG(suspected_fraud),4) AS fraud_rate,
               ROUND(SUM(claim_amount),2) AS total_amount
        FROM claims
        GROUP BY product
        ORDER BY total_amount DESC
    """, con=engine)

    # Save to CSV (first KPIs, then a blank row, then by_product)
    with open(args.out, "w", encoding="utf-8") as f:
        kpis.to_csv(f, index=False)
        f.write("\n")
        by_product.to_csv(f, index=False)

    print(f"Wrote KPI summary to {args.out}")

if __name__ == "__main__":
    main()
