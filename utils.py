def get_input(day: int, split_line=True) -> str:
    with open(f"inputs/day{day}", "r") as f:
        content = f.read()
        if split_line:
            return content.splitlines()
        else:
            return content