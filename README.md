# Gaussian-Splatting-Colab
3D Gaussian Splatting を Google Colab 上で実行する

## VSCode で Colab を使う場合の準備
1. VSCode に Colab のアドオンを入れる
1. カーネルを選択する際に、Colab を選ぶ
  ![](https://github.com/user-attachments/assets/424b9441-41e7-4823-b727-78a70296d622)
1. 適当に進めて GPU を選択する
  ![](https://github.com/user-attachments/assets/7827c540-f582-453d-a708-7f78171f2281)
1. Colab への接続が確認できます
  ![](https://github.com/user-attachments/assets/c825ed82-b117-40ef-87d9-d839deaf24b6)


## 写真データの準備
- あらかじめ、同じ物体をさまざまな異なる角度から撮影した写真データを準備しておく

## 3DGSのモデル作成
- `colab_3DGS.ipynb` の内容を実施する
1. Colab のセッションを Google Drive へマウントする
    - この手続きは、セッションを起動するたびに実施しする必要がある（Colab を一度切断したら、再度実施する必要がある）
  ![](https://github.com/user-attachments/assets/ede0e6de-538f-4765-ab26-a8bed8ae845e)
    - Google Drive とのリンクに関する警告・ログイン画面が出た場合は、適当に対応する
    - このセルを実行すると、左側赤枠のように、`drive`と`3DGS`の2つのディレクトリが出現する
1. Gaussian Splatting の本家リポジトリを Clone する
    - この手続きは、一度実行したら以降は実施不要（マウントした Google Drive 上に保存されるため）
  ![](https://github.com/user-attachments/assets/923c9cb8-79b3-4915-a910-53d91d1153ef)
    - https://github.com/graphdeco-inria/gaussian-splatting
    - Clone が完了すると、左側赤枠のように`gaussian-splatting`のディレクトリができる
1. 必要な PIP パッケージをインストールする
  ![](https://github.com/user-attachments/assets/20bea557-4ed8-4ba7-9ad4-9f8d3b05076f)
1. 準備した画像ファイルを Google Drive の `適当なフォルダ名/input/`以下に保存し、リンクを通す
  ![](https://github.com/user-attachments/assets/7c537bad-471b-4804-8618-b7741861d766)
1. COLMAP により、Structure from Motion （特徴点の抽出・マッチングと特徴点・カメラ位置の推定）で3次元復元する
  ![](https://github.com/user-attachments/assets/eaa9a9de-64eb-4642-b77c-3a32cad24b0d)
1. 学習により、 3D Gaussian の値を更新する
  ![](https://github.com/user-attachments/assets/431035f1-9bf4-4624-ab64-32ecd5ce6ea3)
    - 無事完了すると、`output/<ランダムなID>/point_cloud/iteration_iter数/point_cloud.ply`に 3DGS モデルが出力される


## モデルの表示

### Web サービスを使う
- 例：https://superspl.at/editor
    - ![](https://github.com/user-attachments/assets/1b0ceddd-c9f4-4f11-85d9-3133db6cbbcc)
    - `ply`ファイルをアップロードすることでモデルを確認できる

### Blender + アドオン (3DGS Render by KIRI Engine) を使う
1. 以下のリンク -> Releases から適当なバージョンのアドオンの `.zip` をダウンロードする
    - https://github.com/Kiri-Innovation/3dgs-render-blender-addon
1. ダウンロードした zip ファイルを Blender にドラッグアンドドロップし、アドオンをインストールする
1. 念のため、アドオンインストール後は Blender を再起動する
1. 3D Viewport の右側の小さな `<` みたいなのを左にドラッグし、 `3DGS Render` のタブを押す
  ![](https://github.com/user-attachments/assets/9e268eb6-305e-4968-956d-8496510c7209)
1. `Create Proxy Object` にチェックを入れる
  ![](https://github.com/user-attachments/assets/cf877602-7c2d-488c-9d14-9ba499150846)
1. `Import PLY` を押し、`ply` ファイルを選択する
  ![](https://github.com/user-attachments/assets/5278af52-809b-44f5-9807-e7407441b776)
1. 図のように 3D Gaussians が配置される
  ![](https://github.com/user-attachments/assets/213a1929-233c-4f24-a1fd-5ec37d0ddd53)
1. `Active Mode` を Render にすると、以下のようにモデルが描画される
  ![](https://github.com/user-attachments/assets/a8be5960-6632-43b1-8484-5d88ef1f79a1)
  ![](https://github.com/user-attachments/assets/c9c3d491-8efb-4cd1-8786-84db7c7c8f29)
