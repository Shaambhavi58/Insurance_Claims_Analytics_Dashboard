
-- KPI views
CREATE VIEW IF NOT EXISTS vw_claims_daily AS
SELECT date(claim_date) AS day,
       COUNT(*) AS claims_count,
       SUM(claim_amount) AS claims_amount
FROM claims
GROUP BY day;

CREATE VIEW IF NOT EXISTS vw_claims_kpis AS
WITH base AS (
  SELECT
    COUNT(*) AS total_claims,
    SUM(CASE WHEN status='Approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(CASE WHEN status='Rejected' THEN 1 ELSE 0 END) AS rejected_count,
    AVG(settlement_days) AS avg_settlement_days,
    AVG(report_delay_days) AS avg_report_delay_days,
    AVG(suspected_fraud) AS fraud_rate
  FROM claims
)
SELECT * FROM base;
