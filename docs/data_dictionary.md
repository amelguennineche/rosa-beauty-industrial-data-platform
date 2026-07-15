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