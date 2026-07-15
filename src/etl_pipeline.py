import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"

STAGING_DIR = BASE_DIR / "data" / "staging"



# ==========================
# Extrat Functions
# ==========================

def extract_products():

    file_path = RAW_DATA_DIR / "products.csv"

    df = pd.read_csv(file_path)

    return df

def extract_factories():

    file_path = RAW_DATA_DIR / "factories.csv"

    df = pd.read_csv(file_path)

    return df

def extract_production_orders():

    file_path = RAW_DATA_DIR / "production_orders.csv"

    df = pd.read_csv(file_path)

    return df

# ==========================
# Transform Functions
# ==========================

def transform_products(df):

    df["product_name"] = (
        df["product_name"]
        .str.strip()
    )


    df["category"] = (
        df["category"]
        .str.title()
    )


    df["brand"] = (
        df["brand"]
        .str.title()
    )


    df["launch_date"] = pd.to_datetime(
        df["launch_date"]
    )

# Data quality checks

    assert df["product_id"].is_unique

    assert df["product_name"].notnull().all()

    assert df["category"].notnull().all()

    assert df["brand"].notnull().all()

    assert df["launch_date"].notnull().all()

    return df

def transform_factories(df):

    # Nettoyage des textes

    df["factory_name"] = (
        df["factory_name"]
        .str.strip()
    )


    df["city"] = (
        df["city"]
        .str.title()
    )


    df["region"] = (
        df["region"]
        .str.strip()
    )


    df["country"] = (
        df["country"]
        .str.title()
    )


    # Conversion date

    df["opening_date"] = pd.to_datetime(
        df["opening_date"]
    )


    # Data quality checks

    assert df["factory_id"].is_unique

    assert df["factory_name"].notnull().all()

    assert df["city"].notnull().all()

    assert df["region"].notnull().all()

    assert df["opening_date"].notnull().all()

    assert (
        df["production_capacity"] > 0
    ).all()

    assert (
        df["employees_count"] > 0
    ).all()

    return df

def transform_production_orders(df):

    df["production_date"] = pd.to_datetime(
        df["production_date"]
    )

    df["production_status"] = (
        df["production_status"]
        .str.strip()
        .str.title()
    )

    assert df["production_id"].is_unique

    assert df["product_id"].notnull().all()

    assert df["factory_id"].notnull().all()

    assert df["production_date"].notnull().all()

    assert df["planned_quantity"].notnull().all()

    assert df["actual_quantity"].notnull().all()

    assert (
        df["planned_quantity"] > 0
    ).all()

    assert (
        df["actual_quantity"] > 0
    ).all()

    assert (
        df["defect_rate"].between(0, 1)
    ).all()


    # Allowed production statuses

    allowed_status = [
        "Completed",
        "In Progress",
        "Delayed"
    ]


    assert (
        df["production_status"]
        .isin(allowed_status)
        .all()
    )


    return df

# ==========================
# Load Functions
# ==========================

def load_products(df):

    STAGING_DIR.mkdir(
        exist_ok=True
    )


    output_file = (
        STAGING_DIR /
        "stg_products.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        "Products staging loaded"
    )

def load_factories(df):

    STAGING_DIR.mkdir(
        exist_ok=True
    )


    output_file = (
        STAGING_DIR /
        "stg_factories.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        "Factories staging loaded"
    )

def load_production_orders(df):

    STAGING_DIR.mkdir(
        exist_ok=True
    )


    output_file = (
        STAGING_DIR /
        "stg_production_orders.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        "Production orders staging loaded"
    )

if __name__ == "__main__":

    # Products

    """products = extract_products()

    products = transform_products(products)

    load_products(products)"""

    # Factories

    """factories = extract_factories()

    factories = transform_factories(factories)

    load_factories(factories)"""

    # Production orders

    production_orders = extract_production_orders()

    production_orders = transform_production_orders(
        production_orders
    )

    load_production_orders(
        production_orders
    )
