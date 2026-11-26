USE retail_forecasting;
SELECT store_id,YEAR(sales_date) sales_year,MONTH(sales_date) sales_month,SUM(sales) total_sales FROM daily_sales GROUP BY store_id,YEAR(sales_date),MONTH(sales_date);
SELECT promo,AVG(sales) avg_sales,COUNT(*) observations FROM daily_sales WHERE open_flag=1 GROUP BY promo;
SELECT store_id,SUM(sales) total_sales FROM daily_sales GROUP BY store_id ORDER BY total_sales DESC LIMIT 10;
