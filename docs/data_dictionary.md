# Data Dictionary

## products.csv

| Column | Type | Description |
|---------|------|-------------|
| product_id | STRING | Unique product identifier |
| product_name | STRING | Product name |
| category | STRING | Product category |
| brand | STRING | Brand |
| volume_ml | INTEGER | Product volume in milliliters |
| launch_date | DATE | Product launch date |
| active_flag | BOOLEAN | Indicates if the product is active |


## factories.csv

| Column | Type | Description |
|--------|------|-------------|
| factory_id | STRING | Unique factory identifier |
| factory_name | STRING | Factory name |
| city | STRING | Factory city |
| region | STRING | Administrative region |
| country | STRING | Country |
| employees_count | INTEGER | Number of employees |
| production_capacity | INTEGER | Annual production capacity |
| opening_date | DATE | Factory opening date |
| active_flag | BOOLEAN | Indicates if factory is active |

## production_orders.csv

| Column | Type | Description |
|--------|------|-------------|
| production_id | STRING | Unique production order identifier |
| product_id | STRING | Product reference |
| factory_id | STRING | Factory reference |
| production_date | DATE | Production date |
| planned_quantity | INTEGER | Planned production quantity |
| actual_quantity | INTEGER | Actual production quantity |
| production_status | STRING | Production order status |
| defect_rate | FLOAT | Percentage of defective products |