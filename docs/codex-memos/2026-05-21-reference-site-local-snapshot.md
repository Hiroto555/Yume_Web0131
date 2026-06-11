# 住宅情報館参考サイト ローカルスナップショットメモ

## 1. This Report's Purpose

このメモは、参考サイト `https://www.jyuutakujyouhoukan.com/` をローカルに取得し、ゆめハウスサイト改善の参考として使える状態を記録するためのもの。目的は複製ではなく、構成・写真の使い方・不動産サイトらしい情報設計を分析すること。

## 2. User Request

ユーザーは「これを参考にしたい！chrome dev toolでこれをlocalに持ってくることもできるよね？」と依頼した。意図は、参考サイトをローカルで見ながら、ゆめハウスサイトの画像・雰囲気・導線改善に活かすこと。

その後、トップページだけでは足りないため「全部取り込んで！フォルダとかのpathも正しくなるように」と追加依頼があった。以降は、トップページ単体ではなく公開ページ全体をローカル参照できるミラーとして保存する方針に切り替えた。

## 3. Context

作業フォルダは `/Users/shiroto/Desktop/Blooo/Stitch_Web/Astra本番0205`。現在のゆめハウスサイトは、画像素材の質感が混ざっていて安っぽく見えるという課題がある。参考サイトは、街並み・空・港・物件カード・売却導線を組み合わせた不動産サイト。

## 4. What Was Done

Chrome DevTools MCP を使おうとしたが、既存の自動化用 Chrome プロファイルがロックされており、接続整理後に MCP transport が閉じた。そのため、このターンでは DevTools 経由の取得は断念し、同じ目的を `wget` とブラウザ確認で実行した。

取得先:

```text
reference-sites/jyuutakujyouhoukan-2026-05-21/
```

ローカル表示URL:

```text
http://127.0.0.1:8124/www.jyuutakujyouhoukan.com/index.html
```

## 5. Implementation Overview

実行したコマンド:

```bash
mkdir -p reference-sites/jyuutakujyouhoukan-2026-05-21
wget --page-requisites --convert-links --adjust-extension --span-hosts \
  --domains=www.jyuutakujyouhoukan.com,jyuutakujyouhoukan.com,fonts.googleapis.com,fonts.gstatic.com \
  --no-parent --timeout=20 --tries=2 \
  --directory-prefix=reference-sites/jyuutakujyouhoukan-2026-05-21 \
  https://www.jyuutakujyouhoukan.com/
```

結果:

- 109 files
- 37MB
- `index.html`, CSS, JS, 画像, フォントを取得
- ローカルサーバー `python3 -m http.server 8124` で表示確認
- Browser で表示確認し、broken image は 0 件

## 6. Reference Design Notes

参考になる点:

- トップヒーローで街の俯瞰写真を大きく使っている
- 不動産会社の「実物件」だけではなく、街・暮らし・地域感を主役にしている
- 物件カードで価格・種別・住所がすぐ読める
- 売却相談バナーが大きく、購入だけでなく売却導線も目立つ
- 電話番号と営業時間がヘッダーで見える
- 「購入までの流れ」「選ばれる理由」「FAQ」など、相談前の不安を消す構成になっている

ゆめハウスに活かすなら、完全コピーではなく以下を抽出する。

- 街中・住宅地・自然・空の画像で空気感を作る
- 物件導線をカード化する
- 売却/購入/賃貸管理の導線を整理する
- ヒーローは「店舗写真だけ」ではなく「地域で暮らすイメージ」を前面に出す

## 7. Copyright and Safety

取得したローカルデータは参考・分析用。デザイン、文章、画像、ロゴ、CSSをそのままゆめハウスサイトへ流用しない。最終実装では、構成や考え方だけを抽出し、画像・文言・配色・余白・コンポーネントはゆめハウス独自に作る。

## 8. Verification

確認済み:

- `curl -I -L https://www.jyuutakujyouhoukan.com/` returned HTTP 200
- `wget` でページ取得
- `du -sh reference-sites/jyuutakujyouhoukan-2026-05-21` returned 37MB
- Browser 表示確認
- `document.images` ベースで broken image 0 件
- ローカル表示タイトル: `協和住建 縁むすび`

## 9. Next Steps

