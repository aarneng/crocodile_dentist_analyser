from collections import defaultdict
import json


def split_data(fname):
    ret = []
    with open(fname, "r") as f:
        c = 0
        for line in f:
            for n in line.split(" "):
                c += 1
                ret.append(int(n))
    return ret


def pretty_print(data):
    print(json.dumps(data), indent=4)


def anal(data):
    # analyse  the data to find the occurrences of the next number
    nums = defaultdict(lambda: defaultdict(lambda: 0))
    for i, d in enumerate(data[:-1]):
        nums[d][data[i + 1]] += 1
    return nums


def anal2(data):
    # analyse  the data to find the occurrences of the next number
    nums = defaultdict(lambda: defaultdict(lambda: 0))
    for i, d in enumerate(data[:-3]):
        nums[(d, data[i + 1], data[i + 2])][data[i + 3]] += 1
    return nums


def normalise_data_highroll(data):
    vals = defaultdict(lambda: 0)
    for k, v in data.items():
        for k2, v2 in v.items():
            if k2 > k:
                x = k2 - k
            else:
                x = k2 + 14 - k - 5
            vals[x] += v2
    vals = {k: v for k, v in sorted(vals.items(), key=lambda item: -item[1])}  # sort form high to low occurrence
    return vals


def main():
    """
    note: for now, this function only works with low-to-high datasets
    """
    data = split_data("low-to-high-data3.txt")
    # d = anal(data)  # analyse the data
    # for i in range(1, 10):
    #     v = d[i]
    #     print(f"{i}: {sum(i for i in v.values())} ->", {k: v for k, v in sorted(v.items(), key=lambda item: -item[1])})

    d = anal2(data)  # analyse the data
    for k, v in d.items():
        print(k, v)

    data_norm1 = normalise_data_highroll({k: v for k, v in d.items() if k >= 6})

    print()
    print("variance for rho on high rolls (6-9):")
    print(data_norm1)
    print(f"total: {sum(i for i in data_norm1.values())} rolls")
    data_norm2 = normalise_data_highroll({k: v for k, v in d.items() if k <= 2})
    print()
    print("variance for rho on high rolls (6-9):")
    print(f"total: {sum(i for i in data_norm2.values())} rolls")
    print(data_norm2)


if __name__ == '__main__':
    main()
