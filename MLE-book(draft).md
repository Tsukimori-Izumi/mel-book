```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
(作成)2026.02.02
(更新)2026.03.09
# Why，モチベーション，目的：
A－Spice4.0 PAMを生成AIで解析したところ，MLEプロセスを"__開発する機能__にAIを搭載するプロセス"と誤認識した。
組込を考えた場合，AI搭載は現実的ではない。
そこで本件では，開発プロセスにAIを使用するプロセスへテーラリングする。


![[image.png]](./image.png)
図.Automotive-SPICE-PAM_40_Japanese-1 Automotive-SPICE プロセス参照モデルの概要

# A-Spice
## A-spice4.0ドメイン（抽象）
```mermaid
flowchart LR

subgraph a-spice
	subgraph　共通プロダクト成果物ドメイン
		subgraph ドキュメント
		end
	end
	subgraph プロセス群ドメイン
		subgraph プロセスドメイン
			subgraph　プロセス成果物ドメイン[プロセス成果物ドメイン<br>作業]
			end
			subgraph 基本プラクティスドメイン[基本プラクティスドメイン<br>作業]
			end
		end
	end
end

共通プロダクト成果物ドメイン --> プロセス成果物ドメイン
プロセス成果物ドメイン --> 基本プラクティスドメイン
基本プラクティスドメイン　--> 共通プロダクト成果物ドメイン
```
<div style="text-align: center;">
図，A－Spiceのドメインアーキテクチャと，MLE-bookのドメインアーキテクチャの関係
</div>

### A-spice MLE-機械学習エンジニアリングプロセス群ドメイン
MLEプロセスは，SYS,SWE,MANを代替できるように定義される。
```mermaid
flowchart TB

subgraph a-spice
	subgraph MLE-機械学習エンジニアリングプロセス群
		subgraph MLE1[MLE.1機械学習要求分析]
		end
		subgraph MLE2[MLE.2機械学習要求アーキテクチャ]
		end
		subgraph MLE3[MLE 3 機械学習要求トレーニング]
		end
		subgraph MLE4[MLE4 機械学習要求モデルテスト]
		end
		subgraph SUP11[SUP11 機械学習データ管理]
		end
	end
end

MLE1 -->MLE2 -->MLE3 -->MLE4
MLE1 -->SUP11
MLE2 -->SUP11
MLE3 -->SUP11
MLE4 -->SUP11
```
<div style="text-align: center;">
図，MLEプロセス群のアーキテクチャ
</div>

#### MLE1ドメイン
<div style="text-align: center;">
表，MLE1のプロセス成果物と基本プラクティス
</div>

|A-Spice共通プロダクト成果物|プロセス成果ID|プロセス成果概要|基本プラクティスID|基本プラクティス概要|
|--|--|--|--|--|
|17-00要求|MLE1.PRD1|仕様化されている|MLE1.BP1|仕様化する|
|17-00要求|MLE1.PRD2|優先順位が付けられている|MLE1.BP2|優先順位をつける|
|17-54要求の属性|MLE1.PRD2|優先順位が付けられている|MLE1.BP2|優先順位をつける|
|17-54要求の属性|MLE1.PRD3|分析されている|MLE1.BP3|分析する|
|13-52情報伝達の証拠|MLE1.PRD6|伝達されている|MLE1.BP5|伝達する|
|13-51一貫性の証拠|MLE1.PRD5|双方向トレーサビリティが確立されている|MLE1.BP4|双方向トレーサビリティを確立する|
|15-51分析結果|MLE1.PRD3|分析されている|MLE1.BP3|分析する|
|15-51分析結果|MLE1.PRD4|運用環境が検討されている|MLE1.BP4|運用環境を検討する|
```mermaid
flowchart TD

17-00 --> プロセス成果ドメイン
プロセス成果ドメイン --> 基本プラクティスドメイン
基本プラクティスドメイン -- |共通成果物| --> 共通プロダクト成果物ドメイン
MLE1.PRD1 --> MLE1.BP1
MLE1.PRD2 --> MLE1.BP2
MLE1.PRD3 --> MLE1.BP3
MLE1.PRD4 --> MLE1.BP3
MLE1.PRD6 --> MLE1.BP5
MLE1.PRD5 --> MLE1.BP4

