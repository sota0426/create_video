from pydub import AudioSegment
from moviepy.editor import *
import os
root_folder =r"D:\2.ターゲット（完全版）\501-600"

audio_root_folder = os.path.join(root_folder, "audio")
image_root_folder = os.path.join(root_folder, "スライド")
movie_folder_all = os.path.join(root_folder, "movie_all")
os.makedirs(movie_folder_all, exist_ok=True)
movie_folder_short = os.path.join(root_folder, "movie_short")
os.makedirs(movie_folder_short, exist_ok=True)


def create_video(audio_path, image_path, output_path,interval_time):
    audio = AudioSegment.from_file(audio_path, 'mp3')
    video = ImageClip(image_path).set_duration(audio.duration_seconds)
    extended_duration = video.duration + interval_time  # 動画の長さを1 秒延長

    # N 秒の追加時間を含むように画像をループする
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



merged_videos = []

def process_files(sub_folder,movie_folder):
    audio_folder = os.path.join(audio_root_folder, sub_folder)
    image_folder = os.path.join(image_root_folder, sub_folder)
    os.makedirs(movie_folder, exist_ok=True)   

    for i in range(1,101):  # 番号の範囲を適切に変更してください
        print(f"Processing files for number {i} in folder {sub_folder}...")  # メッセージを追加

        audio_path = os.path.join(audio_folder, f"{i}.mp3")
        image_path = os.path.join(image_folder, f"{i}.PNG")
        movie_path = os.path.join(movie_folder, f"{str(i*10 + int(sub_folder))}.mp4")

        # 出力先のファイルが既に存在するかどうかをチェック
        if not os.path.exists(movie_path):
            create_video(audio_path, image_path, movie_path,interval_time)
        else:
            print(f"Skipping number {i} in folder {sub_folder} as it's already processed.")



text_count = 3
interval_time =1

 # 各サブフォルダのファイルを処理
for sub_folder in os.listdir(audio_root_folder):
    if sub_folder.isdigit():
        # sub_folderが数値の場合の処理
        sub_folder_int = int(sub_folder)
        print("サブフォルダは数値です。整数値:", sub_folder_int)
        if(text_count * 2 >= int(sub_folder)):
            process_files(sub_folder,movie_folder_all)

text_count =1
interval_time =0.3

 # 各サブフォルダのファイルを処理
for sub_folder in os.listdir(audio_root_folder):
    if sub_folder.isdigit():
        # sub_folderが数値の場合の処理
        sub_folder_int = int(sub_folder)
        print("サブフォルダは数値です。整数値:", sub_folder_int)
        if(text_count * 2 >= int(sub_folder)):
            process_files(sub_folder,movie_folder_short)
