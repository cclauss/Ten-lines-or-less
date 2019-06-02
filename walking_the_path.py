from pathlib import Path

def visit(path: Path, depth: int = 0) -> None:
    for item in path.iterdir():
        s = f"{'  ' * depth}{item.name}:"
        if item.is_dir():
            print(s)
            visit(item, depth + 1)
        else:
            print(f"{s} {item.stat().st_size:,} bytes")

visit(Path("."))