subgraph 共通プロダクト成果物ドメイン
17-00[17-00要求]
17-54[17-54要求の属性]
13-52[13-52情報伝達の証拠]
13-51[13-51一貫性の証拠]
15-51[15-51分析結果]
end
subgraph プロセス成果ドメイン
MLE1.PRD1[MLE1.PRD1<br>仕様化される]
MLE1.PRD2[MLE1.PRD2<br>優先順位がつけられる]
MLE1.PRD3[MLE1.PRD3<br>検証可能性がつけられる]
MLE1.PRD4[MLE1.PRD4<br>運用環境が検討される]
MLE1.PRD5[MLE1.PRD5<br>双方向トレーサビリティが確立される]
MLE1.PRD6[MLE1.PRD6<br>合意と伝達される]
end
subgraph 基本プラクティスドメイン
MLE1.BP1[MLE1.BP1<br>仕様化する]
MLE1.BP2[MLE1.BP2<br>優先順位づけする]
MLE1.BP3[MLE1.BP3<br>分析する]
MLE1.BP4[MLE1.BP4<br>双方向トレーサビリティする]
MLE1.BP5[MLE1.BP5<br>伝達する]
end
```

図，MLE1のプロセス成果物と基本プラクティスの関係

#### MLE2ドメイン
<div style="text-align: center;">
表，MLE2のプロセス成果物と基本プラクティス
</div>

|A-Spice共通プロダクト成果物|プロセス成果ID|プロセス成果概要|基本プラクティスID|基本プラクティス概要|
|--|--|--|--|--|
|04-51MLアーキテクチャ|MLE2.PRD1|MLアーキテクチャが作成されている|MLE2.BP1|MLアーキテクチャを作成する|
|04-51MLアーキテクチャ|MLE2.PRD2|MLアーキテクチャの初期値が決定されている|MLE2.BP2|MLアーキテクチャの初期値を決定する|
|04-51MLアーキテクチャ|MLE2.PRD3|MLアーキテクチャが評価されている|MLE2.BP3|MLアーキテクチャを分析する|
|04-51MLアーキテクチャ|MLE2.PRD4|MLアーキテクチャのインターフェイスが定義されている|MLE2.BP4|MLアーキテクチャのインターフェイスを定義する|
|04-51MLアーキテクチャ|MLE2.PRD5|MLアーキテクチャのリソース消費目標が定義されている|MLE2.BP5|MLアーキテクチャのリソース消費目標を定義する|
|13-51一貫性の証拠|MLE2.PRD6|MLアーキテクチャの双方向トレーサビリティが確立されている|MLE2.BP6|MLアーキテクチャの双方向トレーサビリティを確立する|
|13-52情報伝達の証拠|MLE2.PRD7|MLアーキテクチャが伝達されている	|MLE2.BP7|MLアーキテクチャを伝達する|
|01-54ハイパーパラメータ|MLE2.PRD1|MLアーキテクチャが作成されている|MLE2.BP1|MLアーキテクチャを作成する|
|01-54ハイパーパラメータ|MLE2.PRD2|MLアーキテクチャの初期値が決定されている|MLE2.BP2|MLアーキテクチャの初期値を決定する|
|15-51分析結果|MLE2.PRD1|MLアーキテクチャが作成されている|MLE2.BP3|MLアーキテクチャを分析する|
|15-51分析結果|MLE2.PRD3|MLアーキテクチャが評価されている|MLE2.BP3|MLアーキテクチャを分析する|

```mermaid
flowchart TB
subgraph 共通プロダクト成果物ドメイン入力
17-00[17-00要求]
17-54[17-54要求の属性]
13-52[13-52情報伝達の証拠]
13-51[13-51一貫性の証拠]
15-51[15-51分析結果]
end
subgraph 共通プロダクト成果物ドメイン出力
04-51[04-51MLアーキテクチャ]
01-54[01-54ハイパーパラメータ]
15-512[15-51分析結果]
13-522[13-52情報伝達の証拠]
13-512[13-51一貫性の証拠]
end
subgraph プロセス成果物ドメイン
MLE2.PRD1[MLE2.PRD1<br>MLアーキテクチャが作成されている]
MLE2.PRD2[MLE2.PRD2<br>MLアーキテクチャの初期値が決定されている]
MLE2.PRD3[MLE2.PRD3<br>MLアーキテクチャが評価されている]
MLE2.PRD4[MLE2.PRD4<br>MLアーキテクチャのインターフェイスが定義されている]
MLE2.PRD5[MLE2.PRD5<br>MLアーキテクチャのリソース消費目標が定義されている]
MLE2.PRD6[MLE2.PRD6<br>MLアーキテクチャの双方向トレーサビリティが確立されている]
MLE2.PRD7[MLE2.PRD7<br>MLアーキテクチャが伝達されている]
end
subgraph 基本プラクティスドメイン
MLE2.BP1[MLE2.BP1<br>MLアーキテクチャを作成する]
MLE2.BP2[MLE2.BP2<br>MLアーキテクチャの初期値を決定する]
MLE2.BP3[MLE2.BP3<br>MLアーキテクチャを分析する]
MLE2.BP4[MLE2.BP4<br>MLアーキテクチャのインターフェイスを定義する]
MLE2.BP5[MLE2.BP5<br>MLアーキテクチャのリソース消費目標を定義する]
MLE2.BP6[MLE2.BP6<br>MLアーキテクチャの双方向トレーサビリティを確立する]
MLE2.BP7[MLE2.BP7<br>MLアーキテクチャを伝達する]
end
17-00 --> MLE2.BP1
17-54 --> MLE2.BP1
15-51 --> MLE2.BP1
15-51 --> MLE2.BP2
17-00 --> MLE2.BP3
17-54 --> MLE2.BP3
15-51 --> MLE2.BP3
17-00 --> MLE2.BP4
17-54 --> MLE2.BP4
15-51 --> MLE2.BP4
17-00 --> MLE2.BP5
17-54 --> MLE2.BP5
15-51 --> MLE2.BP5
17-00 --> MLE2.BP6
17-00 --> MLE2.BP7

