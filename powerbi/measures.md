// Create these measures in Power BI (Model view > New measure):

Total Claims = COUNTROWS('claims')
Total Claim Amount = SUM('claims'[claim_amount])
Approval Rate = 
DIVIDE(
    CALCULATE(COUNTROWS('claims'), 'claims'[status] = "Approved"),
    [Total Claims]
)

Rejection Rate =
DIVIDE(
    CALCULATE(COUNTROWS('claims'), 'claims'[status] = "Rejected"),
    [Total Claims]
)

Avg Settlement Days = AVERAGE('claims'[settlement_days])
Avg Report Delay = AVERAGE('claims'[report_delay_days])
Fraud Rate = AVERAGE('claims'[suspected_fraud])
