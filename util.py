def load(problem_number: int) -> str:
    if problem_number < 0:
        s = "test"
    else:
        s = str(problem_number).zfill(2)
    with open(f"data/{s}.txt") as f:
        data = f.read()
    return data
