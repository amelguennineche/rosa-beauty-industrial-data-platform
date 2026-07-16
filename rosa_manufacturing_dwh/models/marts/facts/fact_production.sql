-- depends_on: {{ ref('dim_products') }}
-- depends_on: {{ ref('dim_factories') }}

with production as (

    select *
    from {{ ref('int_production') }}

),

date_dimension as (

    select
        date_id

    from {{ ref('dim_date') }}

)

select

    p.production_id,

    p.product_id,

    p.factory_id,

    d.date_id,

    p.planned_quantity,

    p.actual_quantity,

    p.production_variance,

    p.production_efficiency,

    p.defect_rate,

    p.production_status

from production p

left join date_dimension d
    on to_char(p.production_date, 'YYYYMMDD')::integer = d.date_id