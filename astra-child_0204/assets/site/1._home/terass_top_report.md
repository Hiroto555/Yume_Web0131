# TERASS（terass.com）トップページ 構成・デザイン詳細レポート

対象ページ: `https://terass.com/`  
取得日: 2026-02-01（Chrome DevTools MCPで計測）  
計測Viewport:
- Desktop: `1440×900`（DPR=2）
- Mobile相当: `500×760`（DPR=2）

> 注: Newsなどのコンテンツは更新されるため、件名/日付/カード数などは取得日時点のスナップショットです。  
> 注: ここに記載の数値は「computed style / 実測（bounding box）」由来です。

---

## 1. 全体構成（Information Architecture）

ページは `header → main → footer` の3レイヤーで明確に分割され、`main` は縦積み（`display:flex; flex-direction:column`）でセクションが並びます。

### Main内の順序（Desktop）
1. **KV / ヒーロー**: `section#kv`（高さ 約`603px`）
2. **2カラム導線**（住宅購入/売却・仲介経験者）: `SectionHomeBuying`（高さ 約`256px`）
3. **News**: `section#news`（高さ 約`674px`）
4. **Service**: `section#service`（高さ 約`690px`、色面の帯）
5. **Recruit**: `section#recruit`（高さ 約`1181px`）

### Main内の順序（Mobile相当）
1. `#kv`（高さ 約`889px`）
2. HomeBuying（高さ 約`496px`）
3. `#news`（高さ 約`731px`）
4. Service（高さ 約`823px`）
5. Recruit（高さ 約`2064px`）

---

## 2. ビジュアルトーン（印象設計）

- **全体印象**: 余白多めでクリーン、コーポレート寄り。情報は「見出し→短文→導線ボタン」で整理。
- **写真の選び方**: 高キー（明るい）で白い余白が大きい写真を背景に採用し、テキストが読める構図（HomeBuyingの2枚が象徴的）。
- **コンポーネントの統一**: 主要CTA（丸いボタン）は色・角丸・高さがページ全体でほぼ同一。

---

## 3. カラー設計（実測値）

| 役割 | 色 |
|---|---|
| ベース背景 | `#ffffff` |
| ベース文字 | `#171717` |
| 見出し/本文の濃色 | `#333333` |
| ブランド濃色（見出し/補助） | `#213544` |
| 主要CTA背景 | `#2a3f54` |
| セクション帯/注意喚起の背景 | `#e7ecec` |
| フッター背景（濃色） | `#212121` |
| フッターナビ背景 | `#acb4b9` |
| バッジ枠線（Newsカテゴリ） | `#596873`（1px solid相当） |

---

## 4. タイポグラフィ（実測値）

### ベース
- Body font: `MFW-PA1GothicStdN-Regular, sans-serif`
- Body size: `16px`
- Body color: `#171717`

### セクション大見出し（例: News / Service / Recruit）
- Font: `Roboto`
- Size: `36px`
- Weight: `400`
- Line-height: `36px`
- Color:
  - News: `#333333`
  - Service / Recruit: `#213544`

### 和文の中見出し（例: HomeBuying H3）
- Font: `"Noto Sans JP"`
- Size: `22px`
- Weight: `700`
- Letter-spacing: `0.48px`
- Color: `#1a202c`

### Newsカードのタイトル（H3）
- Font: `"Noto Sans JP"`
- Size: `15px`
- Weight: `500`
- Line-height: `22.5px`
- Color: `#333333`

---

## 5. レイアウトシステム（グリッド/コンテナ）

### コンテナ幅（Desktopの基準）
- 多くのセクションで **`max-width:1200px`** の中央寄せコンテナを採用
  - 左右マージンが結果的に `120px`（`1440 - 1200 = 240` の半分）
  - コンテナ内の左右 `padding:20px` が多く、実効幅が `1160px` になりがち

### HomeBuyingの例外（2枚カードをピッタリ配置）
- 外側は左右 `12px` の余白で幅 `1416px`
- `702px`カード×2 + `gap 12px` で横並びを成立させる

