{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "import-spark",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pyspark.sql import SparkSession\n",
    "from pyspark.sql.functions import col, to_date, round\n",
    "\n",
    "spark = SparkSession.builder.appName(\"EcommerceDataTransform\").getOrCreate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "load-data",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load raw data from Azure Data Lake\n",
    "df = spark.read.option(\"header\", True).csv(\n",
    "    \"abfss://sales-data@<storageaccount>.dfs.core.windows.net/raw/sales.csv\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "transform-data",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Transformations\n",
    "df_transformed = df.withColumn(\"order_date\", to_date(col(\"order_date\"), \"yyyy-MM-dd\")) \\\n",
    "                   .withColumn(\"sales_amount\", round(col(\"sales_amount\").cast(\"double\"), 2)) \\\n",
    "                   .dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "write-data",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write to curated zone\n",
    "df_transformed.write.mode(\"overwrite\").parquet(\n",
    "    \"abfss://sales-data@<storageaccount>.dfs.core.windows.net/curated/sales/\"\n",
    ")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
