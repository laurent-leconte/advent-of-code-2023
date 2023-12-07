def get_input(day: int, example=False, split_line=True) -> str:
    file = f"inputs/day{day}"
    if example:
        file += "_example"
    with open(file, "r") as f:
        content = f.read()
        if split_line:
            return content.splitlines()
        else:
            return content