let
    Source = Csv.Document(File.Contents("//mnt//data//Insurance_Dashboard_PowerBI_Tableau//data//claims_sample.csv"),[Delimiter=",", Columns=12, Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    PromoteHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangeTypes = Table.TransformColumnTypes(PromoteHeaders,{{"claim_id", type text},{"policy_id", type text},{"customer_id", type text},{"product", type text},{"claim_amount", type number},{"claim_date", type date},{"report_delay_days", Int64.Type},{"settlement_days", Int64.Type},{"channel", type text},{"state", type text},{"suspected_fraud", Int64.Type},{"status", type text}})
in
    ChangeTypes
