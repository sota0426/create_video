from PIL import Image
import os

def convert_png_to_webp(input_path, output_path):
    """
    PNGファイルをWebPに変換する関数
    :param input_path: 入力PNGファイルのパス
    :param output_path: 出力WebPファイルのパス
    """
    with Image.open(input_path) as img:
        img.save(output_path, 'webp')

def batch_convert_png_to_webp(input_dir, output_dir):
    """
    指定されたディレクトリ内のすべてのPNGファイルをWebPに変換する関数
    ファイル名は変更せず、拡張子のみをwebpに変更します
    :param input_dir: 入力PNGファイルのディレクトリ
    :param output_dir: 出力WebPファイルのディレクトリ
    """
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 入力ディレクトリ内のすべてのPNGファイルを処理
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_dir, filename)
            # ファイル名は同じで、拡張子のみwebpに変更
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_dir, output_filename)
            convert_png_to_webp(input_path, output_path)
            print(f'Converted {filename} to {output_filename}')

# 使用例

input_directory = r"C:\Users\User\Desktop\english\picture_png"
output_directory = r"C:\Users\User\Desktop\english\picture_webp"
batch_convert_png_to_webp(input_directory, output_directory)