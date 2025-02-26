from pathlib import Path
import sys


def main(
    file_content: str, uniq: bool = False, count: bool = False, repeated: bool = False
) -> str:
    lines = file_content.splitlines()
    result = []
    line_counts = {}

    for line in lines:
        line_counts[line] = line_counts.get(line, 0) + 1

    if repeated and count:
        return "\n".join(
            f"{count} {line}" for line, count in line_counts.items() if count > 1
        )
    if repeated:
        return "\n".join(line for line, count in line_counts.items() if count > 1)
    if count:
        return "\n".join(f"{count} {line}" for line, count in line_counts.items())
    if uniq:
        return "\n".join(line for line, count in line_counts.items() if count == 1)
    else:
        result = lines

    return "\n".join(result)


def _cli() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", nargs="?", type=str, default="-")
    parser.add_argument("-u", dest="uniq", action="store_true", default=False)
    parser.add_argument("-c", "--count", action="store_true", default=False)
    parser.add_argument("-d", "--repeated", action="store_true", default=False)
    args = parser.parse_args()

    if args.filepath == "-":
        content = sys.stdin.read()
    else:
        content = Path(args.filepath).read_text(encoding="utf-8")

    result = main(content, args.uniq, args.count, args.repeated)
    print(result)


if __name__ == "__main__":
    _cli()
