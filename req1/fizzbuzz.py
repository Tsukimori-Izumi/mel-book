"""
FizzBuzz ルールベースプログラム
==============================
MLE-book プロセスに基づいて開発されたルールベースのFizzBuzzプログラム。

アーキテクチャ: MLE2-output.md 参照
要件: MLE1-output.md 参照
上位要求: req1 (fizzbuzzをルールベースで行うプログラム)
"""


# === RuleEngine ===
def fizzbuzz(n: int) -> str:
    """FizzBuzzルール判定 (MLR-001, MLR-002)"""
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


# === OutputFormatter ===
def format_results(start: int = 1, end: int = 100) -> list:
    """結果をフォーマットする (MLR-004)"""
    return [(n, fizzbuzz(n)) for n in range(start, end + 1)]


def main():
    results = format_results(1, 100)

    # コンソール出力
    print("=== FizzBuzz Results (Rule-Based) ===\n")
    for n, result in results:
        print(f"{n}: {result}")

    # ファイル出力 (MLR-004-b)
    output_path = "fizzbuzz_result.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("=== FizzBuzz Results (Rule-Based) ===\n\n")
        for n, result in results:
            f.write(f"{n}: {result}\n")
    print(f"\n結果を {output_path} に出力しました。")


if __name__ == "__main__":
    main()
