CREATE VIEW v_bisfx AS

    SELECT
        SUBSTR(date, 1, 4) || "-" ||SUBSTR(date, 6, 2) || "-" || "01" AS date,
        
        CASE    
            WHEN SUBSTR(attrib, 3, 1) = "N" THEN "Nominal"
            WHEN SUBSTR(attrib, 3, 1) = "R" THEN "Real"
        END AS eer_type,

        CASE    
            WHEN SUBSTR(attrib, 5, 1) = "B" THEN "Broad"
            WHEN SUBSTR(attrib, 5, 1) = "N" THEN "Narrow"
        END AS basket_type,
        
        SUBSTR(attrib, 7, 2) AS country,
        
        CAST(value AS REAL) AS value

    FROM bisfx_data

    WHERE country IN (SELECT code FROM country WHERE include = 1)
    AND date > "2009-12-31"

    ORDER BY eer_type, basket_type, country, date