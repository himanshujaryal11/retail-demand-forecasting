CREATE DATABASE IF NOT EXISTS retail_forecasting;
USE retail_forecasting;
CREATE TABLE stores(store_id INT PRIMARY KEY,store_type VARCHAR(10),assortment VARCHAR(10),competition_distance INT);
CREATE TABLE daily_sales(store_id INT,sales_date DATE,day_of_week TINYINT,sales DECIMAL(14,2),customers INT,open_flag TINYINT,promo TINYINT,state_holiday VARCHAR(5),school_holiday TINYINT,PRIMARY KEY(store_id,sales_date),FOREIGN KEY(store_id) REFERENCES stores(store_id));
