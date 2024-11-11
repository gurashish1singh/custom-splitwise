from __future__ import annotations

import json
import os

from dotenv import load_dotenv
from superset_api import SupersetAPIClient

load_dotenv()

SUPERSET_USER = os.getenv("SUPERSET_ADMIN_USERNAME")
SUPERSET_PASSWORD = os.getenv("SUPERSET_ADMIN_PASSWORD")
DATABASE_URL = os.getenv("DATABASE_URL")
SUPERSET_PORT = os.getenv("SUPERSET_PORT")
DATASOURCE_NAME = "public.expenses"

# Using custom ip address configured in docker
client = SupersetAPIClient(host=f"http://superset:{SUPERSET_PORT}")
client.login(username=SUPERSET_USER, password=SUPERSET_PASSWORD)


# Create the empty dashboard first
dashboard_id = client.create_dashboard(title="Expense tracking")

# Connect Superset to pgsql
database_id = client.create_database(
    database_name="Splitwise DB",
    engine="postgres",
    driver="postgresql+psycopg2",
    sqlalchemy_uri=DATABASE_URL,
)

dataset_id = client.create_dataset(database_id=1, schema="public", table="expenses")

# Create raw metadata table
raw_metadata_params = {
    "query_mode": "raw",
    "all_columns": [
        "expense_id",
        "group_id",
        "category",
        "cost",
        "currency_code",
        "description",
        "date",
        "details",
        "transaction_method",
        "created_by",
        "updated_by",
        "deleted_by",
        "created_at",
        "updated_at",
        "deleted_at",
    ],
    "temporal_columns_lookup": {
        "date": True,
        "created_at": True,
        "updated_at": True,
        "deleted_at": True,
    },
    "adhoc_filters": [
        {
            "clause": "WHERE",
            "comparator": "Last month",
            "expressionType": "SIMPLE",
            "operator": "TEMPORAL_RANGE",
            "subject": "date",
        }
    ],
    "show_cell_bars": True,
}
raw_table_chart = client.create_chart(
    dashboard_ids=[dashboard_id],
    datasource_id=dataset_id,
    datasource_name="public.expenses",
    params=json.dumps(raw_metadata_params),
    slice_name="Raw Metadata",
    viz_type="table",
)


# Create SunburstV2 Chart
sunburst_params = {
    "columns": ["category"],
    "metric": {
        "expressionType": "SIMPLE",
        "column": {
            "column_name": "cost",
            "type": "DOUBLE_PRECISION",
        },
        "aggregate": "SUM",
    },
    "adhoc_filters": [
        {
            "clause": "WHERE",
            "comparator": "Last month",
            "expressionType": "SIMPLE",
            "operator": "TEMPORAL_RANGE",
            "subject": "date",
        }
    ],
    "color_scheme": "supersetColors",
    "linear_color_scheme": "superset_seq_1",
    "label": "SUM(cost)",
}
expenses_sunburst_v2 = client.create_chart(
    dashboard_ids=[dashboard_id],
    datasource_id=dataset_id,
    datasource_name=DATASOURCE_NAME,
    params=json.dumps(sunburst_params),
    slice_name="Spending per category (past month)",
    viz_type="sunburst_v2",
)


# Create stacked category chart
stacked_category_chart_params = {
    "groupby": ["category"],
    "metrics": {
        "expressionType": "SIMPLE",
        "column": {
            "column_name": "cost",
            "type": "DOUBLE_PRECISION",
            "filterable": True,
            "groupby": True,
        },
        "aggregate": "SUM",
        "label": "SUM(cost)",
    },
    "adhoc_filters": [
        {
            "clause": "WHERE",
            "comparator": "Last month",
            "expressionType": "SIMPLE",
            "operator": "TEMPORAL_RANGE",
            "subject": "date",
        }
    ],
    "comparison_type": "values",
    "orientation": "vertical",
    "rich_tooltip": True,
    "show_empty_columns": False,
    "show_legend": True,
    "sort_series_type": "sum",
    "stack": "Stack",
    "show_legend": True,
    "legendType": "scroll",
    "legendOrientation": "top",
    "tooltipTimeFormat": "smart_date",
    "truncateXAxis": True,
    "truncateYAxis": False,
    "truncate_metric": False,
    "time_grain_sqla": "P1D",
    "x_axis": "date",
    "x_axis_sort_asc": True,
    "x_axis_sort_series": "name",
    "x_axis_sort_series_ascending": True,
    "x_axis_time_format": "smart_date",
    "x_axis_title": "Date",
    "x_axis_title_margin": 15,
    "y_axis_format": "SMART_NUMBER",
    "y_axis_title": "Cost (in dollars)",
    "y_axis_title_margin": 30,
    "y_axis_title_position": "Left",
    "color_scheme": "supersetColors",
    "linear_color_scheme": "superset_seq_1",
}
stacked_category_chart = client.create_chart(
    dashboard_ids=[dashboard_id],
    datasource_id=dataset_id,
    datasource_name=DATASOURCE_NAME,
    params=json.dumps(stacked_category_chart_params),
    slice_name="Spending per category (past month)",
    viz_type="echarts_timeseries_bar",
)


# Top spending categories
top_spending_categories_params = {
    "query_mode": "aggregate",
    "groupby": ["category"],
    "temporal_columns_lookup": {
        "date": True,
        "created_at": True,
        "updated_at": True,
        "deleted_at": True,
    },
    "include_search": True,
    "adhoc_filters": [
        {
            "clause": "WHERE",
            "comparator": "Last month",
            "expressionType": "SIMPLE",
            "operator": "TEMPORAL_RANGE",
            "subject": "date",
        }
    ],
    "metrics": [{"expressionType": "SQL", "label": "Cost in dollars", "sqlExpression": "SUM(cost)"}],
    "show_cell_bars": True,
    "order_desc": True,
    "row_limit": 10,
}
top_spending_categories = client.create_chart(
    dashboard_ids=[dashboard_id],
    datasource_id=dataset_id,
    datasource_name="public.expenses",
    params=json.dumps(top_spending_categories_params),
    slice_name="Top 10 spending categories (past month)",
    viz_type="table",
)


print("Superset Dashboard created successfully...")
