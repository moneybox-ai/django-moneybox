from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
from pyecharts.globals import ThemeType

from core.defs.exeptions import ReportAPIException


def render_bar_chart(x_axis_data, report_data):
    try:
        bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(x_axis_data)
            .add_yaxis("Расходы", [report_data["total_expenses"]])
            .add_yaxis("Доходы", [report_data["total_incomes"]])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Диаграмма доходов и расходов", subtitle="За выбранный период")
            )
        )
        return bar.render_embed()
    except Exception as e:
        raise ReportAPIException(detail=f"Error occurred while rendering bar chart: {e}")


def render_pie_chart(data, title):
    try:
        pie = (
            Pie()
            .add("", data)
            .set_global_opts(title_opts=opts.TitleOpts(title=title))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
        )
        return pie.render_embed()
    except Exception as e:
        raise ReportAPIException(detail=f"Error occurred while rendering pie chart: {e}")


def render_charts_to_html(*args):
    try:
        chart_html = " ".join(args)
        return chart_html
    except Exception as e:
        raise ReportAPIException(detail=f"Error occurred while rendering charts to HTML: {e}")


def render_no_data_html():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>No Data to Build a Report</title>
    </head>
    <body>
        <p>No data to build a report</p>
    </body>
    </html>
    """


def generate_charts(x_axis_data, report_data):
    try:
        if (
            not report_data
            or all(value == 0 for value in report_data.values())
            or all(not value for value in report_data.values())
        ):
            return render_no_data_html()
        bar_chart_html = render_bar_chart(x_axis_data, report_data)
        category_incomes = report_data["category_incomes"]
        category_expenses = report_data["category_expenses"]

        incomes_data = [(category["category__name"], category["category_incomes"]) for category in category_incomes]
        pie_chart_incomes_html = render_pie_chart(incomes_data, "Доходы по категориям")

        expenses_data = [(category["category__name"], category["total_expenses"]) for category in category_expenses]
        pie_chart_expenses_html = render_pie_chart(expenses_data, "Расходы по категориям")

        chart_html = render_charts_to_html(bar_chart_html, pie_chart_incomes_html, pie_chart_expenses_html)
        return chart_html
    except Exception as e:
        raise ReportAPIException(detail=f"Error occurred while generating charts: {e}")
