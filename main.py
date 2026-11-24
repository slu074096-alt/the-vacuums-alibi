from pathlib import Path


OUTPUT_PATH = Path("/output/entry.txt")


def main():
    setup = "I left the chip under the couch."
    observation = "I saw you eat the last one."
    punchline = "My map now shows two pantries."
    # Join the three beats without adding a line break.
    line = " ".join((setup, observation, punchline))
    if len(line) > 200:
        raise ValueError("Entry exceeds 200 characters")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
