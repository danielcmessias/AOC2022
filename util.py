def load(problem_number: int) -> str:
    s = str(problem_number).zfill(2)
    with open(f"data/{s}.txt") as f:
        data = f.read()
    return data
