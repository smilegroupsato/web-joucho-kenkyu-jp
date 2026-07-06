# REPOSITORY_CONTEXT｜情緒研究Web

このリポジトリは、`joucho-kenkyu.jp` の公開用静的HTML/CSSと運用文書を管理する正本リポジトリである。

## 構成

```text
/
├─ site/                 # Web公開対象
├─ docs/                 # 運用文書
├─ README.md             # 概要
├─ AGENTS.md             # 作業指示
└─ REPOSITORY_CONTEXT.md # リポジトリ文脈
```

## 公開対象

Web公開対象は `site/` 以下のみ。

GitHub Actions のFTP Deployは、原則として `local-dir: ./site/` を使う。

## 基本方針

情緒研究は、論考サイトではなく観測記録アーカイブである。

観測記録は、記事ではなく、棚・標本・目録として扱う。

黒背景、モノスペース、軽量HTML/CSSを維持する。

## 重要ルール

- GitHubに反映していないものを公開済みと言わない。
- Notionを更新していないものを Notion反映済みと言わない。
- HTMLコード自体を本文として掲載する場合は必ずエスケープする。
- 観測終了はCSSで自動付与せず、本文の一部として入れる。
- 既存URLは可能な限り壊さない。
