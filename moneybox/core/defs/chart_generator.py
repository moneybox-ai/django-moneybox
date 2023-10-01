from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
from pyecharts.globals import ThemeType


def render_bar_chart(x_axis_data, report_data):
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


def render_pie_chart(data, title):
    pie = (
        Pie()
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(title=title))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    )
    return pie.render_embed()


def render_charts_to_html(*args):
    chart_html = " ".join(args)
    return chart_html


def generate_charts(x_axis_data, report_data):
    bar_chart_html = render_bar_chart(x_axis_data, report_data)

    category_incomes = report_data["category_incomes"]
    category_expenses = report_data["category_expenses"]

    data1 = [(category["category__name"], category["total_expenses"]) for category in category_incomes]
    pie_chart1_html = render_pie_chart(data1, "Доходы по категориям")

    data2 = [(category["category__name"], category["total_expenses"]) for category in category_expenses]
    pie_chart2_html = render_pie_chart(data2, "Расходы по категориям")

    chart_html = render_charts_to_html(bar_chart_html, pie_chart1_html, pie_chart2_html)

    return chart_html
