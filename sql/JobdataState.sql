SELECT
    j."State",
    j."Job Type",
    ROUND(AVG(j."Annual Median Income")) AS avg_income
FROM
    public."JobsFiltered" AS j
GROUP BY
    j."State",
    j."Job Type"
ORDER BY
    j."State";