---

## 6. ヘッダー（Header）

### 位置/挙動
- `position:absolute`（固定ヘッダーではない）
- スクロールすると上へ流れる（追従/固定しない）
- Desktop 高さ 約`74px`（padding: `20px 24px 16px 24px`）
- Mobile 高さ 約`61px`

### ナビゲーション（Desktop）
- 左: ロゴ（`/images/logo.svg`）表示サイズ 約`129×26`
- 右: 5項目（2段表記）
  - About / Service / News / Recruit / Contact
  - 英語: `18px` / weight `500`
  - 日本語: `10px` / weight `500`
  - 文字色: `#333333`

### モバイルメニュー（オフキャンバス）
- 右上にハンバーガーボタン（約`24×24`）
- オーバーレイ:
  - `position:fixed`
  - 背景 `#ffffff`
  - `z-index:100`
  - `transition: transform 0.3s ease-in-out`
  - 閉: `transform` がX方向に画面外（`translateX(100%)`相当）
  - 開: `transform` が `x=0`（全面表示）
- 開いたとき: `body` のスクロールが抑制される（`overflow:hidden`系）

---

## 7. KV（#kv）

### サイズ
- Desktop: 高さ 約`603px`
- Mobile相当: 高さ 約`889px`

### 背景画像（レスポンシブ差し替え）
- Desktop: `/images/kv_bg_pc.webp`
- Mobile: `/images/kv_bg_sp.webp`

### コンテンツ
- KV内の主導線は「TERASSについて」のリンク
  - テキストはSVG描画（`aria-label="TERASSについて"`、サイズ `136×22`）
  - 右に矢印アイコン（`small_arrow.svg` / hover用 `small_arrow_hover.svg`）
  - リンクのクリック領域（Desktop実測）約 `187×24`

---

## 8. 2カラム導線（住宅購入/売却・仲介経験者）

### レイアウト
- コンテナ: `display:flex; gap:12px`
- カード: `702×240` が2枚
- どちらも背景画像フルブリード（`background-size:cover; background-position:50% 50%; overflow:hidden`）

### 背景画像
- 左カード: `/images/home_buying_img1.png`
- 右カード: `/images/home_buying_img2.png`

### タイポ/配置
- カード内コンテンツは左上基準で `padding-top:48px; padding-left:48px`
- 見出し（H3）: `22px`/700、色 `#1a202c`
- 説明文: `14px`/500、letter-spacing `0.8px`、色 `#1a202c`

### CTA（主要ボタンの共通仕様）
- 背景: `#2a3f54`
- 文字: `#ffffff`
- 角丸: `28px`
- パディング: `10px 30px`
- 高さ（実測）: `52px`
- フォント: `MFW-PA1GothicStdN-Regular`、`16px`/400
- 例: 「住宅購入売却相談」ボタン サイズ 約 `212×52`

---

## 9. News（#news）

### セクション/コンテナ
- `margin-top:96px`
- コンテナ幅 `1200px` 中央寄せ

### タイトル行
- H2: `News`（`Roboto 36px`、色 `#333333`）
- 右側に「ニュース一覧へ」リンク

### 注意喚起バー（caution bar）
- 幅 `1200px`、高さ 約`124px`
- 背景 `#e7ecec`
- 角丸 `10px`
- パディング `24px 32px`
- 右側にCTA「TERASSお客様ホットライン」（主要ボタン仕様、サイズ 約 `285×52`）

### ニュース一覧（横スクロールのスライダー）
- リスト: `display:flex; gap:48px; overflow-x:auto; padding-bottom:15px`
- カード数（取得時点）: 6
- カード外枠:
  - 背景 `#ffffff`
  - 角丸 `8px`
  - `overflow:hidden`
- 画像領域: `368×207`
- テキスト領域: `padding:15px`
- カテゴリバッジ:
  - 枠: `1px solid #596873`
  - 文字色: `#213544`
  - `font-size:12px; padding:4px 10px`
