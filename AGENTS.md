# Dataset Summary

## Scope
The `data.csv` extract holds 192,991 member-level records from a nutrition program spanning multiple commercial payers. Each row combines payer identity, a unique `patient_id`, and the member's first Nourish appointment date, forming the join keys for longitudinal analysis.

## Structure & Engagement Signals
Across 120 columns, the file blends categorical descriptors (primary and secondary conditions), boolean program buckets (`is_weight_bucket`, `is_diabetes_bucket`, etc.), and medication flags (`is_on_glp1`, `is_on_diabetes_medication`, `is_on_high_bp_medication`). Engagement is tracked through rolling appointment counts covering the first 30, 60, 90, 120, and 180 days, enabling retention and utilization studies.

## Clinical Metrics
For weight, BMI, blood pressure (systolic and diastolic), A1C, LDL, HDL, triglycerides, time-in-range, and resting heart rate, the dataset provides baseline value/date pairs plus change deltas at multiple follow-up windows (30 to 360 days). Weight and BMI changes appear in absolute and percentage terms; preliminary sampling shows average 180-day weight deltas around –7.5 lb among members with follow-up data, with similar downward trends for BMI and LDL.

## Data Quality Considerations
Longitudinal columns are sparse: labs and vitals often lack follow-up entries, so any descriptive statistics must filter for non-null values. Boolean fields mix string states such as `"1"`/`"0"` and `"true"`/`"false"`, requiring normalization before aggregation. Secondary condition lists are stored as bracketed strings and will need parsing to explode into individual tags. Cleaning these facets will make the dataset ready for robust segmentation, outcome tracking, and payer-level reporting.
