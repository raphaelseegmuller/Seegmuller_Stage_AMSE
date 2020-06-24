from plotly.subplots import make_subplots

from libs.useful_fcts import converter, get_OxCGRT
import data as dt


def fig_creator(name):
    limit = dt.Ending[name]
    if limit == 0:
        fig = make_subplots(rows=1, cols=1)
        fig.update_layout(
            title={
                'text': "OxCGRT - COVID 19 {}".format(name),
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            title_font_size=30)

        fig.add_scatter(
            x=dt.Time_ext,
            y=get_OxCGRT(converter("data_text/{}".format(name)))[0],
            name="Government response index - {}".format(name))

        fig.add_scatter(
            x=dt.Time_ext,
            y=get_OxCGRT(converter("data_text/{}".format(name)))[1],
            name="Containment and health index - {}".format(name))

        fig.add_scatter(
            x=dt.Time_ext,
            y=get_OxCGRT(converter("data_text/{}".format(name)))[2],
            name="Stringency index - {}".format(name))

        fig.add_scatter(
            x=dt.Time_ext,
            y=get_OxCGRT(converter("data_text/{}".format(name)))[3],
            name="Economic support index - {}".format(name))
    else:
        fig = make_subplots(rows=1, cols=1)
        fig.update_layout(
            title={
                'text': "OxCGRT - COVID 19 {}".format(name),
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            title_font_size=30)

        fig.add_scatter(
            x=dt.Time_ext[: -limit],
            y=get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[0],
            name="Government response index - {}".format(name))

        fig.add_scatter(
            x=dt.Time_ext[: -limit],
            y=get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[1],
            name="Containment and health index - {}".format(name))

        fig.add_scatter(
            x=dt.Time_ext[: -limit],
            y=get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[2], name="Stringency index - {}".format(name))

        fig.add_scatter(
            x=dt.Time_ext[: -limit],
            y=get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[3], name="Economic support index - {}".format(name))
    return fig
