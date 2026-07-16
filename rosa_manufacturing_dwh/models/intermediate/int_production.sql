with production_orders as (

    select *
    from {{ source('rosa_staging','stg_production_orders') }}
),

products as (

    select *
    from {{ source('rosa_staging','stg_products') }}

),

factories as (

    select *
    from {{ source('rosa_staging','stg_factories') }}

)

select

    p.production_id,

    p.product_id,
    prod.product_name,
    prod.category,
    prod.brand,

    p.factory_id,
    f.factory_name,
    f.city,
    f.region,
    f.country,

    p.production_date,

    p.planned_quantity,
    p.actual_quantity,

    -- Production variance
    p.actual_quantity - p.planned_quantity 
        as production_variance,


    -- Production efficiency
    round(
        p.actual_quantity::numeric 
        / nullif(p.planned_quantity,0),
        3
    ) as production_efficiency,


    p.production_status,

    p.defect_rate,


    -- Quality classification
    case

        when p.defect_rate < 0.02
            then 'Good'

        when p.defect_rate < 0.05
            then 'Acceptable'

        else 'Needs Review'

    end as quality_status


from production_orders p

left join products prod
    on p.product_id = prod.product_id

left join factories f
    on p.factory_id = f.factory_id