# ゆめハウス 全体デザイン更新メモ

## 1. 目的

ユーザーの「あとは全体的にデザインを更新していって」という依頼に対して、トップだけでなく全11ページへ効く共通デザインを更新した。

今回は大きな構造変更よりも、サイト全体の粗さを消すための基礎デザイン調整を優先した。

## 2. 問題

直前の状態では、家写真の使いすぎは改善したが、まだ以下の粗さが残っていた。

- ブラウザ標準の `body` 余白で、ページ全体が少し内側に浮いて見える
- ヒーローの黒帯コピーが強すぎる
- セクション、カード、CTAの余白・角丸・影がやや均一で、少し素材感が残る
- 物件カード画像の比率が横長寄りで、不動産掲載写真らしさが弱い
- スマホヘッダーとメニュー位置の高さ調整が不十分

## 3. 方針

共通CSSを中心に更新し、全ページへ同じ質感を反映する。

優先したこと:

- 全体の余白をきちんとリセットする
- ヒーローを画面幅いっぱいに見せる
- 色を少し落ち着かせる
- カードは角丸を抑えて、業務系サイトらしい静かな見た目にする
- 物件写真は `4:3` に近づける
- スマホでも横スクロールを出さない

## 4. 実装内容

変更ファイル:

- `tools/rebuild_yume_estate_site.py`
- `astra-child_0204/assets/site/shared/base.css`
- 再生成された `astra-child_0204/assets/site/*/code.html`

主な変更:

- `VERSION` を `20260521-design-refresh2` に更新
- `.estate-page` に `margin: 0` と `overflow-x: hidden` を追加
- 色変数を少し落ち着いたトーンへ調整
- ヘッダーを `68px` からPC `76px` に調整
- `.estate-main` の上余白もヘッダー高に合わせて調整
- ヒーロー最小高さを `calc(100svh - 76px)` ベースに調整
- ヒーローの黒帯コピー幅と濃さを調整
- セクション上下余白を `clamp(72px, 8vw, 110px)` に変更
- soft/warm セクションを単色から薄いグラデーションへ変更
- カード角丸を `8px` から `6px` へ抑制
- 物件カード画像を `aspect-ratio: 4 / 3` に変更
- ポータルロゴ画像は `object-fit: contain` で潰れないように調整
- スマホ時のメニューパネル位置をヘッダー高 `68px` に合わせた

## 5. Before / After

Before:

- ページ全体に微妙な外側余白があり、ローカルHTML感が出ていた
- ヒーローやセクションがやや重く、カードの質感も少し汎用的だった
- 物件写真が横長に見え、不動産掲載写真らしさが弱かった

After:

- ページが画面端まで自然に広がる
- PCヒーロー、CTA、セクションの余白が揃った
- テキストカードと物件カードの役割差が見えやすくなった
- 物件写真が不動産掲載らしい比率になった
- スマホでも横スクロールなし

## 6. Verification

実行:

```bash
python3 tools/rebuild_yume_estate_site.py
python3 -m py_compile tools/rebuild_yume_estate_site.py
curl -I --max-time 3 'http://127.0.0.1:8123/1._home/code.html?v=20260521-design-refresh2'
```

結果:

- 全11ページ再生成成功
- Python構文チェック成功
- トップURL `HTTP/1.0 200 OK`
- HTML参照チェック: missing `0`

ブラウザ確認:

- PC幅 `1280px`
  - `bodyMargin = 0px`
  - `headerHeight = 76px`
  - `scrollWidth = clientWidth = 1280`
  - PCヒーロー背景: `hero-desktop.jpg`
  - トップ内の画像カード: `3`
  - トップ内のテキストカード: `9`

- スマホ幅 `390px`
  - `bodyMargin = 0px`
  - `headerHeight = 68px`
  - `scrollWidth = clientWidth = 390`
  - スマホヒーロー背景: `hero-mobile.jpg`

確認スクリーンショット:

- `/tmp/yume-design-refresh2/home-top-1280.png`
- `/tmp/yume-design-refresh2/home-mid-1280.png`
- `/tmp/yume-design-refresh2/home-lower-1280.png`
- `/tmp/yume-design-refresh2/home-mobile-top.png`

## 7. 次の改善案

次の段階では、さらにお手本サイト寄りにするなら以下を進める。

- ヒーローコピーの文字量を短くする
- CTAバナーの文章をさらに短くして視線誘導を強める
- トップ下部に会社・スタッフ・FAQへの導線を整理する
- 下層ページごとの見出し/余白/画像密度を個別に微調整する
- 実店舗・スタッフ写真が用意できたら会社情報/問い合わせページに反映する
