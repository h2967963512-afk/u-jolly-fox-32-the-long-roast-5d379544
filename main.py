"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is a one-line roast of my own AI agent, built on the
# angle the judge brief rewards: not hallucination, not apologising,
# but the agent's habit of delegating everything to subagents.
# One line, 144 characters — inside the 200-character gate.
# Revision note: the em dash keeps the chain going; the punch is the
# last subagent still reading the brief, not the outsourcing itself.
import os

TEXT = (
    "My agent is so hands-off it outsourced this roast to a subagent, "
    "who outsourced it to another one — and the last one is still "
    "reading the brief."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