1. 参考サイトの構成を、ゆめハウス向けに「真似してよい構造」と「真似しない表現」に分ける。
2. ゆめハウスのトップを、店舗写真中心から「熊本の暮らし・街並み・相談しやすさ」中心に再設計する。
3. 外部素材/AI生成で使う画像カテゴリを決める。
4. 現在の抽象背景やAIっぽい素材を、暮らし・街・住宅地系の画像へ置き換える。

## 10. Full Mirror Follow-up

追加依頼を受けて、公開ページを広くクロールするフル版を別フォルダに作成した。

取得先:

```text
reference-sites/jyuutakujyouhoukan-full-2026-05-21/
```

ローカル表示URL:

```text
http://127.0.0.1:8125/www.jyuutakujyouhoukan.com/index.html
```

実行した主コマンド:

```bash
wget --mirror --page-requisites --convert-links --adjust-extension --span-hosts \
  --domains=www.jyuutakujyouhoukan.com,jyuutakujyouhoukan.com,fonts.googleapis.com,fonts.gstatic.com,cdnjs.cloudflare.com,cdn.datatables.net \
  --reject-regex='(/wp-admin/|/wp-json/|xmlrpc\.php|\?replytocom=|/feed/?|/comments/feed|/trackback)' \
  --timeout=20 --tries=2 --wait=0.2 \
  --directory-prefix=reference-sites/jyuutakujyouhoukan-full-2026-05-21 \
  https://www.jyuutakujyouhoukan.com/
```

取得結果:

- `Downloaded: 418 files, 60M`
- 作業後のファイル数: 416 files
- HTML系ファイル数: 220 files
- `topics/page/1` から `topics/page/63` 相当まで取得
- 主要ページ: `search`, `list`, `point`, `reason`, `flow`, `faq`, `company`, `staff`, `contact`, `sales`, `topics`, `privacypolicy`
- 物件/分譲地系: `sales/index.html`, `sales/sales-1085`, `sales/sales-1210.html`

`wget` の終了コードは `8`。これは一部外部リソースや取得対象外URLが混ざる場合に出るが、HTMLのリンク変換自体は `Converted links in 226 files` まで完了している。

追加のパス補正:

- `wget --convert-links` は通常の `href/src` をローカル相対パスに変換した。
- ただし、SEO用 `og:url`、JSON-LD、Contact Form 7 のJS設定などの文字列には元ドメインが残った。
- ローカル参照で混乱しないよう、同一ドメインの絶対URLを `/www.jyuutakujyouhoukan.com/...` に一括補正した。
- 補正後、`rg` で `https://www.jyuutakujyouhoukan.com/` と `http://www.jyuutakujyouhoukan.com/` の残存がないことを確認した。

意図的に残した外部要素:

- AtHome等の外部物件リンク
- `kyowa-jyuken.jp` など別ドメインへのリンク
- Google Analytics / Google Tag Manager / Google Ads 系スクリプト

これらは同一サイト配下のフォルダではなく外部サービスなので、ローカルミラーの対象外とした。

## 11. Full Mirror Verification

ローカルサーバー:

```bash
cd reference-sites/jyuutakujyouhoukan-full-2026-05-21
python3 -m http.server 8125
```

ブラウザ確認結果:

- トップ: title `協和住建 縁むすび`, images 49, broken image 0
- `search/index.html`: broken image 0
- `list/index.html`: broken image 0
- `reason/index.html`: images 11, broken image 0
- `company/index.html`: images 3, broken image 0
- `sales/index.html`: images 4, broken image 0
- `topics/index.html`: broken image 0
- `topics/page/63/index.html`: images 2, broken image 0
- 同一ドメインの外部 `a[href]` はブラウザ上で 0 件
- HTTPサーバーログ上も、確認対象のCSS/JS/画像/フォントは 200 で返っている

検証用スクリーンショット:

```text
reference-sites/jyuutakujyouhoukan-full-2026-05-21/_verification/home.png
```

残る注意点:

- フォーム送信、WordPress REST API、Analytics、外部物件リンクは本物の外部サービスに依存するため、ローカル静的ミラーでは完全再現しない。
- このミラーは参考・分析用であり、文章・画像・ロゴ・CSSをゆめハウス本番へそのまま流用しない。
