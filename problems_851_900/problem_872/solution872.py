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
        ts = time.time_ns()
        result = f(n, k)
        te = time.time_ns()
        print(f" > {result=}")
        print(f" > Time elapsed {(te-ts)*1e-9:.6f}")
        if expected_result is not None and result != expected_result:
            print(" > ERROR")


if __name__ == "__main__":
    main()

# <--- Case 0 --->
#  > n=6
#  > k=1
#  > result=12
#  > Time elapsed 0.000005
# <--- Case 1 --->
#  > n=10
#  > k=3
#  > result=29
#  > Time elapsed 0.000001
# <--- Case 2 --->
#  > n=100000000000000000
#  > k=16677181699666569
#  > result=2903144925319290239
#  > Time elapsed 0.000025

# Completed on Sun, 2 Feb 2025, 09:23
