# ユーザーは2つの数字、最小数（n）と最大数（m）を入力
# 最小値が最大値以下であることを確認する
# プログラムが n から m の範囲内で乱数を生成
# ユーザーは乱数を正しく推測するまで、ゲームループの中で繰り返し数字を入力
# ユーザーが数字を推測するための試行回数を制限する

import sys

def main():
    try:
        print(
"""\
このゲームは数当てゲームです。
ルールは以下のとおりです。
1. 最小値を入力する。
2. 最大値を入力する。ただし最大値は最小値以上の数値を入力してください。
3. コンピュータ内部で最小値から最大値までの値をランダムで選択するので、正解と思われる数値を入力してください。
4. 間違えた場合、ヒントが表示されます。
   答えより大きい場合: your number is greater than the answer
   答えより小さい場合: your number is smaller than the answer
5. 回答のチャンスは5回でそれまでに数を当てられるよう頑張ってください。
"""
        )

        while True:
            playStart = input("ゲームをプレイしますか？y = yes、n = noをタイプしてください。")
            #  入力値がy, yes, n, noのみ許可
            if playStart in ["y", "yes", "n", "no"]:
                break
            else:
                print("入力値が間違えています。y, yes, n, noいづれかをタイプしてください。")
        
        if playStart in ["n", "no"]:
            raise EOFError()
        
            
    except KeyboardInterrupt:
        print("\n\nゲームを中断しました。")
    except EOFError:
        print("\nゲームを終了します。")
    finally:
        print("ありがとうございました！")

if __name__ == "__main__":
    main()