with products as (

    select *
    from {{ source('rosa_staging','stg_products') }}

)

select

    product_id,
    product_name,
    category,
    brand,
    volume_ml,
    launch_date

from products