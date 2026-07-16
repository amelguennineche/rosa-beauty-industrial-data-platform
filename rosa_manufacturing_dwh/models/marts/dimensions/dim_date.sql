with date_range as (

    select
        min(production_date)::date as start_date,
        max(production_date)::date as end_date

    from {{ ref('stg_production_orders') }}

),

dates as (

    select
        generate_series(
            start_date,
            end_date,
            interval '1 day'
        )::date as date_day

    from date_range

)

select

    date_day as date_id,

    extract(year from date_day)::int as year,

    extract(month from date_day)::int as month,

    to_char(date_day, 'Month') as month_name,

    extract(quarter from date_day)::int as quarter,

    extract(day from date_day)::int as day

from dates