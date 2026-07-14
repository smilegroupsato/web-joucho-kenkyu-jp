# REPOSITORY_CONTEXT.md

Repository:
`smilegroupsato/web-joucho-kenkyu-jp`

Public site:
<https://joucho-kenkyu.jp/>

Project:
情緒研究 / JOUCHO ARCHIVE

## Role

このリポジトリは、情緒研究 Web の公開実装を保持する場所である。

Notion は素材・公開キューの正本、GitHub はHTML/CSSとして公開される実装正本として扱う。

## Thought

情緒研究は、意味になる前、意味になった後、そしてその前後が撹乱される地点に立ち上がる気配を観測し、並べ、あとから再び触れられる形にするためのアーカイブである。

ここで扱うページは、ブログ記事ではなく、棚に置かれる観測記録、標本、目録項目として扱う。

## Directory Structure

```text
/
├─ site/                  Web公開対象
│  ├─ index.html
│  ├─ .htaccess
│  ├─ assets/
│  ├─ about/
│  ├─ records/
│  ├─ technology/
│  ├─ philosophy/
│  ├─ time/
│  ├─ objects/
│  ├─ science/
│  ├─ relations/
│  ├─ body/
│  ├─ narrative/
│  └─ meta/
├─ docs/                  運用文書
├─ README.md
├─ AGENTS.md
└─ REPOSITORY_CONTEXT.md
```

Web公開対象は `site/` 以下のみ。ルート直下に旧公開用HTMLやカテゴリフォルダを戻さない。

## Deploy Policy

GitHub Actions / FTP Deploy は `local-dir: ./site/` を公開対象にする。

`docs/`、`README.md`、`AGENTS.md`、`REPOSITORY_CONTEXT.md` は公開対象ではない。

## Classification

```text
00 records/      観測記録・案内・台帳
10 philosophy/   哲学・神学・宗教
11 time/         時間・時間帯・生活リズム
20 objects/      物・記録・メディア
30 liminal/      空間・無人性・境界
40 names/        薬名・商品名・言葉の響き
50 culture/      レイヴ・未参加文化・記録物
55 technology/   技術の情緒（計算機・コマンド・規格・インターフェース）
60 science/      科学概念・AI・数学
70 relations/    関係
80 body/         身体・欲望・疲労・病・老い・死
90 narrative/    物語・神話・小説・漫画・映画
99 meta/         情緒について考えるときにだけ立ち現れる情緒
```

分類は、題材名ではなく、情緒がどこで発生しているかで決める。

## Writing and Display Rules

- 軽量なHTML/CSSで書く。
- terminal / archive 風の黒背景と monospace を基本にする。
- 観測記録は説明しすぎず、本文の余白を残す。
- 「——観測終了。」はCSS自動挿入ではなく本文に入れる。
- HTMLコードそのものを本文として表示する場合は、必ずHTMLエスケープする。
- 観測記録ページには、判明している範囲で `observed:` を入れる。
- 日時が不明な場合は推測で補わず、`docs/remaining-tasks.md` に残す。

## URL Policy

既存URLはできるだけ維持する。

旧ルート公開ファイルを `site/` に統合する場合も、公開URLとしてのパスが維持されるように配置する。URL変更が必要な場合は、`site/.htaccess` にリダイレクトを置く。

## Repository Context Boundary

このリポジトリは、情緒研究 Web 固有の分類、文体、公開フローを持つ。

別プロジェクトの文書構成やテーマ切替、デプロイ前提を流用しない。汎用化できる知見は、プロジェクト固有ルールと分けて記録する。
