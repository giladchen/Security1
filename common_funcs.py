import matplotlib.pyplot as plt
import pandas as pd


def open_wireshark_csv(file_path):
    headers = ["num", "time", "src", "dst", "protocol", "len", "info"]
    dtypes = {'num': int, 'time': float,
              'src': str, 'dst': str,
              'protocol': str, 'len': int,
              'info': str}
    return pd.read_csv(file_path, skiprows=1, names=headers, dtype=dtypes)