MLE2.BP1 --> MLE2.PRD1
MLE2.BP2 --> MLE2.PRD2
MLE2.BP3 --> MLE2.PRD3
MLE2.BP4 --> MLE2.PRD4
MLE2.BP5 --> MLE2.PRD5
MLE2.BP6 --> MLE2.PRD6
MLE2.BP7 --> MLE2.PRD7

MLE2.PRD1 --> 04-51
MLE2.PRD2 --> 04-51
MLE2.PRD3 --> 04-51
MLE2.PRD4 --> 04-51
MLE2.PRD5 --> 04-51


MLE2.PRD1 --> 01-54
MLE2.PRD2 --> 01-54

MLE2.PRD1 --> 15-512
MLE2.PRD3 --> 15-512

MLE2.PRD6 --> 13-512
MLE2.PRD7 --> 13-522


```
<div style="text-align: center;">
図，MLE2のプロセス成果物と基本プラクティスの関係
</div>

# MLE-Book
## MLE-bookドメイン(抽象)
```mermaid
flowchart LR
subgraph a-spice
	subgraph プロセス群ドメイン
		subgraph A-spiceプロセスドメイン
			subgraph 基本プラクティスドメイン
			end
		end
	end
end

subgraph SWE-book
	subgraph SWEプロセスドメイン
		subgraph SWEアクティビティドメイン
		end
	end
end
subgraph MLE-book
	subgraph MLEプロセスドメイン
		subgraph MLEアクティビティドメイン
		end
	end
end

classDef mle stroke:#f00

 基本プラクティスドメイン --> SWEアクティビティドメイン
 基本プラクティスドメイン --> MLEアクティビティドメイン
```

### MLE-bookとA-SpiceとMEL-bookプラグインのドメイン関係
```mermaid
flowchart LR
a-spiceドメイン --> MLE-bookドメイン
プラグイン[MLE-bookプラグイン-ドメイン<br>ドメイン固有の拡張] --> MLE-bookドメイン
```
<div style="text-align: center;">
図，MLE-bookの抽象アーキテクチャ
</div>

## MLE-book プラグイン-ドメイン
プロジェクトは，プラグインの有無を選択できる。
```mermaid
flowchart TB
	subgraph HILSプラグイン[人間介入プラグイン]
		MLE.PLG1[MLE.PLG1<br>レビュー]
	end
```
<div style="text-align: center;">
図，MLE-bookのプラグインアーキテクチャ
</div>

## MLE-book ドメイン
```mermaid
flowchart TB

	subgraph プロセスドメイン
		subgraph アクティビティドメイン
			subgraph タスクドメイン
				
			end
		end
		MLE1[MLE1<br>機械学習要求分析]
		MLE2[MLE2<br>機械学習要求アーキテクチャ]
		MLE3[MLE3<br>機械学習要求トレーニング]
		MLE4[MLE4<br>機械学習要求モデルテスト]
		SUP11[SUP11<br>機械学習データ管理]
	end
