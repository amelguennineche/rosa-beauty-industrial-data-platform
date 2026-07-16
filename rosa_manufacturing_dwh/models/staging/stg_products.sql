with source_products as (

    select *
    from {{ source('staging', 'stg_products') }}

)

select

    product_id,
    product_name,
    category,
    brand,
    volume_ml,
    launch_date

from source_products