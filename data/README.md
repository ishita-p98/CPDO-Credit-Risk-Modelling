# Market-data inputs (not redistributed)

This project intentionally does not include the CDX.NA.IG spread CSV, daily interest-rate CSV, or the `Market Risk.xlsx` workbook. Their provider terms and redistribution rights have not been established.

To reproduce the research, obtain inputs from a source whose terms permit your intended use and place them locally in this directory.

## CIR + jump notebook

The notebook expects two semicolon-delimited files:

- `cdx_spread.csv`: date and spread (basis points), with decimal commas normalized during import.
- `sofr_daily.csv`: date and rate (percent).

Update the file paths in the first data-loading cells if your authorized source uses different filenames or schemas.

## Regime-switching notebook

The experimental notebook expects `market_risk.xlsx`, sheet `Data`, with these columns:

- `treasury_date`, `5_year_treasurey`
- `date_cdx`, `cdx_5y`
- `dbaa_date`, `dbaa`

The notebook combines different spread proxies and periods; this is experimental, requires careful provenance review, and is not validated as a continuous comparable credit-spread history.

Do not commit provider exports, licensed data, credentials, or personally identifiable information.
