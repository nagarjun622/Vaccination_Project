-- Starter queries for vaccination_analysis.sqlite
SELECT year,antigen,AVG(coverage) mean_coverage,COUNT(*) records FROM coverage_admin GROUP BY year,antigen ORDER BY year,antigen;
SELECT code,name,year,antigen,coverage FROM coverage_admin WHERE coverage<95 ORDER BY year DESC,coverage;
SELECT who_region,year,AVG(introduced_pct) introduction_share_pct FROM introduction_by_region GROUP BY who_region,year;
SELECT disease,year,SUM(cases) reported_cases FROM cases GROUP BY disease,year ORDER BY disease,year;
