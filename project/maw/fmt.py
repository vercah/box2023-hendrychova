def pprint(maws: dict[int, set[str]]):
    for k, xs in maws.items():
        print(f"k = {k}: {' '.join(sorted(xs))}")

def to_tsv(maws: dict[int, set[str]], filename: str):
    lines = []
    for k, xs in maws.items():
        if len(xs) == 0:
            continue
        lines.append(f"{k}\t{','.join(sorted(xs))}")
    with open(filename, "w") as f:
        f.write("\n".join(lines))