```
<div style="text-align: center;">
図，MLE-bookのドメインアーキテクチャ
</div>


### MLE1-アクティビティ-ドメイン

<div style="text-align: center;">
表，MLE1の基本プラクティスとアクティビティ
</div>

| 基本プラクティスID | 基本プラクティス内容        | アクティビティID            | アクティビティ内容         |
| ---------- | ----------------- | -------------------- | ----------------- |
| MLE1.BP1   | 仕様化               | MLE1.AC01            | 機械学習要求を取得し分解する。   |
| MLE1.BP2   | 運用環境              | MLE1.AC02            | 機械学習要求の実現環境を検討する。 |
| MLE1.BP3   | 優先順位              |                      |                   |
| MLE1.BP4   | 機械学習要求の検証可能性を検討する | MLE1.AC02            | 機械学習要求の検証可能性を検討する |
| MLE1.PLG1  | AC1とAC2をレビューする    | MLE1.AC03            | AC1とAC2をレビューする    |
| MLE1.BP4   || MLE1.AC04         | 双方向トレーサビリティを確立する[*1] |                   |
| MLE1.BP5   || MLE1.AC05         | 機械学習要件を伝達する          |                   |

*1: 双方向トレーサビリティは，レビューによる出戻りを防ぐため，レビューの後工程とする。

```mermaid
flowchart TB
	subgraph 基本プラクティス
		MLE1BP1[MLE1.BP1<br>仕様化]
		MLE1BP2[MLE1.BP2<br>優先順位づけ]
		MLE1BP3[MLE1.BP3<br>分析]
		MLE1BP4[MLE1.BP4<br>双方向トレーサビリティ]
		MLE1BP5[MLE1.BP5<br>伝達]
	end
	subgraph プラグイン
		MLE.PLG1[MLE.PLG1<br>レビュー]
		
	end
	
	subgraph MLE-book
		subgraph activity
			MLE1AC01[MLE1.AC01<br>機械学習要求の取得と分解]
			MLE1AC02[MLE1.AC02<br>機械学習要求の実現，検証可能性の検証と統合]
			MLE1AC03[MLE1.AC03<br>レビュー]
			MLE1AC04[MLE1.AC04<br>双方向トレーサビリティ]
			MLE1AC05[MLE1.AC05<br>機械学習要求の伝達]
		end
	end
	
	MLE1BP1 --> MLE1AC01
	MLE1BP2 --> MLE1AC02
	MLE1BP3 --> MLE1AC02
	MLE1BP4 --> MLE1AC04
	MLE1BP5 --> MLE1AC05
	MLE.PLG1 --> MLE1AC03
