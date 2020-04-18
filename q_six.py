import pandas as pd
import string
from collections import Counter
from common_funcs import open_wireshark_csv


def open_files(num_questions):
    dfs = []
    for letter in string.ascii_uppercase[:num_questions]:
        file_path = f'resources/6{letter}.csv'
        dfs.append(open_wireshark_csv(file_path))
    return dfs


def get_unique_field(df, field):
    fields = df[field].tolist()
    return list(Counter(fields).keys())


def get_unique_protocols(df):
    return get_unique_field(df, 'protocol')


def get_unique_dsts(df):
    return get_unique_field(df, 'dst')


def count_dsts(df):
    unique_dsts = get_unique_dsts(df)
    return len(unique_dsts)


def count_rows(df):
    return len(df.index)


def find_max_occ_in_dict(dict):
    return max(dict, key=dict.get)


def q1(df):
    print(f'Q1: Number of unique destinations is {count_dsts(df)}')


def q2(df):
    print(f'Q2: Number of unique destinations is {count_dsts(df)}')


def q3(df):
    print(f'Q3: Number of messages is {count_rows(df)}')


def q4(df):
    len_dict = dict(Counter(df['len'].tolist()))
    print(f'Q4: Common packet size is {find_max_occ_in_dict(len_dict)}')


def q5(df):
    print(f'Q5: DNS Servers are {get_unique_dsts(df)}')


def q6(df):
    print(f'Q6: Number of video packets is {count_rows(df)}')


def q7(df):
    print(f'Q7: Number of packets with size lesser than 100 is {count_rows(df)}')


def q8(df):
    print(f'Q8: The ip 35.172.73.102 '
          f'{"did" if count_rows(df) != 0 else "did not"} '
          f'try to communicate with 132.72.81.121 using HTTP')


def q9(df):
    print(f'Q9: There are {len(get_unique_protocols(df))} protocols. They are {get_unique_protocols(df)}')


def q10(df):
    time_list = df['time'].tolist()
    time_list = sorted(time_list)
    max_diff = time_list[-1] - time_list[0]
    min_diff = time_list[1] - time_list[0]
    for i in range(len(time_list) - 1):
        diff = abs(time_list[i + 1] - time_list[i])
        if diff < min_diff:
            min_diff = diff
    print(f'Q10: The shortest time span is {min_diff}. The longest time span is {max_diff}')


if __name__ == '__main__':
    num_questions = 10
    data_frames = open_files(num_questions)
    funcs = [q1, q2, q3, q4, q5,
             q6, q7, q8, q9, q10]
    for (q, data_frame) in zip(funcs, data_frames):
        q(data_frame)
