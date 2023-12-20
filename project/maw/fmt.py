def pprint(maws: dict[int, set[str]]):
    for k, xs in maws.items():
        print(f"k = {k}: {' '.join(sorted(xs))}")