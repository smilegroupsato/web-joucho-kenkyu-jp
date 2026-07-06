# publish-flow｜公開手順

Notion公開キューからWeb公開する手順。

1. Notionの対象ページを読む。
2. タイトル、Slug、副題、本文、主要テーマを確認する。
3. `docs/classification.md` に従ってカテゴリを決める。
4. `site/` 以下にHTMLを作成する。
5. カテゴリindexに追加する。
6. `site/index.html` の newly cataloged に追加する。
7. 必要なら `site/about/index.html` の shelves を更新する。
8. Notion公開キューに公開URLと公開状態を反映する。

GitHubに反映していない場合は、公開済みとは言わない。
