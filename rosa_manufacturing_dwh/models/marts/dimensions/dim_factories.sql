with factories as (

    select *
    from {{ source('rosa_staging','stg_factories') }}

)

select

    factory_id,
    factory_name,
    city,
    region,
    country

from factories