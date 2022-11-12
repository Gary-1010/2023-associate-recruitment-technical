CREATE TABLE new_table
AS SELECT
    owner_id, owner_name, COUNT(DISTINCT category_title) as category_count


SELECT *
FROM new_table
ORDER BY category_count