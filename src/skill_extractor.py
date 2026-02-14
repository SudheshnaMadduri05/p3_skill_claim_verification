def load_text(file_path: str) -> str:
    """
    Load text from a file safely.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
