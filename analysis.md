# Patient Cohort Analysis

## Analysis

I analyzed 5 million (synthetic) patients and grouped patients into four BMI categories. The CSV file was converted to Parquet for efficiency. Patients with BMI values less than 10 and greater than 60 were excluded.  I then counted the patients per BMI category and calculated their average age and glucose.

## Patterns

- Average glucose increased with BMI.
- Average BMI increased with age.
- Most patients fell into the Overweight and Obese categories.

## Efficiency of Polars

- Lazy evaluation to plan operations before executing
- Streaming to process data in chunks without storing it all in memory
- Parquet is a columnar storage format that can be used to quickly aggregate large amounts of data