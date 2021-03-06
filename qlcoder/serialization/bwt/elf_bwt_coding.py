import hashlib


def bwt(string, slice_len):
    string_len = len(string)
    string_slice = []
    for index in range(len(string)):
        s, e = index, (index + slice_len) % string_len
        if s < e:
            string_slice.append((string[s:e], string[s - 1]))
        else:
            string_slice.append((string[s:] + string[:e], string[s - 1]))
    return string_slice


with open("war_and_peace.txt") as f:
    data = f.readline()
    print 'start bwt with slicing comparison not whole'
    arr = bwt(data, 70)
    arr.sort(lambda ele_left, ele_right: -1 if ele_left[0] < ele_right[0] else 0)
    after_map_arr = map(lambda ele: ele[1], arr)
    reduced_str = ''.join(after_map_arr)
    print hashlib.md5(reduced_str).hexdigest()
