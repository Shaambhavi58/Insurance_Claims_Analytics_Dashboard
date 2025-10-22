#!/usr/bin/env python3
import argparse
import pandas as pd
from sqlalchemy import create_engine, text

def main():
    parser = argparse.ArgumentParser(description="Load claims CSV into SQLite and build schema/views.")
    parser.add_argument("--csv", required=True, help="Path to claims_sample.csv")
    parser.add_argument("--db", required=True, help="Path to SQLite DB to create (e.g., data/claims.db)")
    parser.add_argument("--ifexists", default="replace", choices=["fail","replace","append"], help="Behavior when table exists")
    args = parser.parse_args()

    engine = create_engine(f"sqlite:///{args.db}")
    df = pd.read_csv(args.csv)
    df.to_sql("claims", con=engine, if_exists=args.ifexists, index=False)

    # Apply KPI views
    with engine.begin() as conn:
        with open("sql/views.sql", "r") as f:
            conn.execute(text(f.read()))

    print(f"Loaded {len(df)} rows into {args.db} and created KPI views.")

if __name__ == "__main__":
    main()
