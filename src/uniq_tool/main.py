from pathlib import Path


def main(file_content: str, uniq: bool = False) -> str:
    lines = file_content.splitlines()
    result = []

    if uniq:
        for line in lines:
            if not line in result:
                result.append(line)
    else:
        result = lines
    
    return "\n".join(result)


def _cli() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=Path)
    parser.add_argument("-u", dest="uniq", action="store_true", default=False)
    args = parser.parse_args()

    content = args.filepath.read_text(encoding="utf-8")
    result = main(content, args.uniq)
    print(result)


if __name__ == "__main__":
    _cli()