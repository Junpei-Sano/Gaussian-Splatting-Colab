import cv2
import os
import sys

# 動画からフレームを抽出して保存する関数
# 第1引数: 動画ファイルのパス
# 第2引数: フレームを抽出する間隔（秒）

def extract_frames(video_path, output_dir, step_seconds=0.5):
    # 出力フォルダ作成
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("動画を開けませんでした")
        return

    # FPS と総フレーム数を取得
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 指定された秒数ごとのフレーム間隔（フレーム数）
    step = int(fps * step_seconds)

    frame_index = 0
    saved_index = 0

    while frame_index < frame_count:
        # 読み込み位置を指定
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        if not ret:
            break

        # ファイル名を決めて保存
        filename = os.path.join(output_dir, f"frame_{saved_index:05d}.jpg")
        cv2.imwrite(filename, frame)

        saved_index += 1
        frame_index += step

    cap.release()
    print("完了しました")


if __name__ == "__main__":

    output_base_dir = "output/"

    if len(sys.argv) < 3:
        print("引数が足りません")
        exit()

    input_fname = sys.argv[1]
    step_seconds = float(sys.argv[2])
    output_dir = os.path.splitext(os.path.basename(input_fname))[0]  # 入力ファイル名から拡張子を除いたものを出力フォルダ名にする

    video_path = input_fname          # ここに動画ファイル名
    output_dir = os.path.join(output_base_dir, output_dir, "input")    # 出力フォルダ名
    extract_frames(video_path, output_dir, step_seconds=step_seconds)