```
<div style="text-align: center;">
図，MLE1の基本プラクティスとactivityの関係
</div>

#### MLE1.アクティビティ01-ドメイン

| アクティビティID | アクティビティ内容    | タスクID       | タスク内容                      |
| --------- | ------------ | ----------- | -------------------------- |
| MLE1.AC01 | 機械学習要件の取得と分解 | MLE1.TA0101 | 機械学習要件を取得する                |
| MLE1.AC01 | 機械学習要件の取得と分解 | MLE1.TA0102 | 機械学習要件を分解する                |
| MLE1.AC01 | 機械学習要件の取得と分解 | MLE1.TA0103 | これまでMLE1で検討した機械学習要件を表にまとめる |

#### MLE1.アクティビティ02-ドメイン

| アクティビティID | アクティビティ内容             | タスクID       | タスク内容                |
| --------- | --------------------- | ----------- | -------------------- |
| MLE1.AC02 | 機械学習要件の実現，検証可能性の検証と統合 | MLE1.TA0201 | 機械学習要件の運用環境への影響を考慮する |
| MLE1.AC02 | 機械学習要件の実現，検証可能性の検証と統合 | MLE1.TA0202 | 機械学習要件の実現方法の可能性を考慮する |
| MLE1.AC02 | 機械学習要件の実現，検証可能性の検証と統合 | MLE1.TA0203 | 機械学習要件の検証方法の可能性を考慮する |
| MLE1.AC02 | 機械学習要件の実現，検証可能性の検証と統合 | MLE1.TA0204 | 機械学習要件を合成する          |
| MLE1.AC02 | 機械学習要件の実現，検証可能性の検証と統合 | MLE1.TA0205 | 機械学習要件の優先順位付けを記述する   |

#### MLE1.アクティビティ03-ドメイン

| アクティビティID | アクティビティ内容 | タスクID       | タスク内容               |
| --------- | --------- | ----------- | ------------------- |
| MLE1.AC03 | レビュー      | MLE1.TA0301 | AC01,AC02のレビューを実施する |

#### MLE1.アクティビティ04-ドメイン

| アクティビティID |アクティビティ内容| タスクID     | タスク内容     	         |
| --------- | --------- | ------------ | ------------ |
| MLE1.AC04 | 双方向トレーサビリティ| MLE1.TA0401 | 双方向トレーサビリティを確立する              |

#### MLE1.アクティビティ05-ドメイン

| アクティビティID | アクティビティ内容 | タスクID       | タスク内容     |
| --------- | --------- | ----------- | --------- |
| MLE1.AC05 | 機械学習要件の伝達 | MLE1.TA0501 | 機械学習要件の伝達 |

### MLE2-アクティビティ-ドメイン

<div style="text-align: center;">
表，MLE1の基本プラクティスとアクティビティ
</div>

| 基本プラクティスID | 基本プラクティス内容        | アクティビティID            | アクティビティ内容         |
| ---------- | ----------------- | -------------------- | ----------------- |
| MLE2.BP1   | MLアーキテクチャを作成する               | MLE2.AC01            | MLモデルの詳細，前処理，後処理を作成し，MLモデル，トレーニング，テストに必要となるハイパーパラメータを作成し，MLアーキテクチャエレメントについて仕様化する。   |
| MLE2.BP2   | MLアーキテクチャの初期値を決定する              | MLE2.AC02            | MLアーキテクチャの初期値を，トレーニングのための基礎として決定する。 |
| MLE2.BP3   | MLアーキテクチャのエレメントを分析する              | MLE2.AC03            | MLアーキテクチャのエレメントの分析基準を定義し，分析基準にしたがってアーキテクチャエレメントを分析する。 |
| MLE2.BP4   | MLアーキテクチャのインターフェイスを定義する | MLE2.AC04            | MLアーキテクチャのインターフェイスを定義する。 |
| MLE2.BP5   | MLアーキテクチャのリソース目標を定義する | MLE2.AC05            | MLアーキテクチャのリソース目標を定義する。 |
| MLE2.PLG1  | 	レビューする    | MLE2.AC06            | AC1，AC2，AC3，AC4，AC5をレビューする    |
| MLE2.BP5   |双方向トレーサビリティ| MLE2.AC07         | 双方向トレーサビリティを確立する[*1] |                   |
| MLE2.BP6   |MLアーキテクチャを伝達する| MLE2.AC08         | MLアーキテクチャを伝達する          |                   |

*1: 双方向トレーサビリティは，レビューによる出戻りを考慮して，レビューの後工程とする。
```mermaid
flowchart TB

subgraph 基本プラクティス
MLE2BP1[MLE2.BP1<br>MLアーキテクチャを作成する]
MLE2BP2[MLE2.BP2<br>MLアーキテクチャの初期値を決定する]
MLE2BP3[MLE2.BP3<br>MLアーキテクチャのエレメントを分析する]
MLE2BP4[MLE2.BP4<br>MLアーキテクチャのインターフェイスを定義する]
end
subgraph MLE-book
MLE2PLG1[MLE2.PLG1<br>レビューする]
subgraph アクティビティ
MLE2AC01[MLE2.AC01<br>MLMLモデルの詳細，前処理，後処理を作成し，MLモデル，トレーニング，テストに必要となるハイパーパラメータを作成し，MLアーキテクチャエレメントについて仕様化する。]
MLE2AC02[MLE2.AC02<br>MLアーキテクチャの初期値を，トレーニングのための基礎として決定する。]
MLE2AC03[MLE2.AC03<br>MLアーキテクチャのエレメントの分析基準を定義し，分析基準にしたがってアーキテクチャエレメントを分析する。]
MLE2AC04[MLE2.AC04<br>MLアーキテクチャのインターフェイスを定義する。]
end
end

