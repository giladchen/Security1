import matplotlib.pyplot as plt

from common_funcs import open_wireshark_csv

if __name__ == '__main__':
    df = open_wireshark_csv('resources/7A.csv')
    df.filter(['time', 'len'])
    # print(df)
    points = [(0, 0)]
    curr_time, curr_len = 0, 0
    point_x, point_y = 2, 0
    for index, row in df.iterrows():
        curr_time = row['time']
        curr_len = row['len']
        # advancing points
        while curr_time > point_x:
            print(f'Point ready: ({point_x}, {point_y})')
            points.append((point_x, point_y))
            point_x += 2
            point_y = 0
        point_y += curr_len
    print(f'LAST POINT ({curr_time}, {curr_len})')
    x, y = zip(*points)
    print(f'x: {x}\n y: {y}')
    plt.scatter(x, y)
    plt.show()

    # df_filter = df['time'] < 2
    # df_2_sec = df[df_filter]
    # df_2_sec.plot(x='time', y='len', kind='scatter')
    # plt.show()
