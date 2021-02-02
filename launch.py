def main():
    from windows import main_window
    main_window.run()


if __name__ == "__main__":
    # from classes import topology_generator as tp
    # import matplotlib.pyplot as plt
    # #posible metrics --> [PDR, Overhead, Energy, Lifetime]
    # tp.generateGraph('PDR', ['MRHOF'],[30], folder='30-nodes-quien-knows')
    # tp.generateGraph('Overhead', ['MRHOF'],[30], folder='30-nodes-quien-knows')
    # tp.generateGraph('Energy', ['MRHOF'],[30], folder='30-nodes-quien-knows')
    # tp.generateGraph('Lifetime', ['MRHOF'],[30], folder='30-nodes-quien-knows')
    # plt.show()

    # from classes import topology_generator as tp
    # import matplotlib.pyplot as plt
    # #posible metrics --> [PDR, Overhead, Energy, Lifetime]
    # tp.generateGraph('PDR', ['MRHOF10','MRHOF20','MRHOF30'],[25], folder='sim-ppm')
    # tp.generateGraph('Overhead', ['MRHOF10','MRHOF20','MRHOF30'],[25], folder='sim-ppm')
    # tp.generateGraph('Energy', ['MRHOF10','MRHOF20','MRHOF30'],[25], folder='sim-ppm')
    # tp.generateGraph('Lifetime', ['MRHOF10','MRHOF20','MRHOF30'],[25], folder='sim-ppm')
    # plt.show()

    # from classes import topology_generator as tp
    # import matplotlib.pyplot as plt
    # #posible metrics --> [PDR, Overhead, Energy, Lifetime]
    # tp.generateGraph('PDR', ['OF010','OF020','OF030'],[25], folder='sim-ppm')
    # tp.generateGraph('Overhead', ['OF010','OF020','OF030'],[25], folder='sim-ppm')
    # tp.generateGraph('Energy', ['OF010','OF020','OF030'],[25], folder='sim-ppm')
    # tp.generateGraph('Lifetime', ['OF010','OF020','OF030'],[25], folder='sim-ppm')
    # plt.show()

    # from classes import topology_generator as tp
    # import matplotlib.pyplot as plt
    # # posible metrics --> [PDR, Overhead, Energy, Lifetime]
    # tp.generateGraphTraffic('PDR', ['MRHOF', 'OF0', 'WRF'], [
    #                         10, 20, 30], 25, folder='sim-ppm')
    # tp.generateGraphTraffic('Overhead', ['MRHOF', 'OF0', 'WRF'], [
    #     10, 20, 30], 25, folder='sim-ppm')
    # tp.generateGraphTraffic('Energy', ['MRHOF', 'OF0', 'WRF'], [
    #     10, 20, 30], 25,  folder='sim-ppm')
    # tp.generateGraphTraffic('Lifetime', ['MRHOF', 'OF0', 'WRF'], [
    #     10, 20, 30], 25,  folder='sim-ppm')
    # plt.show()

    # from classes import topology_generator as tp
    # import matplotlib.pyplot as plt
    # # posible metrics --> [PDR, Overhead, Energy, Lifetime]
    # lifetime = tp.generateGraphTraffic('Lifetime', ['MRHOF','OF0','WRF'], [
    #     20,40,60,80,100], 31,  folder='sim-ppm-v2')
    # print(lifetime)
    # tp.generateGraphTraffic('PDR', ['MRHOF','OF0','WRF'], [
    #                          20,40,60,80,100], 31, folder='sim-ppm-v2', lifetime=lifetime)
    # tp.generateGraphTraffic('Overhead', ['MRHOF','OF0','WRF'], [
    #     20,40,60,80,100], 31, folder='sim-ppm-v2', lifetime=lifetime)
    # tp.generateGraphTraffic('Energy', ['MRHOF','OF0','WRF'], [
    #      20,40,60,80,100], 31,  folder='sim-ppm-v2', lifetime=lifetime)
    # plt.show()

    # from classes import topology_generator as tp
    # import matplotlib.pyplot as plt
    # # posible metrics --> [PDR, Overhead, Energy, Lifetime]
    # lifetime = tp.generateGraphTraffic('Lifetime', [
    #                                    'MRHOF_RX70', 'WRF_RX70', 'MRHOF_RX80', 'WRF_RX80', 'MRHOF_RX90', 'WRF_RX90'], [40], 31,  folder='rx-change-ppm')
    # print(lifetime)
    # tp.generateGraphTraffic('PDR', ['MRHOF_RX70', 'WRF_RX70', 'MRHOF_RX80', 'WRF_RX80', 'MRHOF_RX90', 'WRF_RX90'], [
    #                         40], 31, folder='rx-change-ppm', lifetime=lifetime)
    # tp.generateGraphTraffic('Overhead',  ['MRHOF_RX70', 'WRF_RX70', 'MRHOF_RX80', 'WRF_RX80', 'MRHOF_RX90', 'WRF_RX90'], [
    #                         40], 31, folder='rx-change-ppm', lifetime=lifetime)
    # tp.generateGraphTraffic('Energy',  ['MRHOF_RX70', 'WRF_RX70', 'MRHOF_RX80', 'WRF_RX80', 'MRHOF_RX90', 'WRF_RX90'], [
    #                         40], 31,  folder='rx-change-ppm', lifetime=lifetime)
    # plt.show()

    # from classes import topology_generator as tp
    # import matplotlib.pyplot as plt
    # # posible metrics --> [PDR, Overhead, Energy, Lifetime]
    # lifetime = tp.generateGraphTraffic('Lifetime', ['MRHOF', 'WRF'], [40], 31,  folder='31-2-ppm')
    # print(lifetime)
    # tp.generateGraphTraffic('PDR', ['MRHOF', 'WRF'], [
    #                         40], 31, folder='31-2-ppm')
    # tp.generateGraphTraffic('Overhead', ['MRHOF', 'WRF'], [
    #                         40], 31, folder='31-2-ppm', lifetime=lifetime)
    # tp.generateGraphTraffic('Energy',  ['MRHOF', 'WRF'], [
    #                         40], 31,  folder='31-2-ppm', lifetime=lifetime)
    # plt.show()

    
    # from classes import topology_generator as tp
    # import matplotlib.pyplot as plt
    # # posible metrics --> [PDR, Overhead, Energy, Lifetime]
    # lifetime = tp.generateGraphTraffic('Lifetime', ['WRF','MRHOF'], [40], 31,  folder='31-2-ppm')
    # print(lifetime)
    # tp.generateGraphTraffic('PDR', ['WRF','MRHOF'], [
    #                         20], 31, folder='31-ppm-new')
    # tp.generateGraphTraffic('Overhead', ['WRF','MRHOF'], [
    #                         20], 31, folder='31-ppm-new', lifetime=lifetime)
    # tp.generateGraphTraffic('Energy',  ['WRF','MRHOF'], [
    #                         20], 31,  folder='31-ppm-new', lifetime=lifetime)
    # plt.show()

    # from classes import topology_generator as tp
    # import matplotlib.pyplot as plt
    # # posible metrics --> [PDR, Overhead, Energy, Lifetime]
    # lifetime = tp.generateGraphTraffic('Lifetime', ['WRF','MRHOF'], [20,40,80,100], 31,  folder='ppm-last')
    # print(lifetime)
    # tp.generateGraphTraffic('PDR', ['WRF','MRHOF'],[20,40,80,100], 31, folder='ppm-last',  lifetime=lifetime)
    # tp.generateGraphTraffic('Overhead', ['WRF','MRHOF'],[20,40,80,100], 31, folder='ppm-last', lifetime=lifetime)
    # tp.generateGraphTraffic('Energy',  ['WRF','MRHOF'], [20,40,80,100], 31,  folder='ppm-last', lifetime=lifetime)
    # plt.show()

    from classes import topology_generator as tp
    import matplotlib.pyplot as plt
    # posible metrics --> [PDR, Overhead, Energy, Lifetime]
    lifetime = tp.generateGraph('Lifetime', ['WRF','MRHOF'], [31,51,76,101], folder='nodes-tests')
    print('Lowest lifetime of the networks --> {}'.format(','.join([str(time) for time in lifetime])))
    print('\n')
    tp.generateGraph('PDR', ['WRF','MRHOF'],[31,51,76,101], folder='nodes-tests', lifetime=lifetime)
    print('\n')
    tp.generateGraph('Overhead', ['WRF','MRHOF'],[31,51,76,101], folder='nodes-tests', lifetime=lifetime)
    print('\n')
    tp.generateGraph('Energy',  ['WRF','MRHOF'], [31,51,76,101], folder='nodes-tests', lifetime=lifetime)
    plt.show()

    # tp.generateGraph('PDR', ['MRHOF','OF0','WRF'],[25], folder='sim-3')
    # tp.generateGraph('Overhead', ['MRHOF','OF0','WRF'],[25], folder='sim-3')
    # tp.generateGraph('Energy', ['MRHOF','OF0','WRF'],[25], folder='sim-3')
    # tp.generateGraph('Lifetime', ['MRHOF','OF0','WRF'],[25], folder='sim-3')

    # from classes.topology_generator import Topologies
    # top = Topologies(1, 'mySimulation', 75,1.0,0.9, [100,100], startInterval=[-100,-100], TR=70, IR=90)
    # top.generate()

    # main()
