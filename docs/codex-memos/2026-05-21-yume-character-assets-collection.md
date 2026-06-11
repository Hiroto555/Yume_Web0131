# ゆめハウス新キャラクター素材 集約メモ

## 目的

Desktop上に散らばっていた、ゆめハウスの新キャラクター関連素材を `Astra本番0205` 側にまとめる。

ユーザーは `Astra本番2025` と表現したが、実在確認では `Astra本番2025` は見つからず、既存の本番作業フォルダは次だった。

```text
/Users/shiroto/Desktop/Blooo/Stitch_Web/Astra本番0205
```

そのため、この既存フォルダに集約した。

## コピー先

```text
/Users/shiroto/Desktop/Blooo/Stitch_Web/Astra本番0205/related-assets/yume-house-character-assets
```

## コピーしたもの

```text
/Users/shiroto/Desktop/Download/看板デザイン入稿/ゆめハウスキャラクター
/Users/shiroto/Desktop/Download/看板デザイン入稿/デザイン共有素材
/Users/shiroto/Desktop/Download/看板デザイン入稿/ぬいぐるみ質感なし
/Users/shiroto/Desktop/Download/看板デザイン入稿/ゆめハウス　ロゴ
/Users/shiroto/Desktop/Download/看板デザイン入稿/ゆめハウス看板デザイン既存
/Users/shiroto/Desktop/Blooo/写真一時保存3:9/青い子犬のマスコット.png
```

`青い子犬のマスコット.png` はフォルダではなく単体ファイルだったため、コピー先では次に入れた。

```text
related-assets/yume-house-character-assets/standalone-candidates/青い子犬のマスコット.png
```

また、`看板デザイン入稿` 直下にあったQR、提案画像、アイコン、要件メモなどの単体ファイルは次にまとめた。

```text
related-assets/yume-house-character-assets/root-files/
```

## 代表ファイル

```text
related-assets/yume-house-character-assets/ゆめハウスキャラクター/ゆめハウスキャラクター（基本）.png
related-assets/yume-house-character-assets/ゆめハウスキャラクター/青い子犬と黄金の鍵.png
related-assets/yume-house-character-assets/ゆめハウスキャラクター/青い子犬とライン.png
related-assets/yume-house-character-assets/デザイン共有素材/キャラクター1.png
related-assets/yume-house-character-assets/ぬいぐるみ質感なし/ゆめハウスキャラクター1.png
```

## 検証

実行後、コピー先のサイズは約 `41M`。

`find` で主要ファイルがコピー先に存在することを確認した。最大深度2のファイル数は `53`。

## 注意

元フォルダは削除・移動していない。壊さないためにコピーで集約した。

`git status` には今回作業前から存在していた可能性が高い削除・未追跡項目も見えているため、それらには触れていない。
