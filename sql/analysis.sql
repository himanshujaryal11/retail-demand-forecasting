USE retail_forecasting;

-- 1. Monthly sales by store
SELECT store_id, YEAR(sales_date) AS sales_year,
       MONTH(sales_date) AS sales_month, SUM(sales) AS total_sales
FROM daily_sales
GROUP BY store_id, YEAR(sales_date), MONTH(sales_date)
ORDER BY store_id, sales_year, sales_month;

-- 2. Average sales on promotion vs non-promotion days
SELECT promo, AVG(sales) AS average_sales, COUNT(*) AS observations
FROM daily_sales
WHERE open_flag = 1
GROUP BY promo;

-- 3. Top stores by total sales
SELECT store_id, SUM(sales) AS total_sales
FROM daily_sales
GROUP BY store_id
ORDER BY total_sales DESC
LIMIT 10;

-- 4. Weekday performance
SELECT day_of_week, AVG(sales) AS average_sales
FROM daily_sales
WHERE open_flag = 1
GROUP BY day_of_week
ORDER BY day_of_week;
