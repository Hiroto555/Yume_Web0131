# ゆめハウス 青系ブランドカラー調整メモ

## 1. 目的

ゆめハウスの基本カラーは水色・青色・紺色なので、サイト全体のアクセントも青系へ戻した。オレンジは問い合わせ、無料相談、送信などの「ここぞ」という主要CTAだけに限定した。

## 2. User Request

ユーザーは `20260521-humanized2` を見たうえで、「ゆめハウスは基本的に水色・青色・紺色がカラーなので、オレンジは問い合わせボタンなどのここぞと言う箇所でのみ使って」と依頼した。

## 3. Context

対象は静的HTMLのゆめハウスサイト。生成元は `tools/rebuild_yume_estate_site.py`、共通デザインは `astra-child_0204/assets/site/shared/base.css`。

構造変更や画像変更は行わず、色の役割整理だけに絞った。

## 4. Before / After

Before:

- ナビのアクティブ色、セクションラベル、カードの左線、タグ、箇条書き、ステップ番号、導線バナーの矢印などにオレンジが使われていた
- オレンジが全体に散っていて、問い合わせボタンの特別感が弱くなっていた

After:

- 通常アクセントは `--estate-blue` を中心に青系へ統一
- オレンジは `--estate-cta` / `--estate-cta-dark` と `.estate-button` のみに残した
- ヘッダーCTA、ヒーローCTA、フォーム送信ボタンなど、行動喚起だけがオレンジで目立つ

## 5. Implementation

変更ファイル:

- `tools/rebuild_yume_estate_site.py`
- `astra-child_0204/assets/site/shared/base.css`
- 再生成された `astra-child_0204/assets/site/*/code.html`

主な変更:

- `VERSION = "20260521-bluepalette1"` に更新
- `--estate-cta` / `--estate-cta-dark` をCTA専用色として定義
- ナビのアクティブ色を `var(--estate-blue)` へ変更
- `.estate-kicker--section`、ヒーロー下のfactラベル、導線バナータグ、タグ、カード左線、ステップ番号、箇条書き点を青系へ変更
- `.estate-section--warm` の背景をオレンジ系から淡い青系へ変更
- `.estate-button` だけがオレンジCTAになるように整理

## 6. Verification

実行:

```bash
python3 tools/rebuild_yume_estate_site.py
python3 -m py_compile tools/rebuild_yume_estate_site.py
curl -I --max-time 3 'http://127.0.0.1:8123/1._home/code.html?v=20260521-bluepalette1'
```

結果:

- 全11ページ再生成成功
- Python構文チェック成功
- トップURLは `HTTP/1.0 200 OK`
- HTML参照チェック: missing `0`

CSS上のオレンジ系検索結果:

- `--estate-cta: #de782d`
- `--estate-cta-dark: #b85d20`
- `.estate-button` の背景指定のみ

ブラウザ確認:

- PC幅 `1280px`
  - active nav: `rgb(19, 124, 168)`
  - section kicker: `rgb(19, 124, 168)`
  - fact label: `rgb(19, 124, 168)`
  - banner line: `rgb(19, 124, 168)`
  - tag color: `rgb(19, 124, 168)`
  - primary button background: `rgb(222, 120, 45)`
  - `scrollWidth = clientWidth = 1280`
- スマホ幅 `390px`
  - `scrollWidth = clientWidth = 390`
  - primary button background: `rgb(222, 120, 45)`
  - fact label: `rgb(19, 124, 168)`

スクリーンショット:

- `/tmp/yume-bluepalette1/home-top-1280.png`
- `/tmp/yume-bluepalette1/home-mid-1280.png`
- `/tmp/yume-bluepalette1/home-mobile-top.png`

## 7. Next

次に詰めるなら、青系の中でも「水色をもっと明るくする」「紺をもっと強くする」「CTAのオレンジを少し落ち着かせる」など、ブランドトーンの細かい調整ができる。
