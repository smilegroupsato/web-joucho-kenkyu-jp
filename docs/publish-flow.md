# publish-flow｜公開手順

Notion公開キューからWeb公開する手順。

1. Notionの対象ページを読む。
2. タイトル、Slug、副題、本文、主要テーマ、観測日時を確認する。
3. `docs/classification.md` に従ってカテゴリを決める。
4. `site/` 以下にHTMLを作成する。
5. 観測記録ページのメタ情報に、判明している範囲で `observed:` を入れる。
6. カテゴリindexに追加する。
7. 必要なら `site/index.html` の `newly cataloged` に追加する。
8. 必要なら `site/about/index.html` の shelves を更新する。
9. `sgos-site-tree.config.json` の棚名・表示順と矛盾がないか確認する。
10. 相対リンク、CSSパス、モバイル表示を確認する。
11. `python -m unittest discover -s tests -v` を実行する。
12. `python scripts/build_sgos_site_tree.py` を実行し、`site/sgos-site-tree.json` を生成する。
13. 生成JSONのページタイトル、URL、階層、件数を確認する。
14. GitHubへcommit/pushする。
15. Notion公開キューに公開URLと公開状態を反映する。

GitHubに反映していない場合は、公開済みとは言わない。

Notionを実際に更新したときだけ、Notion反映済みとして報告する。

## SGOS Site Tree

`site/sgos-site-tree.json` は、SGOS Consoleが公開サイトの構造を読み取るための派生データである。

- HTML/CSSの公開実装が正本であり、JSONは正本ではない。
- JSONを手編集しない。
- 公開のたびに `scripts/build_sgos_site_tree.py` で再生成する。
- ページの`<h1>`を表示名として優先し、存在しない場合は`<title>`を使う。
- `site/`以下のディレクトリ構造を、section / group / page の階層へ変換する。
- 空の棚は`sgos-site-tree.config.json`に定義された場合のみ残す。
- 生成または検証に失敗した場合は、GitHub ActionsのFTP公開を止める。

公開後の取得先：

`https://joucho-kenkyu.jp/sgos-site-tree.json`

## Deploy

GitHub Actions / FTP Deploy は `site/` 以下だけを公開する。

処理順：

1. Python環境を準備する。
2. サイトツリー生成器のテストを実行する。
3. `site/sgos-site-tree.json` を生成・検証する。
4. `site/` 以下をFTP公開する。

`.github/workflows/` を変更する場合は、`local-dir: ./site/` が維持されているか確認する。

## 更新履歴

- 2026-07-18：SGOS Site Treeの生成・検証を公開必須工程へ追加。
