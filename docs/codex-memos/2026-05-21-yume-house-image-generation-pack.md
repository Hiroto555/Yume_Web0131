# ゆめハウス AI画像生成パック メモ

## 1. 目的

ゆめハウスのサイトを不動産会社らしく見せるため、生成AI感の薄い写真調素材を用途別に用意する。

今回の画像方針は、お手本サイトの構造に合わせて「画像の役割」を分けること。

## 2. 生成する画像カテゴリ

1. トップヒーロー候補
   - 熊本・地方都市・住宅地・川・青空
   - 文字を置ける余白がある
   - 物件単体ではなく地域感を出す

2. スマホヒーロー候補
   - 同じ世界観で縦構図
   - 上に空、下に街や住宅地

3. 横長CTAバナー候補
   - 売却相談、物件検索、住宅ローン相談に使える背景
   - 文字なし、ロゴなし
   - 薄めの情報量でテキストを載せやすい

4. 物件カード候補
   - 普通の日本の戸建て
   - 空き地
   - 住宅街の道路
   - マンション・アパート外観
   - 不自然に高級にしない

5. 相談・信頼感候補
   - 図面、鍵、ノートPC、電卓、住宅資料
   - 人物は小さめ、横顔、後ろ姿中心
   - 手や顔の破綻を避ける

## 3. 共通禁止条件

- 画像内テキスト
- 看板、ロゴ、会社名、透かし
- 読めそうで読めない漢字や英字
- 豪邸、海外住宅、アメリカ郊外
- 映画風の夕焼け、夜景、過剰なボケ
- CGI感、過度にツルツルした質感
- 不自然な窓、道路、屋根、手、顔

## 4. 採用基準

- 実在の不動産会社サイトに自然に入る
- 画像単体で主張しすぎない
- 文字やCTAを重ねても邪魔にならない
- 普通の住宅購入・売却相談の文脈に合う
- AI生成とすぐ分かる違和感が少ない

## 5. 次の作業

生成後に候補を見て、採用画像を選ぶ。
採用後は `astra-child_0204/assets/site/estate-images/` 配下に用途別ファイル名で保存し、各HTML/CSSから参照する。

## 6. 今回生成・整理した画像

生成画像は、元ファイルを残したままプロジェクト配下へコピーし、用途別に切り出した。

保存先:

- 候補シート: `astra-child_0204/assets/site/estate-images/generated-20260521/source-sheets/`
- 切り出し候補: `astra-child_0204/assets/site/estate-images/generated-20260521/hero/`
- 切り出し候補: `astra-child_0204/assets/site/estate-images/generated-20260521/banner/`
- 切り出し候補: `astra-child_0204/assets/site/estate-images/generated-20260521/property/`
- 切り出し候補: `astra-child_0204/assets/site/estate-images/generated-20260521/trust/`
- すぐ使える選抜セット: `astra-child_0204/assets/site/estate-images/generated-20260521/selected/`

選抜セット:

- `selected/hero-desktop.jpg` - PCヒーロー用、`2800x1040`
- `selected/hero-mobile.jpg` - スマホヒーロー用、`1280x1300`
- `selected/banner-sale-consultation.jpg` - 売却相談バナー
- `selected/banner-property-search.jpg` - 物件検索バナー
- `selected/banner-land-sale.jpg` - 土地・売却系バナー
- `selected/banner-loan-consultation.jpg` - ローン相談バナー
- `selected/consultation-office.jpg` - 相談シーン
- `selected/consultation-desk-close.jpg` - 相談机の寄り
- `selected/keys-and-floorplan.jpg` - 鍵・図面
- `selected/property-used-house.jpg` - 中古戸建て
- `selected/property-vacant-land.jpg` - 空き地
- `selected/property-narrow-street.jpg` - 住宅街道路
- `selected/property-parking.jpg` - 駐車場
- `selected/property-apartment.jpg` - アパート外観
- `selected/property-older-house.jpg` - 古めの戸建て

## 7. 確認

実施した確認:

- 生成画像をローカルへコピー
- 候補シートから個別画像へ切り出し
- PCヒーローを `2800x1040` に整形
- スマホヒーローを `1280x1300` に整形
- `sips` で主要ファイルのピクセルサイズを確認
- プレビューシート `/tmp/yume-selected-assets-preview.jpg` を作成して見た目を確認

現時点の判断:

- PCヒーローとスマホヒーローは、お手本に近い「地域景観＋青空＋余白」の方向に寄せられている。
- 物件画像は、あえて少し実務寄りで古い住宅や空き地も混ぜた。きれいすぎるAI画像より、不動産サイトの実在感が出やすい。
- 相談画像はやや整いすぎているものもあるため、最終反映時には顔が目立ちすぎないものを優先する。
