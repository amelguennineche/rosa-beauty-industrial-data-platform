with factories as (

    select *
    from {{ ref('stg_factories') }}

)

select

    factory_id,
    factory_name,
    city,
    region,
    country

from factories