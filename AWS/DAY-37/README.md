
# AWS Data Pipeline - DAY-37

## Project Overview

This project demonstrates a complete AWS data pipeline workflow that ingests, transforms, queries, and monitors data using AWS services. The workflow showcases integration between S3, Athena, EventBridge Scheduler, and CloudWatch for automated data processing and analytics.

---

## Architecture & Workflow

```
┌─────────────────┐
│   Python Code   │ (Upload CSV files)
└────────┬────────┘
         │
         ▼
┌──────────────────────┐
│   AWS S3 Bucket      │ (Data Lake Storage)
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│  Amazon Athena       │ (Query CSV as SQL Tables)
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│ Scheduled Queries    │ (Automated Query Execution)
│  (EventBridge +      │   via AWS Scheduler
│   Lambda/Step Func)  │
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│   CloudWatch Metrics │ (Monitoring & Logging)
│   & Dashboards       │
└──────────────────────┘
```

---

## Components & Steps

### 1. **S3 Bucket Creation & CSV File Storage**
- **Purpose**: Centralized data lake for storing raw CSV files
- **Process**:
  - Created AWS S3 bucket to store data files
  - Used Python code to upload CSV files to S3
  - Organized data using S3 prefixes (folder structure)
  - Enabled versioning and encryption for data protection

**Example Python Code Pattern**:
```python
import boto3

s3_client = boto3.client('s3')
bucket_name = 'small-potato-data-lake'

# Upload CSV file
s3_client.upload_file(
    Filename='local_file.csv',
    Bucket=bucket_name,
    Key='data/bmw_cars.csv'
)
```

---

### 2. **Amazon Athena - Query CSV Files as Tables**
- **Purpose**: Run SQL queries directly on CSV files stored in S3 without ETL
- **Process**:
  - Created external tables in Athena that reference S3 CSV files
  - Defined schema (columns, data types) to match CSV structure
  - Used Athena to query data using standard SQL
  - Results stored in separate S3 output location

**Example Athena Query**:
```sql
CREATE EXTERNAL TABLE IF NOT EXISTS bmw_cars (
    car_id INT,
    model STRING,
    model_year INT,
    engine STRING,
    price DECIMAL(12, 2),
    created_at TIMESTAMP
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://small-potato-data-lake/data/';

-- Query the table
SELECT model, COUNT(*) as count, AVG(price) as avg_price
FROM bmw_cars
GROUP BY model;
```

---

### 3. **AWS Scheduler - Scheduled Query Execution**
- **Purpose**: Automate query execution on a defined schedule
- **Process**:
  - Created scheduled queries in Athena for recurring analysis
  - Defined cron-based schedules (e.g., daily, weekly)
  - Results automatically saved to S3 output tables
  - Integrated with EventBridge for advanced scheduling

**Configuration**:
- **Frequency**: Daily / Weekly / Custom CRON
- **Output Format**: Parquet (optimized for analytics)
- **Retention**: Query results stored with timestamps
- **Notifications**: Optional SNS/SQS integration

**Example Scheduled Query**:
```sql
-- This runs daily at 2 AM UTC
INSERT INTO bmw_cars_daily_summary
SELECT 
    DATE_TRUNC('day', created_at) as date,
    model,
    COUNT(*) as daily_count,
    AVG(price) as avg_price,
    MIN(price) as min_price,
    MAX(price) as max_price
FROM bmw_cars
WHERE created_at >= DATE_TRUNC('day', CURRENT_DATE - INTERVAL '1' DAY)
GROUP BY DATE_TRUNC('day', created_at), model;
```

---

### 4. **CloudWatch - Metrics & Monitoring**
- **Purpose**: Monitor query performance, data volume, and costs
- **Metrics Tracked**:
  - Athena query execution time
  - Data scanned (bytes)
  - Query success/failure rates
  - S3 data volume and growth
  - Lambda invocation metrics (if used for orchestration)

**CloudWatch Dashboards**:
- Real-time query performance graphs
- Data ingestion volume trends
- Cost estimation charts
- Error rate monitoring

**Example Metrics**:
```
- Athena Query Duration: Track query performance
- DataScannedInBytes: Monitor data access patterns
- EngineExecutionTime: Identify bottlenecks
- TotalExecutionTime: End-to-end latency
```

**Alarms Configuration**:
- Alert if query execution time exceeds threshold
- Notify on query failures
- Track data volume anomalies
- Cost tracking against budget

---

## Data Flow Summary

| Stage | Service | Function | Output |
|-------|---------|----------|--------|
| **1. Ingestion** | S3 + Python SDK | Upload CSV files | Raw data in S3 |
| **2. Querying** | Athena | Create tables and run SQL | Query results in S3 |
| **3. Automation** | EventBridge Scheduler | Schedule query execution | Periodic results |
| **4. Monitoring** | CloudWatch | Track metrics & logs | Dashboards & Alerts |

---

## Key Technologies Used

- **AWS S3**: Data lake and storage
- **Amazon Athena**: Serverless SQL query engine
- **AWS EventBridge Scheduler**: Serverless task scheduler
- **CloudWatch**: Metrics, logs, and monitoring
- **Python/Boto3**: AWS SDK for automation
- **IAM Roles & Policies**: Access control and permissions

---

## Benefits of This Architecture

✅ **Serverless**: No infrastructure to manage  
✅ **Scalable**: Handles growing data volumes  
✅ **Cost-Effective**: Pay only for queries executed and data scanned  
✅ **Automated**: Scheduled queries run without manual intervention  
✅ **Observable**: Comprehensive monitoring and alerting  
✅ **Data Lake**: Flexible schema and easy data exploration  

---

## Prerequisites

- AWS Account with appropriate permissions (S3, Athena, EventBridge, CloudWatch, IAM)
- Python 3.8+ with Boto3 SDK
- IAM roles configured for Athena execution
- S3 bucket with proper folder structure
- CloudWatch Log Groups for query logs

---

## Next Steps

1. Expand to multi-format data (JSON, Parquet, ORC)
2. Implement data quality checks using AWS Glue
3. Create BI dashboards using Amazon QuickSight
4. Integrate ML models using SageMaker
5. Implement data governance with AWS Lakeformation

---

## Files & Structure

```
small-potato/
├── src/
│   ├── modules/
│   │   ├── configurations/
│   │   │   └── config.py         # AWS & Database config
│   │   ├── utils/
│   │   │   └── rds.py            # RDS/Athena utilities
│   │   └── scripts/
│   │       └── upload_to_s3.py   # S3 upload script
│   └── notebooks/
│       └── data_analysis.ipynb    # Athena queries
└── docs/
    └── architecture.md            # Detailed architecture
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Athena table not found | Check S3 path and file format |
| Query timeout | Increase Athena capacity or optimize query |
| CloudWatch metrics missing | Verify IAM permissions for logging |
| Scheduled query failed | Check CloudWatch logs and Scheduler status |

---

**Last Updated**: September 1, 2026  
**Project Status**: Active Development
