CREATE DATABASE IF NOT EXISTS retail_forecasting;
USE retail_forecasting;

CREATE TABLE IF NOT EXISTS stores (
    store_id INT PRIMARY KEY,
    store_type VARCHAR(10),
    assortment VARCHAR(10),
    competition_distance INT NULL,
    competition_open_since_month INT NULL,
    competition_open_since_year INT NULL,
    promo2 TINYINT,
    promo2_since_week INT NULL,
    promo2_since_year INT NULL,
    promo_interval VARCHAR(100) NULL
);

CREATE TABLE IF NOT EXISTS daily_sales (
    store_id INT NOT NULL,
    sales_date DATE NOT NULL,
    day_of_week TINYINT,
    sales DECIMAL(14,2) NOT NULL,
    customers INT,
    open_flag TINYINT,
    promo TINYINT,
    state_holiday VARCHAR(5),
    school_holiday TINYINT,
    PRIMARY KEY (store_id, sales_date),
    CONSTRAINT fk_daily_store FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE INDEX idx_daily_date ON daily_sales(sales_date);
CREATE INDEX idx_daily_promo ON daily_sales(promo);
