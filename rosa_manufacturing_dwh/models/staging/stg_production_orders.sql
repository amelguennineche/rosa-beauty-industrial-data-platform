with source_production_orders as (

    select *
    from {{ source('staging', 'stg_production_orders') }}

)

select

    production_id,
    product_id,
    factory_id,
    production_date,

    planned_quantity,
    actual_quantity,

    production_status,
    defect_rate

from source_production_orders