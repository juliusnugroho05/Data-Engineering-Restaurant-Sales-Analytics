# Restaurant Sales Data Engineering Pipeline

An end-to-end data engineering project focused on building a complete data pipeline for restaurant sales data, from data cleaning and transformation to workflow orchestration, data warehousing, and business visualization.

## Project Overview

This project uses the **Restaurant Sales – Dirty Data for Cleaning Training** dataset from Kaggle. The raw dataset contains more than **17,500 transactions** from 2022–2023 with various data quality issues, including missing values, duplicate records, and inconsistent data formats.

The project implements a complete data engineering lifecycle to transform raw transactional data into structured and reliable business insights.

## Objectives

- Build an end-to-end data engineering pipeline
- Clean and transform raw restaurant sales data
- Implement a data warehouse using a **Star Schema**
- Automate and orchestrate the data pipeline
- Validate data quality throughout the pipeline
- Create an interactive dashboard for business analysis

## Data Engineering Pipeline

```text
Raw CSV Dataset
      ↓
Pentaho Data Integration
      ↓
Data Cleaning & Transformation
      ↓
MySQL
      ↓
Star Schema Data Warehouse
      ↓
Apache Airflow
      ↓
Pipeline Orchestration
      ↓
Power BI
      ↓
Business Insights
```

All process were documented on the [Final Report](Final Report Data Engineering.pdf).
