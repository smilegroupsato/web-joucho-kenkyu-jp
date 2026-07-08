# remaining-tasks

Repository Context方式への整理後に残す確認事項。

## Observed metadata

次の観測記録ページは、リポジトリ内だけでは観測日時を確認できなかったため、`observed:` を推測で追加していない。

- `site/body/shintai-to-jikan-no-kubiki.html`
- `site/meta/noise-yuragi-joucho-language.html`
- `site/meta/phase-shifted-breathing.html`
- `site/meta/yugami.html`
- `site/objects/html.html`
- `site/philosophy/dataism-uchigawa-no-shukyo.html`
- `site/philosophy/simulation-kasetsu-sotogawa-no-shingaku.html`
- `site/science/astrophysics.html`
- `site/science/cosmic-joucho.html`
- `site/science/llm-data-tensor.html`
- `site/time/night/00.html`
- `site/time/night/01.html`
- `site/time/night/02.html`
- `site/time/night/03.html`
- `site/time/night/04.html`
- `site/time/night/05.html`
- `site/time/night/06.html`

Notion公開キュー側で観測日時を確認できたら、各ページの `.observation-meta` に追加する。

## Source confirmation

- `site/philosophy/dataism-uchigawa-no-shukyo.html` は旧root側にも同内容しかなく、本文の完全性はNotion元情報で確認する。

## Old root public files

旧root直下に残っていた移行前の公開用HTML、CSS、カテゴリフォルダは削除済み。

削除対象は、`site/` 側に移行済みであることを確認できた旧公開物に限定した。

削除済みの主な範囲：

- root `index.html`
- root `.htaccess`
- root `assets/style.css`
- root `about/`
- root `body/`
- root `objects/`
- root `meta/`
- root `philosophy/`
- root `science/`
- root `time/`
- root `night/`
- root `records/`
- root `relations/`

Web公開対象は引き続き GitHub Actions / FTP Deploy の `local-dir: ./site/`。

今後、旧root公開物が再発見された場合は、`site/` 側に対応する移行済みパスを確認してから削除する。

## Future categories

次の棚は分類として定義されているが、現時点では独立カテゴリページを持たない。

- `30 liminal/`
- `40 names/`
- `50 culture/`

トップページと `about/` ではアンカーまたは予定棚として扱っている。実ページ化する場合は、`site/index.html`、`site/about/index.html`、`docs/classification.md` を同期する。
