from pathlib import Path
from faker import Faker
import pandas as pd
import random

fake = Faker()

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


# ==========================
# Business constants
# ==========================

BRANDS = [
    "Rosa Premium",
    "Rosa Essentials",
    "Rosa Organics",
    "Rosa Luxe"
]

CATEGORIES = {
    "Skincare": [
        "Hydrating Cream",
        "Anti-Aging Serum",
        "Face Cleanser",
        "Night Cream",
        "Eye Cream"
    ],

    "Haircare": [
        "Shampoo",
        "Conditioner",
        "Hair Mask",
        "Hair Oil"
    ],

    "Makeup": [
        "Foundation",
        "Lipstick",
        "Mascara",
        "Blush"
    ],

    "Fragrance": [
        "Eau de Parfum",
        "Eau de Toilette",
        "Body Mist"
    ]
}
VOLUMES = [
    30,
    50,
    75,
    100,
    150,
    200
]
FACTORY_LOCATIONS = [
    {
        "city": "Arras",
        "region": "Hauts-de-France",
        "country": "France"
    },
    {
        "city": "Reims",
        "region": "Grand Est",
        "country": "France"
    },
    {
        "city": "Lille",
        "region": "Hauts-de-France",
        "country": "France"
    },
    {
        "city": "Lyon",
        "region": "Auvergne-Rhône-Alpes",
        "country": "France"
    },
    {
        "city": "Bordeaux",
        "region": "Nouvelle-Aquitaine",
        "country": "France"
    }
]

def generate_products(n_products=100):
    """
    Generate synthetic product master data
    for Rosa Beauty Industries.
    """

    products = []

    product_counter = 1

    product_names = {
        "Skincare": [
            "Hydrating Cream",
            "Anti-Aging Serum",
            "Face Cleanser",
            "Night Cream",
            "Eye Cream"
        ],
        "Haircare": [
            "Repair Shampoo",
            "Conditioner",
            "Hair Mask",
            "Hair Oil"
        ],
        "Makeup": [
            "Foundation",
            "Lipstick",
            "Mascara",
            "Blush"
        ],
        "Fragrance": [
            "Eau de Parfum",
            "Eau de Toilette",
            "Body Mist"
        ]
    }

    for _ in range(n_products):

        category = random.choice(list(product_names.keys()))

        product_type = random.choice(
            product_names[category]
        )

        product = {
            "product_id": f"PROD{product_counter:04d}",
            "product_name": f"Rosa {product_type}",
            "category": category,
            "brand": random.choice(BRANDS),
            "volume_ml": random.choice(VOLUMES),
            "launch_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            ),
            "active_flag": random.choice([True, True, True, False])
        }

        products.append(product)

        product_counter += 1


    df = pd.DataFrame(products)

    # ============================
    # Data Quality Checks
    # ============================

    assert len(df) == n_products, "Unexpected number of products"

    assert df["product_id"].is_unique, "Product IDs are not unique"
    
    print("\nDataset preview:")
    print(df.head())

    print("\nDataset information:")
    print(df.info())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nNumber of products:")
    print(len(df))

    output_file = RAW_DATA_DIR / "products.csv"

    df.to_csv(
        output_file,
        index=False
    )

    print(f"Generated {n_products} products")
    print(f"Saved to {output_file}")

def generate_factories():

    factories = []

    for index, location in enumerate(FACTORY_LOCATIONS, start=1):

        factory = {
            "factory_id": f"FAC{index:04d}",
            "factory_name": f"Rosa {location['city']} Manufacturing Site",
            "city": location["city"],
            "region": location["region"],
            "country": location["country"],
            "employees_count": random.randint(150, 500),
            "production_capacity": random.randint(500000, 2000000),
            "opening_date": fake.date_between(
                start_date="-20y",
                end_date="-1y"
            ),
            "active_flag": True
        }

        factories.append(factory)


    df = pd.DataFrame(factories)


    # ==========================
    # Data Quality Checks
    # ==========================

    assert df["factory_id"].is_unique, "Factory IDs are not unique"

    assert len(df) == len(FACTORY_LOCATIONS), "Unexpected number of factories"

    assert df["city"].notnull().all(), "Missing city values"

    assert df["region"].notnull().all(), "Missing region values"

    assert df["country"].notnull().all()

    print("\nDataset preview:")
    print(df.head())

    print("\nDataset information:")
    print(df.info())

    print("\nMissing values:")
    print(df.isnull().sum())

    output_file = RAW_DATA_DIR / "factories.csv"

    df.to_csv(
        output_file,
        index=False
    )


    print(f"Generated {len(df)} factories")
    print(f"Saved to {output_file}")


if __name__ == "__main__":

    #generate_products()
    generate_factories()