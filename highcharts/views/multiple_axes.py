from django.views.generic import View
from highcharts.views.common import HighChartsDualAxisView


class HighChartsMultiAxesView(HighChartsDualAxisView, View):
    chart_type = ''
    categories = []
    xlabels = {'rotation': -45}

    def get_data(self):
        data = super(HighChartsMultiAxesView, self).get_data()
        data['xAxis']['categories'] = self.categories
        data['xAxis']['labels'] = self.xlabels
        data['series'] = self.series
        data['yAxis'] = self.yaxis
        return data

    @property
    def series(self):
        return []

    @property
    def yaxis(self):
        return []


class HighChartsStackedView(HighChartsMultiAxesView):

    @property
    def plot_options(self):
        plot_options = super(HighChartsMultiAxesView, self).plot_options
        if plot_options is None:
            plot_options = {}
        if 'series' not in plot_options:
            plot_options['series'] = {}
        plot_options['series']['stacking'] = 'normal'
        return plot_options


class HighChartsColumnView(HighChartsMultiAxesView):
    chart_type = 'column'