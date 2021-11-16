import sys
import collections


def analyze_masks(masks_input):
    # print(masks_input)
    masks = []
    # Remove the < and > and the trailing intergers
    for m in masks_input:
        m_tmp = m[1:-1]

        # trailing ints
        m_tmp = m_tmp[:-3]

        masks.append(m_tmp)
    # print(masks)
    # print(collections.Counter(masks))
    counter = collections.Counter(masks)
    for p in counter.most_common():
        print(p)


def start(inputfile):
    print(f"reading file {inputfile}")

    input_data = []
    with open(inputfile, 'r') as f:
        input_data = f.readlines()

    # print(input_data)

    file_total_num = 0
    file_mask_count = 0
    masks = []

    for i in range(2):
        row = input_data[i]
        print(row)
        splitted = row.split(' ')
        total_num = len(splitted)
        file_total_num += total_num

        # loop tokens to get the num of tokens starting with < and ending in >
        mask_count = 0
        for w in splitted:
            if w.startswith('<') and w.endswith('>'):
                mask_count += 1
                masks.append(w)
        file_mask_count += mask_count

        percentage = (mask_count / total_num) * 100
        print(
            f'total num of tokens: {total_num}, num of masked tokens: {mask_count} ({percentage:.2f}%)')

    print()
    file_percentage = (file_mask_count / file_total_num) * 100
    print(
        f'File total num of tokens: {file_total_num}, masked tokens: {file_mask_count} ({file_percentage:.2f}%)')

    analyze_masks(masks)


if __name__ == "__main__":
    inputfile = sys.argv[1]
    start(inputfile)
