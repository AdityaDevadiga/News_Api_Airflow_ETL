

# News API ETL with Airflow

This project demonstrates how to use Apache Airflow to perform Extract, Transform, and Load (ETL) operations with the News API. The extracted news headlines are stored in a CSV file and then uploaded to an Amazon S3 bucket.

## Prerequisites

Before running the code, ensure you have the following prerequisites installed:

- Python
- Apache Airflow
- Necessary Python packages (requests, pandas, s3fs, etc.)

## Note on SSH Key Permissions

If you encounter the "UNPROTECTED PRIVATE KEY FILE" error while trying to connect to your EC2 instance, it is likely due to incorrect permissions on your private key file.

You can fix this issue by adjusting the permissions using the following commands:

```bash
icacls your_downloaded_key_filename.pem /inheritance:r
icacls your_downloaded_key_filename.pem /grant:r "%USERNAME%:R"

