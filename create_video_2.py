from pydub import AudioSegment
from moviepy.editor import *
import os

audio_root_folder = r"C:\Users\User\Desktop\audio"
image_root_folder = r"C:\Users\User\Desktop\image"
output_root_folder = r"C:\Users\User\Desktop\output_videos"


def create_video(audio_path, image_path, output_path):
    audio = AudioSegment.from_file(audio_path, 'mp3')
    video = ImageClip(image_path).set_duration(audio.duration_seconds)
    extended_duration = video.duration + 1  # 動画の長さを0.5秒延長

    # 0.5秒の追加時間を含むように画像をループする
    looped_image = ImageClip(image_path).set_duration(extended_duration).fx(vfx.loop, duration=extended_duration)

    # 音声とループされた静止画を結合して新しい動画を作成
    final_video = looped_image.set_audio(audio)

    # 動画を書き出し
    final_video.write_videofile(output_path, codec="libx264", fps=10, audio=audio_path)


def merge_videos(video_paths, output_path):
    video_clips = [VideoFileClip(path) for path in video_paths]
    final_clip = concatenate_videoclips(video_clips)
    final_clip.write_videofile(output_path, codec="libx264", fps=video_clips[0].fps)


def merge_all_videos_in_folder(folder_path, output_path):
    video_files = [file for file in os.listdir(folder_path) if file.endswith(".mp4")]
    video_clips = [VideoFileClip(os.path.join(folder_path, file)) for file in video_files]
    final_clip = concatenate_videoclips(video_clips)
    final_clip.write_videofile(output_path, codec="libx264", fps=video_clips[0].fps)



marge_folder = os.path.join(output_root_folder, "marge")

# 出力先のルートフォルダを作成
os.makedirs(output_root_folder, exist_ok=True)
os.makedirs(marge_folder, exist_ok=True)

merged_videos = []

def process_files(sub_folder):
    audio_folder = os.path.join(audio_root_folder, sub_folder)
    image_folder = os.path.join(image_root_folder, sub_folder)
    output_folder = os.path.join(output_root_folder, sub_folder)

    # 出力先のサブフォルダを作成
    os.makedirs(output_folder, exist_ok=True)

    # フォルダから番号ごとに対応する音声ファイルと画像ファイルを取得して処理する
    for i in range(1, 100):  # 番号の範囲を適切に変更してください
        print(f"Processing files for number {i} in folder {sub_folder}...")  # メッセージを追加

        audio_path = os.path.join(audio_folder, f"{i}_単語.mp3")
        image_path = os.path.join(image_folder, f"スライド{i}.PNG")
        output_path = os.path.join(output_folder, f"{i}.mp4")

        # 最後に[1]フォルダ内の「番号.mp4」と[2]フォルダ内の「番号.mp4」を結合して、「marge」フォルダ内に「番号_marge.mp4」を出力
        if sub_folder == "1":
            merged_videos.append(output_path)
        elif sub_folder == "2":
            video_1 = merged_videos.pop(0)  # [1]フォルダ内の動画を取り出す
            video_2 = output_path
            merged_video_path = os.path.join(marge_folder, f"{i}_marge.mp4")
            merge_videos([video_1, video_2], merged_video_path)

# 各サブフォルダのファイルを処理
for sub_folder in os.listdir(audio_root_folder):
    process_files(sub_folder)

# 最後に「marge」フォルダ内の動画を結合して、「output_root_folder」内に「complete_marge.mp4」を出力
merge_all_videos_in_folder(marge_folder, os.path.join(output_root_folder, "complete_marge.mp4"))
