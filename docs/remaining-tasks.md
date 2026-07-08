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

旧root直下には、移行前の公開用HTML、CSS、カテゴリフォルダがまだ残っている。

今回は破壊的操作を避けるため、旧root公開物の削除は未完了として保留した。

ただし、GitHub Actions / FTP Deploy の公開対象は `local-dir: ./site/` であるため、旧root公開物は現時点ではWeb公開対象外である。

次回作業では、削除前に次を一覧化して手動承認を得る。

- 削除候補パス一覧
- `site/` 側に対応する移行済みパス
- redirect が必要なもの
- 削除せず保留すべきもの
- 削除コマンド案

## Future categories

次の棚は分類として定義されているが、現時点では独立カテゴリページを持たない。

- `30 liminal/`
- `40 names/`
- `50 culture/`

トップページと `about/` ではアンカーまたは予定棚として扱っている。実ページ化する場合は、`site/index.html`、`site/about/index.html`、`docs/classification.md` を同期する。
