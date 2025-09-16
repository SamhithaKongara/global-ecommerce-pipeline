# 🌍 Global E-Commerce Sales Data Pipeline

## 📌 Project Overview
This project demonstrates an **end-to-end data engineering solution** for an e-commerce company.  
It includes **data ingestion, transformation, storage, and visualization** using Azure cloud services.

## ⚙️ Tech Stack
- **Azure Data Factory (ADF)** → Orchestrating ETL pipelines  
- **Azure Data Lake Storage Gen2** → Storing raw and curated data  
- **Azure Synapse Analytics** → Data warehouse and reporting layer  
- **Databricks (PySpark)** → Data transformations at scale  
- **Power BI** → Interactive dashboards & KPIs  

## 🚀 Workflow
1. **Data Ingestion**  
   - Raw sales data ingested from CSV/API into Azure Data Lake.  
   - ADF pipelines copy data into staging.  

2. **Data Transformation**  
   - PySpark used in Databricks for cleaning and enrichment.  
   - SQL transformations applied in Synapse for fact/dimension modeling.  

3. **Data Storage**  
   - Data stored in a **star schema** in Synapse Analytics.  

4. **Visualization**  
   - Power BI dashboards showing sales KPIs by region, trends, and customer insights.  

## 📊 Dashboard Preview
![E-commerce Dashboard](dashboards/ecommerce_dashboard.png)

## ✅ Skills Demonstrated
- Cloud-based **ETL pipeline design**  
- **Incremental loads** & performance optimization  
- **Data warehouse modeling (Star schema)**  
- Building **Power BI dashboards** with KPIs  