MLE2BP1--> MLE2AC01
MLE2BP2--> MLE2AC02
MLE2BP3--> MLE2AC03
MLE2BP4--> MLE2AC04
```

#### MLE2.アクティビティ01-ドメイン

| アクティビティID | アクティビティ内容    | タスクID       | タスク内容                      |
| --------- | ------------ | ----------- | -------------------------- |
| MLE2.AC01 | MLアーキテクチャを作成する | MLE2.TA0101 |MLモデルの前処理，処理，後処理について仕様化する。 |
|MLE2.AC01 | MLアーキテクチャを作成する | MLE2.TA0102 |MLアーキテクチャコンポーネントを検討する |
| MLE2.AC01 | MLアーキテクチャを作成する | MLE2.TA0103 |MLモデル，トレーニング，テストに必要となるハイパーパラメータについて仕様化する。 |
| MLE2.AC01 | MLアーキテクチャを作成する | MLE2.TA0104 |MLアーキテクチャエレメントについて仕様化する。 |

#### MLE2.アクティビティ02-ドメイン

| アクティビティID | アクティビティ内容    | タスクID       | タスク内容                      |
| --------- | ------------ | ----------- | -------------------------- |
| MLE2.AC02 | MLアーキテクチャの初期値を決定する | MLE2.TA0201 |MLE2.TA0102を確認する |
| MLE2.AC02 | MLアーキテクチャの初期値を決定する | MLE2.TA0202 |MLアーキテクチャのハイパーパラメータの初期値を決定する |

#### MLE2.アクティビティ03-ドメイン

| アクティビティID | アクティビティ内容    | タスクID       | タスク内容                      |
| --------- | ------------ | ----------- | -------------------------- |
| MLE2.AC03 | MLアーキテクチャのエレメントを分析する | MLE2.TA0301 |MLアーキテクチャのエレメントの分析基準を定義する。例えば信頼性，説明可能性など |
| MLE2.AC03 | MLアーキテクチャのエレメントを分析する | MLE2.TA0302 |MLアーキテクチャのエレメントを分析する。|

#### MLE2.アクティビティ04-ドメイン

| アクティビティID | アクティビティ内容    | タスクID       | タスク内容                      |
| --------- | ------------ | ----------- | -------------------------- |
| MLE2.AC04 | MLアーキテクチャのインターフェイスを定義する | MLE2.TA0401 |MLアーキテクチャのコンポーネントに基づき内部インターフェイスを決定する|
| MLE2.AC04 | MLアーキテクチャのインターフェイスを定義する | MLE2.TA0402 |MLアーキテクチャのコンポーネントに基づき外部インターフェイスを決定する|

#### MLE2.アクティビティ05-ドメイン

| アクティビティID | アクティビティ内容    | タスクID       | タスク内容                      |
| --------- | ------------ | ----------- | -------------------------- |
| MLE2.AC05 | MLアーキテクチャのリソース目標を定義する | MLE2.TA0501 |MLアーキテクチャのコンポーネントに基づきコンポーネントのリソース目標を決定する| 
| MLE2.AC05 | MLアーキテクチャのリソース目標を定義する | MLE2.TA0502 |MLアーキテクチャのコンポーネントに基づきトレーニングおよびデプロイ時のリソース目標を決定する| 

#### MLE2.アクティビティ06-ドメイン

| アクティビティID | アクティビティ内容 | タスクID       | タスク内容               |
| --------- | --------- | ----------- | ------------------- |
| MLE2.AC06 | レビュー      | MLE2.TA0601 | AC01のレビューを実施する |
| MLE2.AC06 | レビュー      | MLE2.TA0602 | AC02のレビューを実施する |
| MLE2.AC06 | レビュー      | MLE2.TA0603 | AC03のレビューを実施する |
| MLE2.AC06 | レビュー      | MLE2.TA0604 | AC04のレビューを実施する |
| MLE2.AC06 | レビュー      | MLE2.TA0605 | AC05のレビューを実施する |

#### MLE2.アクティビティ07-ドメイン

| アクティビティID |アクティビティ内容| タスクID     | タスク内容     	         |
| --------- | --------- | ------------ | ------------ |
| MLE2.AC07 | 双方向トレーサビリティ| MLE2.TA0701 | AC01の双方向トレーサビリティを確立する              |
| MLE2.AC07 | 双方向トレーサビリティ| MLE2.TA0702 | AC02の双方向トレーサビリティを確立する              |
| MLE2.AC07 | 双方向トレーサビリティ| MLE2.TA0703 | AC03の双方向トレーサビリティを確立する              |
| MLE2.AC07 | 双方向トレーサビリティ| MLE2.TA0704 | AC04の双方向トレーサビリティを確立する              |
| MLE2.AC07 | 双方向トレーサビリティ| MLE2.TA0705 | AC05の双方向トレーサビリティを確立する              |
| MLE2.AC07 | 双方向トレーサビリティ| MLE2.TA0706 | AC06の双方向トレーサビリティを確立する              |

#### MLE2.アクティビティ08-ドメイン

| アクティビティID |アクティビティ内容| タスクID     | タスク内容     	         |
| --------- | --------- | ------------ | ------------ |
| MLE2.AC08 | MLアーキテクチャの伝達 | MLE2.TA0801 | MLアーキテクチャの伝達 |