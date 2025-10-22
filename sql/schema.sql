
-- Schema for claims data (SQLite/Postgres compatible-ish)
CREATE TABLE IF NOT EXISTS claims (
  claim_id TEXT PRIMARY KEY,
  policy_id TEXT NOT NULL,
  customer_id TEXT NOT NULL,
  product TEXT NOT NULL,
  claim_amount REAL NOT NULL,
  claim_date DATE NOT NULL,
  report_delay_days INTEGER NOT NULL,
  settlement_days INTEGER NOT NULL,
  channel TEXT NOT NULL,
  state TEXT NOT NULL,
  suspected_fraud INTEGER NOT NULL,
  status TEXT NOT NULL
);
