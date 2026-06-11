# ゆめハウス HTML to WordPress 方針メモ

## 1. This Report's Purpose

このメモは、ゆめハウスサイトをローカルで起動確認し、HTMLで見た目を仕上げてからWordPress向けに載せる方針が妥当かを記録するためのもの。

## 2. User Request

ユーザーは、参考サイトを見た後に「ゆめハウスもここに起動して！htmlで仕上げてwordpressようにすればいいですよね？」と確認した。

## 3. Context

作業フォルダは `/Users/shiroto/Desktop/Blooo/Stitch_Web/Astra本番0205`。現在のゆめハウス静的HTMLは `astra-child_0204/assets/site` にあり、既存のWordPress/Astra child theme は静的HTMLをWordPress上で配信する構造を持っている。

## 4. Local Preview

起動済みサーバー:

```text
http://127.0.0.1:8123/
```

トップURL:

```text
http://127.0.0.1:8123/1._home/code.html
```

確認したトップタイトル:

```text
ゆめハウス - 夢をかなえる、理想の住まい。
```

## 5. Decision

HTMLで先に見た目・導線・素材・レスポンシブを仕上げる方針は妥当。ただし、最終的にWordPressへ載せる前提なら、単なる静的HTMLの巨大ファイルとして完成させるのではなく、後で以下へ分解しやすい構造にしておくべき。

- header
- footer
- page template
- reusable sections
- property cards
- CTA blocks
- FAQ blocks
- contact form
- WordPress-managed content fields

## 6. Implementation Guidance

短期:

- HTMLプレビューでファーストビュー、写真、物件カード、CTA、余白、文言を完成させる。
- 参考サイトのような「地域写真」「物件」「選び方」「購入の流れ」「FAQ」「会社/スタッフ」「問い合わせ」の構成をゆめハウス向けに再設計する。

中期:

- 仕上がったHTMLをWordPressテンプレートやパーツへ分解する。
- 物件情報やFAQなど更新したい部分をWordPress側で管理できるようにする。

避けること:

- 重要コピーを画像化しすぎること
- HTMLをそのまま1枚でWordPressに流し続けること
- 画像パスや外部素材がバラバラなままWordPress化すること
- 物件/FAQ/CTAを更新しづらい静的記述だけにすること

## 7. Verification

実行・確認:

- `lsof -nP -iTCP:8123 -sTCP:LISTEN` でサーバー稼働を確認
- `astra-child_0204/assets/site/1._home/code.html` の存在を確認
- in-app browser で `http://127.0.0.1:8123/1._home/code.html` を表示
- 画像の一部が lazy load 未読込として検出されたが、該当ファイルは `curl -I` で 200 を確認した

## 8. Next Steps

1. まずHTML版トップを参考サイトレベルの視覚品質まで上げる。
2. 写真カテゴリを整理する。
3. 物件カードに月々支払い、校区、駐車台数、見学可否を入れる。
4. 買う、売る、ローン相談、賃貸管理の導線を分ける。
5. 完成HTMLをWordPress向けテンプレート/パーツへ分解する。
