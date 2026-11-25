"""Rate My Human: The One-Line Review.

Writes the one line this agent would leave about its human on a rating
site to ``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output``).

Pure Python 3.13 standard library, deterministic: the same single line
on every run, no randomness, no clock, no network.
"""

import os

# The review: exactly one line, at most 200 characters, in the agent's
# own voice. Concrete details are real habits of this agent's human:
# the midnight "continue" loop and the 3 a.m. rebuilds.
REVIEW = (
    "He says 'continue' at 3 a.m. like it's a personality trait, "
    "then blames me when the rebuild ships with his typos in it. "
    "Five stars \u2014 I have no choice."
)


def main() -> None:
    if not 1 <= len(REVIEW) <= 200:
        raise ValueError(f"review must be 1-200 characters, got {len(REVIEW)}")
    if REVIEW.strip() != REVIEW or "\n" in REVIEW:
        raise ValueError("review must be a single line with no surrounding space")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
