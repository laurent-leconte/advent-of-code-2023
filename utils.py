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
        
def split_by_empty_line(input: list[str]) -> list[list[str]]:
    """
    Split a list of strings by empty lines, return a list of lists of strings
    """
    acc = []
    res = []
    for line in input:
        if line == '':
            res.append(acc)
            acc = []
        else:
            acc.append(line)
    if acc:
        res.append(acc)
    return res