"""Lecture: for / while loops, range, break / continue, for-else."""


def sum_to_n(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def first_even(nums: list[int]) -> int | None:
    for x in nums:
        if x % 2 == 0:
            return x
    return None


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# ---------------- tests ----------------
def test_sum_to_n():
    assert sum_to_n(0) == 0
    assert sum_to_n(5) == 15


def test_first_even():
    assert first_even([1, 3, 4, 6]) == 4
    assert first_even([1, 3]) is None


def test_is_prime():
    assert [n for n in range(20) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19]


if __name__ == "__main__":
    for n in range(10):
        print(n, is_prime(n))
