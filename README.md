# web-joucho-kenkyu-jp

`joucho-kenkyu.jp` / 情緒研究 Web の静的HTML/CSSサイトを管理するリポジトリです。

このリポジトリでは、公開サイト本体と運用文書を分けて扱います。Web公開対象は `site/` 以下だけです。

## Public Site

- Main site: <https://joucho-kenkyu.jp/>
- Backup domain: `joucho.site`
- Deploy target: `site/`

GitHub Actions の FTP Deploy は `local-dir: ./site/` を公開対象にします。リポジトリルートの `README.md`、`AGENTS.md`、`REPOSITORY_CONTEXT.md`、`docs/` は公開物ではありません。

## Repository Role

このリポジトリは、単なるHTML置き場ではなく、情緒研究 Web の実装正本です。

- `site/`: 公開されるHTML/CSS
- `docs/`: 運用、分類、移行、公開手順の記録
- `REPOSITORY_CONTEXT.md`: このリポジトリ固有の前提と設計思想
- `AGENTS.md`: Codex / AI 作業者向けの作業規約

Notion は素材・公開キューの正本、GitHub は公開実装の正本として扱います。

## Current Workflow

```text
Notion public queue
-> GitHub repository
-> GitHub Actions / FTP Deploy
-> joucho-kenkyu.jp
```

公開済みと言えるのは、GitHub に反映され、`site/` からデプロイ可能な状態になったものだけです。

## Documents

作業前に最低限読む文書:

- `REPOSITORY_CONTEXT.md`
- `AGENTS.md`
- `docs/classification.md`
- `docs/publish-flow.md`
- `docs/writing-rules.md`
- `docs/notion-sync.md`
- `docs/migration.md`
- `docs/remaining-tasks.md`

## Maintenance Notes

- 新規公開ページは必ず `site/` 以下に作成する。
- 旧ルート直下の公開用HTMLやカテゴリフォルダを正本として扱わない。
- 既存URLはできるだけ維持し、変更が必要な場合はリダイレクトを検討する。
- HTMLコードそのものを本文として表示する場合は、必ずHTMLエスケープする。
- 観測記録ページには、判明している範囲で `observed:` を表示する。推測で日時を入れない。
- force push は使用しない。

## Repository Context Notes

このリポジトリは、過去に扱った別プロジェクトの構成を流用しません。分類、文体、公開対象、デプロイ方式は、情緒研究 Web 固有のものとして扱います。
