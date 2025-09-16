-- ETL pipeline for staging e-commerce data into Azure Synapse

-- Step 1: Create staging table
CREATE TABLE stg_sales (
    order_id INT,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,
    sales_amount DECIMAL(10,2),
    region VARCHAR(50)
);

-- Step 2: Load data from external source (CSV/Blob)
-- Handled by ADF Copy Activity in practice
COPY INTO stg_sales
FROM 'https://<storage-account>.blob.core.windows.net/sales-data/sales.csv'
WITH (
    FILE_TYPE = 'CSV',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    FIRSTROW = 2
);

-- Step 3: Transform & insert into fact table
CREATE TABLE fact_sales (
    order_id INT,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,
    total_sales DECIMAL(10,2),
    region VARCHAR(50)
);

INSERT INTO fact_sales (order_id, customer_id, product_id, order_date, quantity, total_sales, region)
SELECT order_id, customer_id, product_id, order_date, quantity, sales_amount, region
FROM stg_sales;
