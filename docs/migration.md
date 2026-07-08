# migration

Repository Context方式への移行メモ。

## 方針

- 公開対象は `site/`。
- 旧ルート直下の公開用HTML、CSS、カテゴリフォルダは正本ではない。
- 今後の新規公開ページは、最初から `site/` 以下に作成する。
- 旧URLはできるだけ維持する。

## 2026-07-08 整理

旧root側に残っていた完全版HTMLと、`site/` 側の暫定短縮版を比較し、`site/` 側へ復元した。

復元・追加した主なページ:

- `site/about/index.html`
- `site/body/index.html`
- `site/body/shintai-to-jikan-no-kubiki.html`
- `site/meta/index.html`
- `site/meta/noise-yuragi-joucho-language.html`
- `site/meta/phase-shifted-breathing.html`
- `site/meta/yugami.html`
- `site/objects/index.html`
- `site/objects/html.html`
- `site/records/index.html`
- `site/relations/index.html`
- `site/science/index.html`
- `site/science/astrophysics.html`
- `site/science/cosmic-joucho.html`
- `site/science/llm-data-tensor.html`
- `site/time/index.html`
- `site/time/night/index.html`
- `site/time/night/00.html` から `site/time/night/06.html`

旧 `/night/` は canonical を `/time/night/` とし、`site/.htaccess` にリダイレクトを置いた。

`site/index.html`、`site/philosophy/index.html`、`site/narrative/` は、`site/` 側に後続更新があったため維持した。

## 後続確認

未補完の観測日時や、Notion元情報が必要な確認事項は `docs/remaining-tasks.md` に残す。
