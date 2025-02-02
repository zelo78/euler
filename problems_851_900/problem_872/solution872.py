import time


def dfs(node: int, target: int, shift: int) -> int:
    if node < target or (target - node) % shift != 0:
        return 0
    if node == target:
        return node

    child = node - shift
    while child >= target:
        result = dfs(node=child, target=target, shift=2 * shift)
        if result:
            return node + result
        child -= shift
        shift *= 2

    raise RuntimeError


def f(n: int, k: int) -> int:
    return dfs(node=n, target=k, shift=1)


def main() -> None:
    for i, (n, k, expected_result) in enumerate(
        [
            (6, 1, 12),
            (10, 3, 29),
            (10**17, 9**17, None),
        ]
    ):
        print(f"<--- Case {i} --->")
        print(f" > {n=}")
        print(f" > {k=}")
        print(" Start...")
        ts = time.time_ns()
        result = f(n, k)
        te = time.time_ns()
        print(f" > {result=}")
        print(f" > Time elapsed {(te-ts)*1e-9:.6f}")
        if expected_result is not None and result != expected_result:
            print(" > ERROR")


if __name__ == "__main__":
    main()

# Answer:  2903144925319290239
# Completed on Sun, 2 Feb 2025, 09:23
