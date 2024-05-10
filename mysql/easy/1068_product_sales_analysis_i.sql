# https://leetcode.com/problems/product-sales-analysis-i/description/
SELECT
    P.product_name, S.year, S.price
FROM
    Product AS P
JOIN
    Sales AS S
ON
    P.product_id = S.product_id;
