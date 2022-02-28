import matplotlib.pyplot as pyplot
import pandas as pd


def generate_figure(metric, df, xlabel, test_type):
    filename = 'fig-{}-{}.png'.format(metric, test_type)
    if(metric == 'PDR'):
        ax = df.plot(kind='bar', rot=0,  ylim=(0, 100),
                     ylabel="Packet Delivery Rate (PDR)", xlabel=xlabel)
    elif(metric == 'Energy'):
        ax = df.plot(kind='area', stacked=False,
                     ylabel="Average energy consumption (j)", xlabel=xlabel)
    elif(metric == 'Overhead'):
        ax = df.plot(kind='bar', rot=0,
                     ylabel="Control Message Overhead", xlabel=xlabel)
    elif(metric == 'Lifetime'):
        ax = df.plot(kind='bar', rot=0, ylabel="Network Lifetime (min)",
                     xlabel=xlabel, figsize=(16, 8))
    ax.figure.savefig(filename)


def data_nodes(data, test=True):
    if test:
        index = [30, 75, 100]
    else:
        index = [20, 40, 80, 100]
    return pd.DataFrame(data, index=index)


# Node tests
generate_figure('PDR', data_nodes({'WRF': [61.75, 17.68, 17.68], 'MRHOF': [39.72, 9.85, 10.91], 'ETXPC': [
                16.0, 6.59, 4.14], 'lbRPL': [31.9, 22.32, 18.64]}), 'Number of nodes', 'nodes')
generate_figure('Energy', data_nodes({'WRF': [2.42, 3.51, 3.59], 'MRHOF': [3.02, 4.55, 4.6], 'ETXPC': [
                4.38, 4.47, 4.2], 'lbRPL': [2.74, 3.42, 2.88]}), 'Number of nodes', 'nodes')
generate_figure('Overhead', data_nodes({'WRF': [1764, 2641, 2411], 'MRHOF': [2059, 2863, 2880], 'ETXPC': [
                4344, 1148, 1859], 'lbRPL': [1182, 2632, 2524]}), 'Number of nodes', 'nodes')
generate_figure('Lifetime', data_nodes({'WRF': [17, 13, 15], 'MRHOF': [
                15, 12, 10], 'ETXPC': [9, 11, 10], 'lbRPL': [15, 13, 14]}), 'Number of nodes', 'nodes')

# ppm tests
generate_figure('PDR', data_nodes({'WRF': [65.86, 61.75, 37.5, 32.65], 'MRHOF': [49.12, 39.72, 27.84, 21.29], 'ETXPC': [
                17.58, 16.0, 12.49, 13.04], 'lbRPL': [46.82, 31.9, 24.46, 21.49]}, False), 'ppm', 'ppm')
generate_figure('Energy', data_nodes({'WRF': [3.62, 2.42, 3.07, 3.28], 'MRHOF': [2.89, 3.02, 3.75, 2.81], 'ETXPC': [
                3.62, 4.38, 4.28, 4.17], 'lbRPL': [2.5, 2.74, 2.86, 2.71]}, False), 'ppm', 'ppm')
generate_figure('Overhead', data_nodes({'WRF': [1957, 1764, 1618, 1465], 'MRHOF': [2210, 2059, 1972, 1955], 'ETXPC': [
                5577, 4344, 4223, 2825], 'lbRPL': [1296, 1182, 1024, 1058]}, False), 'ppm', 'ppm')
generate_figure('Lifetime', data_nodes({'WRF': [22, 17, 14, 13], 'MRHOF': [
                20, 15, 12, 12], 'ETXPC': [9, 9, 10, 9], 'lbRPL': [18, 15, 13, 14]}, False), 'ppm', 'ppm')
