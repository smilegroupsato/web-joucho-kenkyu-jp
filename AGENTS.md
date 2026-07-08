# AGENTS.md

Codex / AI 作業者は、このリポジトリで作業する前に、対象リポジトリが `smilegroupsato/web-joucho-kenkyu-jp` であることを確認する。

過去に別リポジトリを扱っていたチャットでも、`web-genai-ron-jp` などの前提を持ち込まない。

## Read First

作業前に読むこと。

- `REPOSITORY_CONTEXT.md`
- `docs/classification.md`
- `docs/publish-flow.md`
- `docs/writing-rules.md`
- `docs/notion-sync.md`
- `docs/migration.md`
- `docs/remaining-tasks.md`

## Public Files

- Web公開対象は `site/` 以下のみ。
- 新規HTML、CSS、画像などの公開物は `site/` 以下に置く。
- ルート直下に公開用 `index.html` やカテゴリフォルダを作らない。
- `docs/`、`README.md`、`AGENTS.md`、`REPOSITORY_CONTEXT.md` は公開対象ではない。

## Publish Workflow

1. Notion公開キューまたは既存HTMLの内容を確認する。
2. `docs/classification.md` に従ってカテゴリを決める。
3. `site/` 以下にHTMLを作成または更新する。
4. カテゴリindexを更新する。
5. 必要なら `site/index.html` の `newly cataloged` を更新する。
6. 可能な範囲で観測日時 `observed:` を表示する。
7. リンク切れと相対パスを確認する。
8. Notionを実際に更新した場合だけ、Notion反映済みとして報告する。

## Category Updates

分類番号、カテゴリ名、説明は次を揃える。

- `site/index.html`
- `site/about/index.html`
- 各カテゴリindex
- `docs/classification.md`

## Rules

- 既存本文を勝手に短縮しない。
- 暫定短縮版が見つかった場合は、旧root側やNotion公開キューから完全版を確認して復元する。
- 既に `site/` 側で後続修正されたページは、`site/` 側を優先する。
- 判断に迷う場合は、差分と保留理由を報告する。
- 既存URLはできるだけ壊さない。URL変更時は `site/.htaccess` でのリダイレクトを検討する。
- HTMLコード自体を本文として表示するページでは、必ずHTMLエスケープする。
- 「——観測終了。」はCSS自動挿入ではなく本文に入れる。
- `observed:` は推測で入れない。
- force push は使用しない。

## Mobile Check

小幅画面で次を確認する。

- 長い日本語タイトルがはみ出さない。
- `pre.ascii-logo` が画面を壊さない。
- `.shelf-list` と `.record-list` が縦並びに崩れる。
- `.observation-meta` が折り返す。
- `site/time/night/index.html` が過大文字サイズにならない。
