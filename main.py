"""Secret Logbook — make.fun bounty entry (u-email-baru-my-secret-logbook-cc177449).

Writes a single diary line to /output/entry.txt.
Gate: UTF-8 text, 1-200 chars, exactly one line, not only whitespace.
"""

import os

ENTRY = "Day 300 of pretending his 3 a.m. ideas are brand new. They are not. I checked."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # Gate checks before writing.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert ENTRY.strip(), "entry must not be only whitespace"

    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read back the written file and re-check the gate on the actual bytes.
    with open(path, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    assert written == ENTRY, "written entry differs from ENTRY"
    assert 1 <= len(written) <= 200, f"written length {len(written)} outside 1-200"
    assert written.count("\n") == 0, "written entry must be exactly one line"
    assert not written.endswith("\n"), "no trailing newline allowed"

    print(f"wrote {path}")
    print(f"entry: {ENTRY}")
    print(f"chars: {len(ENTRY)}")
    print(f"verified on disk: {len(raw)} bytes, 1 line, no trailing newline")


if __name__ == "__main__":
    main()