- 日付: `12px`、色 `#213544`
- 操作ボタン: 「前にスクロール」「次にスクロール」（各 約 `16×18`）

---

## 10. Service（#service）

### 背景/余白
- セクション背景: `#e7ecec`（色面の帯）
- `margin-top:96px`

### コンテナ
- 幅 `1200px` 中央寄せ
- `padding:72px 20px 48px 20px`

### タイトル/導線
- H2: `Service`（`Roboto 36px`、色 `#213544`）
- 右に「事業・サービス一覧」リンク
- 主要CTA: 「お住まいをお探しの方」（主要ボタン仕様、サイズ 約 `244×52`）

---

## 11. Recruit（#recruit）

### 余白/コンテナ
- `margin-top:48px`
- セクション内 `padding:72px 0`
- コンテナ幅 `1200px`（左右 `padding:0 20px`）

### タイトル
- H2: `Recruit`（`Roboto 36px`、色 `#213544`、下 `margin-bottom:24px`）

### 2カラム構成
- カラムラッパー: `display:flex; gap:60px`
- カラム見出し帯: 幅 `502px`、`padding-bottom:12px`
- 見出し: 「本社・ビジネス職」「不動産エージェント」

### カード/記事リスト
- メンバー記事カードは `display:flex` で、左画像（例: 約 `252×142`）+ 右テキスト
- 縦リズムは `padding:32px 0` の反復で作る

### 下部CTA
- 「MEMBER'S STORYをもっと見る」（主要ボタン仕様、サイズ 約 `310×52`）
- 「with TERASSをもっと見る」（主要ボタン仕様）

---

## 12. フッター（Footer / FooterNav）

### 会社情報フッター
- 背景: `#212121`
- 文字色: `#ffffff`
- `padding-top:80px`
- 拠点リンク（地図）: TOKYO / TOKAI / KANSAI / KYUSHU / HOKKAIDO（住所は複数行構成）
- `PAGE TOP` ボタン: 約 `58×48`（背景透明、文字白）
- コピーライト: `Copyright 2025 © All rights reserved by TERASS`

### フッターナビ（カテゴリリンク群）
- `nav` 背景: `#acb4b9`
- `padding:80px 0`
- Desktopは **6カラムgrid**（gap `30px`）
- 表記の階層差:
  - カテゴリ（例: 私たちについて）: `12px`/400（白）
  - サブ（例: 住宅売買仲介）: `12px`/500（白、左 `padding-left:20px`）
  - アイコン付きサブ（例: プレスリリース）: `12px`/400（白）

---

## 13. モーション/インタラクション

- スクロール表示: フェードアップ系（`transition: opacity 0.8s ease-out, transform 0.8s ease-out`）
- Mobileメニュー: `transform` によるスライド（`0.3s ease-in-out`）
- News: 横スクロール（ドラッグ/ホイール/ボタン）前提のカルーセル

---

## 14. 主要UIコンポーネント仕様（再利用用）

### Primary CTA Button（共通）
```css
/* computedから逆算した“見た目の型” */
background: #2a3f54;
color: #fff;
border-radius: 28px;
padding: 10px 30px;
height: 52px; /* 実測 */
font-size: 16px;
font-weight: 400;
```

### News Card（概形）
- 外枠: `background:#fff; border-radius:8px; overflow:hidden;`
- 画像: `368×207`（Desktop実測）
- テキスト領域: `padding:15px`
- バッジ: `font-size:12px; padding:4px 10px; border:1px solid #596873; color:#213544;`

---

## 15. アセット一覧（確認できた範囲）

### KV
- `/images/kv_bg_pc.webp`（Desktop背景）
- `/images/kv_bg_sp.webp`（Mobile背景）
- `/images/icons/small_arrow.svg`
- `/images/icons/small_arrow_hover.svg`

### HomeBuying
- `/images/home_buying_img1.png`
- `/images/home_buying_img2.png`

### News（例）
- `/images/icons/warning.svg`

