if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    sar = set(arr)
    sar.remove(max(sar))
    print max(sar)