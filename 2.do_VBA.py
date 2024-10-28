import win32com.client
import sys

def main(root_file_path):
    file_path=r"D:\googleDrive\動画作成用いろいろ\pythonコード集\create_video\スライド作成マクロ.xlsm"
    macro_name = "Sheet1.create_slide"
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True  # Excelを非表示にする場合はFalseに変更します
    workbook = excel.Workbooks.Open(file_path)
    excel.Run(macro_name,root_file_path)
    workbook.Close(SaveChanges=False)
    excel.Quit()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # VBAからの呼び出しの場合
        data = sys.argv[1]
        main(data)
    else:
        # コマンドラインからの呼び出しの場合
        data_input = r"D:\googleDrive\2.ターゲット（完全版）\1101-1200"
        main(data_input)