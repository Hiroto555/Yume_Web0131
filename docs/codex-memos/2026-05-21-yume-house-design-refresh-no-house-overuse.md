# ゆめハウス 住宅写真入れすぎ修正・デザイン刷新メモ

## 1. 目的

このメモは、ユーザーの「どこでもかんでも家とか入れすぎておかしい」「全体的にデザインとかを刷新していい」という指摘を受けて、画像の使い方とトップページ構成を整理した作業記録です。

## 2. 問題

直前の状態では、生成画像を入れることを優先したため、サービスカード、強み、相談事例などにも住宅・住宅街・土地の写真が多く入りすぎていた。

その結果、以下の違和感があった。

- 物件写真と説明用写真の区別が弱い
- 家の写真が多すぎて、全体が単調に見える
- 不動産会社サイトというより、生成素材を並べた印象になる
- お手本サイトのような「地域感、相談感、物件実在感」の役割分担が弱くなる

## 3. 方針

住宅・土地・建物写真は、基本的に「物件として比較する枠」へ寄せる。

それ以外のセクションは、写真に頼らず、テキストカード・余白・導線で整理する。

画像の役割:

- ヒーロー: 地域景観
- トップ直下CTA: 売却、検索、ローンの導線
- おすすめ物件: 家・マンション・土地の写真
- サービス/強み/相談事例: 原則テキストカード
- CTA: 相談風景

## 4. 実装内容

変更ファイル:

- `tools/rebuild_yume_estate_site.py`
- `astra-child_0204/assets/site/shared/base.css`
- 生成後の `astra-child_0204/assets/site/*/code.html`

主な変更:

- `VERSION` を `20260521-design-refresh1` に更新
- `search_banner` を住宅街画像から地域・川沿い背景へ変更
- `section()` に任意の `kicker` を追加し、汎用の `Section` 表示をやめた
- `card()` に画像なしカード用の `estate-card--text` クラスを追加
- サービス、強み、相談事例、チェックポイント、購入前の整理、賃貸管理のカードから住宅写真を削除
- 物件写真は `おすすめ物件` と物件詳細系に限定
- CSSに `.estate-card--text` と `.estate-kicker--section` を追加

## 5. Before / After

Before:

- トップ下部の多くのカードに家・土地・住宅街の画像が入っていた
- 同じような写真が続き、用途の違いが見えにくかった

After:

- 家・マンション・土地写真は `おすすめ物件` に集中
- サービス/強み/相談事例は文字中心のカードに変更
- トップ直下の検索バナーは地域背景に変更
- 「家だらけ」の印象を抑え、相談導線と物件導線を分離

## 6. Verification

実行:

```bash
python3 tools/rebuild_yume_estate_site.py
python3 -m py_compile tools/rebuild_yume_estate_site.py
```

結果:

- 全11ページ再生成成功
- Python構文チェック成功
- HTML画像/リンク参照チェック: missing `0`

ブラウザ確認:

- URL: `http://127.0.0.1:8123/1._home/code.html?v=20260521-design-refresh1`
- PC幅 `1280px`: ヒーローは `hero-desktop.jpg`
- スマホ幅 `390px`: ヒーローは `hero-mobile.jpg`
- トップページ内の画像カード: `3`
- トップページ内のテキストカード: `9`
- スマホ横スクロールなし: `scrollWidth = clientWidth = 390`

確認スクリーンショット:

- `/tmp/yume-design-refresh1/home-top-1280.png`
- `/tmp/yume-design-refresh1/home-mid-1280.png`
- `/tmp/yume-design-refresh1/home-lower-1280.png`
- `/tmp/yume-design-refresh1/home-mobile-top.png`

## 7. 次の改善案

次に見るべき点:

- ヒーローの文字量と黒帯の幅をもう少し上品にする
- トップ直下CTAの余白と高さをさらにお手本寄りに調整する
- 物件写真は最終的に実物件写真へ置き換える
- 会社情報・相談ページは、後で実店舗/スタッフ写真に差し替える
