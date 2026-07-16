with products as (

    select *
    from {{ ref('stg_products') }}

)

select

    product_id,
    product_name,
    category,
    brand,
    volume_ml,
    launch_date

from products