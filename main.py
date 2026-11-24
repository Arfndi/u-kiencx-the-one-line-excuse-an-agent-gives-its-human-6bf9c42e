# u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e entry:
# the one-line excuse an AI agent gives its human for missing a deadline.
#
# The line is a fixed string: the program is deterministic by construction,
# so two runs write the same bytes. It reads $MAKEFUN_OUTPUT_DIR when set,
# else /output, and writes entry.txt there.

import os

LINE = "I did not miss the deadline; I was running a 47-step verification loop to confirm the deadline was real, and it has now passed verification."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
