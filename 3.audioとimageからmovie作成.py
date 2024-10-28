from pydub import AudioSegment
from moviepy.editor import *
import os

def main(root_folder):

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

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # VBAからの呼び出しの場合
        data = sys.argv[1]
        main(data)
    else:
        # コマンドラインからの呼び出しの場合
        data_input = r"C:\Users\User\Desktop\新しいフォルダー\701-800"
        main(data_input)