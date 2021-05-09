CREATE VIEW v_bisrate AS

    SELECT
        SUBSTR(date, 1, 4) || "-" ||SUBSTR(date, 6, 2) || "-" || "01" AS date,
        SUBSTR(attrib, 3, 2) AS country,
        CAST(value AS REAL) AS value

    FROM bisrate_data

    WHERE country IN (SELECT code FROM country WHERE include = 1)
    AND date > "2009-12-31"

    ORDER BY country, date