from plotly.subplots import make_subplots

from libs.useful_fcts import converter, get_OxCGRT
import data as dt


def fig_creator(name_list, courbe):
    fig = make_subplots(rows=1, cols=1)
    title = "OxCGRT - COVID 19\n Pays : {}".format(name_list[0])
    for name_index in range(1, len(name_list)):
        title += ", {}".format(name_list[name_index])
    fig.update_layout(
        title={
            'text': title,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_size=30,
        xaxis={'title': 'Date (jour/mois)'},
        yaxis={'title': 'Valeur de l\'index (sans unité)'}
    )
    for name in name_list:
        limit = dt.Ending[name]
        if limit == 0:
            if 'GR' in courbe:
                fig.add_scatter(
                    x=dt.Time_ext,
                    y=get_OxCGRT(converter("data_text/{}".format(name)))[0],
                    name="Government response index - {}".format(name))

            if 'CH' in courbe:
                fig.add_scatter(
                    x=dt.Time_ext,
                    y=get_OxCGRT(converter("data_text/{}".format(name)))[1],
                    name="Containment and health index - {}".format(name))

            if 'S' in courbe:
                fig.add_scatter(
                    x=dt.Time_ext,
                    y=get_OxCGRT(converter("data_text/{}".format(name)))[2],
                    name="Stringency index - {}".format(name))

            if 'ES' in courbe:
                fig.add_scatter(
                    x=dt.Time_ext,
                    y=get_OxCGRT(converter("data_text/{}".format(name)))[3],
                    name="Economic support index - {}".format(name))

        else:
            if 'GR' in courbe:
                fig.add_scatter(
                    x=dt.Time_ext[: -limit],
                    y=get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[0],
                    name="Government response index - {}".format(name))

            if 'CH' in courbe:
                fig.add_scatter(
                    x=dt.Time_ext[: -limit],
                    y=get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[1],
                    name="Containment and health index - {}".format(name))

            if 'S' in courbe:
                fig.add_scatter(
                    x=dt.Time_ext[: -limit],
                    y=get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[2],
                    name="Stringency index - {}".format(name))

            if 'ES' in courbe:
                fig.add_scatter(
                    x=dt.Time_ext[: -limit],
                    y=get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[3],
                    name="Economic support index - {}".format(name))
    return fig
