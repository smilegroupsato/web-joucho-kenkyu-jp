# web-joucho-kenkyu-jp

情緒研究 / JOUCHO ARCHIVE の静的HTML/CSSサイト。

## 公開サイト

- joucho-kenkyu.jp
- joucho.site は予備ドメイン

## Repository Context方式

このリポジトリでは、サイト本体と運用文書を分ける。

```text
site/  Web公開対象
docs/  運用文書
```

作業前に以下を読む。

- `REPOSITORY_CONTEXT.md`
- `AGENTS.md`
- `docs/classification.md`
- `docs/publish-flow.md`
- `docs/writing-rules.md`
- `docs/notion-sync.md`

## 公開対象

GitHub Actions のFTP Deployは、`site/` 以下を公開対象にする。
