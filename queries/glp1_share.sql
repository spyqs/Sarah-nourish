SELECT
    COUNT(*) AS total_members,
    SUM(CASE WHEN LOWER(TRIM(is_on_glp1)) = 'true' THEN 1 ELSE 0 END) AS glp1_members,
    100.0 * AVG(CASE WHEN LOWER(TRIM(is_on_glp1)) = 'true' THEN 1.0 ELSE 0.0 END) AS glp1_share_pct
FROM nourish_members;
