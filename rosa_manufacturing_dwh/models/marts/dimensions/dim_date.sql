with production_orders as (

    select
        production_date

    from {{ source('rosa_staging','stg_production_orders') }}

),

dates as (

    select distinct
        production_date

    from production_orders

)

select

    to_char(production_date,'YYYYMMDD')::integer as date_id,

    production_date,

    extract(year from production_date)::integer as year,

    extract(month from production_date)::integer as month,

    extract(day from production_date)::integer as day

from dates