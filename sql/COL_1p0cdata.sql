WITH averaged_data AS (
    SELECT 
        d."State", 
        d."family_member_count",
        ROUND(AVG(d."total_cost"), 2) AS COL
    FROM 
        public."COL1p0c" as d
    GROUP BY 
        d."State", d."family_member_count"
)
SELECT 
    "State", 
    SUM(COL) AS "Cost of Living"
FROM 
    averaged_data
GROUP BY 
    "State"
ORDER BY
    "State";