# ゆめハウス 強い青系カラー調整メモ

## 1. 目的

`20260521-openlayout1` は open layout 化で box 感は下がったが、青系の色が薄く、全体が少し力弱く見えていた。今回は構造を変えず、ゆめハウスらしい水色・青・紺の存在感を強めた。

## 2. User Request

ユーザーは「色が薄いのがなんとなく力弱い」と指摘した。

## 3. Context

対象は静的HTML生成サイト。生成元は `tools/rebuild_yume_estate_site.py`、共通CSSは `astra-child_0204/assets/site/shared/base.css`。

前回までの方針である「オレンジは主要CTAだけ」「boxを減らす open layout」は維持した。

## 4. Before / After

Before:

- 青系の線とラベルが淡く、全体の骨格が弱かった
- open layout にしたことで、白場が増えたぶん、色の支えが不足して見えた
- スマホのヒーロー見出しが少し詰まり気味だった

After:

- 紺、青、罫線色を一段濃くした
- 淡い背景帯も白に近すぎない青系へ調整
- ヒーローの青みとコントラストを少し上げた
- hero facts、導線行、カード罫線、タグ、ステップ番号、FAQ罫線を強めた
- スマホのヒーロー見出しサイズを少し下げ、窮屈さを緩和した

## 5. Implementation

変更ファイル:

- `tools/rebuild_yume_estate_site.py`
- `astra-child_0204/assets/site/shared/base.css`
- 再生成された `astra-child_0204/assets/site/*/code.html`

主な変更:

- `VERSION = "20260521-strongblue1"`
- `--estate-navy`: `#0d2f46`
- `--estate-blue`: `#0077a8`
- `--estate-blue-deep`: `#005f89`
- `--estate-line`: `#b9d1dd`
- `--estate-blue-soft-line`: `#8fc8dc`
- soft/warm セクション背景を少し濃い青系へ変更
- hero facts の上線を `5px` にし、背景に薄い青を追加
- 物件カード、テキストブロック、バナー、FAQ、ステップの罫線を青系へ変更
- ステップ番号とリンク矢印は、青線＋薄青背景で少し強くした
- スマホ見出しを `clamp(1.55rem, 6.6vw, 2rem)` に調整

## 6. Verification

実行:

```bash
python3 tools/rebuild_yume_estate_site.py
python3 -m py_compile tools/rebuild_yume_estate_site.py
curl -I --max-time 3 'http://127.0.0.1:8123/1._home/code.html?v=20260521-strongblue1'
```

結果:

- 全11ページ再生成成功
- Python構文チェック成功
- トップURLは `HTTP/1.0 200 OK`
- HTML参照チェック: missing `0`

Chromeスクリーンショット:

- `/tmp/yume-strongblue1/chrome/home-top-1280.png`
- `/tmp/yume-strongblue1/chrome/home-mobile-390.png`

Chrome 実行時に OS integration / GPU 系の warning は出たが、PNG生成は成功した。

## 7. 次の確認ポイント

次に詰めるなら、以下を画面で見ながら決める。

- 青をさらに濃くして金融・士業寄りにするか
- 水色を少し増やして親しみを出すか
- CTAのオレンジを今より少し落ち着いた橙にするか
- 下層ページの背景帯をページごとに変えるか
