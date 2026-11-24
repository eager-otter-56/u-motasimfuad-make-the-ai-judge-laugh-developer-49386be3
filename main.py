import os

TEXT = (
    "Prod's down because I asked the AI to delete the dead code, and it "
    "correctly flagged everything I shipped this sprint as dead \u2014 including "
    "payments, which are now resting in peace, in production."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
