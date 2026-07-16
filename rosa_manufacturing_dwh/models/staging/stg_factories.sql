with source_factories as (

    select *
    from {{ source('staging', 'stg_factories') }}

)

select

    factory_id,
    factory_name,
    city,
    region,
    country,
    employees_count,
    production_capacity,
    opening_date,
    active_flag

from source_factories