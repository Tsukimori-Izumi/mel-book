"""
FizzBuzz ML Program
==================
MLE-book プロセスに基づいて開発された機械学習ベースのFizzBuzzプログラム。

アーキテクチャ: MLE2-output.md 参照
要件: MLE1-output.md 参照
上位要求: req1 (fizzbuzzを行うプログラム)
"""

import numpy as np
from sklearn.neural_network import MLPClassifier


# === DataGenerator ===
def generate_data(start: int = 1, end: int = 100):
    """学習データを生成する (MLR-004)"""
    X = np.arange(start, end + 1).reshape(-1, 1)
    y = []
    for x in X.flatten():
        if x % 15 == 0:
            y.append(2)   # FizzBuzz
        elif x % 3 == 0:
            y.append(0)   # Fizz
        elif x % 5 == 0:
            y.append(1)   # Buzz
        else:
            y.append(3)   # 数値そのまま
    return X, np.array(y)


# === FeatureExtractor ===
def extract_features(X: np.ndarray) -> np.ndarray:
    """特徴量を抽出する: [x, x%3, x%5, x%15] (MLE2.AC03改善提案適用)"""
    x = X.flatten()
    features = np.column_stack([
        x,
        x % 3,
        x % 5,
        x % 15,
    ])
    return features


# === LabelDecoder ===
LABEL_MAP = {0: "Fizz", 1: "Buzz", 2: "FizzBuzz", 3: None}


def decode_labels(predictions: np.ndarray, original_values: np.ndarray) -> list:
    """クラスIDをラベル文字列に変換する (MLR-005)"""
    results = []
    for pred, val in zip(predictions, original_values.flatten()):
        label = LABEL_MAP[pred]
        results.append(label if label is not None else str(int(val)))
    return results


# === Main Pipeline ===
def main():
    # 1. データ生成 (MLR-004)
    X_raw, y = generate_data(1, 100)

    # 2. 特徴量抽出
    X = extract_features(X_raw)

    # 3. モデル構築・学習 (MLR-001, 01-54 ハイパーパラメータ)
    model = MLPClassifier(
        hidden_layer_sizes=(64, 32),
        activation="relu",
        solver="adam",
        max_iter=2000,
        random_state=42,
        learning_rate_init=0.001,
    )
    model.fit(X, y)

    # 4. 予測
    predictions = model.predict(X)

    # 5. ラベル変換・出力 (MLR-005)
    labels = decode_labels(predictions, X_raw)

    # 6. 精度確認 (MLR-003)
    accuracy = np.mean(predictions == y)
    print(f"=== FizzBuzz ML Results (Accuracy: {accuracy:.1%}) ===\n")

    for val, label in zip(X_raw.flatten(), labels):
        print(f"{val}: {label}")

    # 7. テキストファイルに出力
    output_path = "fizzbuzz_result.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"=== FizzBuzz ML Results (Accuracy: {accuracy:.1%}) ===\n\n")
        for val, label in zip(X_raw.flatten(), labels):
            f.write(f"{val}: {label}\n")
    print(f"\n結果を {output_path} に出力しました。")


if __name__ == "__main__":
    main()
