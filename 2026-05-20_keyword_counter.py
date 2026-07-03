from pathlib import Path

content = r"""【中文版】

最近重新開始認真練習 LeetCode / 演算法時，我有一個很深的體悟。

我發現自己過去十多年在 production 環境工作的習慣，某種程度上，反而讓我一開始很難進入演算法思維。

因為在真實 production 世界裡，很多時候最重要的事情其實不是「核心功能」，而是：

- error handling
- reconciliation
- retry
- consistency
- logging
- edge case
- transaction safety
- fallback strategy

有時甚至可以說，「不要出事」的重要性遠高於「功能本身」。

長期在這種環境下工作後，大腦會自然習慣：
「先把所有風險與邊界條件一起背進問題裡。」

所以一開始刷題時，我常常會不自覺把問題複雜化。

但最近我開始慢慢理解：

演算法很多時候真正想測試的，其實不是：
「你能不能把整個 production 世界完整防守起來。」

而是：

「你能不能先看見問題最核心的形狀。」

例如：

Two Sum 真正的核心不是 error handling，
而是：

「你有沒有看見 complement lookup pattern。」

DP 真正重要的不是把所有情況硬列出來，
而是：

「你有沒有理解 state transition。」

這對我來說是一個很有趣的轉變。

因為我開始意識到：

production engineering 與 algorithmic abstraction，
其實是兩種不同層次的思維。

前者在處理真實世界的混亂與風險。
後者則是在訓練如何抽象化問題本質。

而我現在，也正在重新學習如何在這兩者之間切換。


==================================================


【English Version】

Recently, while getting back into LeetCode and algorithm practice seriously, I realized something interesting.

My past decade of experience in large-scale production environments actually made it harder for me to initially think in an “algorithmic” way.

Because in real production systems, the hardest part is often not the core feature itself, but things like:

- error handling
- reconciliation
- retries
- consistency
- logging
- edge cases
- transaction safety
- fallback strategies

Sometimes, “making sure nothing breaks” is far more important than the feature itself.

After years working in that environment, my brain became naturally trained to:
“Carry all the risks and edge cases into the problem immediately.”

As a result, when I first started solving algorithm problems again, I tended to overcomplicate them.

But recently, I started to understand:

Algorithm interviews are often not testing whether you can fully defend a production system.

They are testing whether you can first identify the core shape of the problem.

For example:

The essence of Two Sum is not error handling.
It’s whether you recognize the complement lookup pattern.

The essence of Dynamic Programming is not listing every possible situation manually.
It’s whether you understand state transitions.

This realization has been surprisingly refreshing for me.

Because I’m starting to see that production engineering and algorithmic abstraction are actually two very different layers of thinking.

One deals with real-world chaos and operational risk.
The other trains your ability to extract the essence of a problem through abstraction.

And right now, I’m learning how to switch between those two modes of thinking again.
"""
print(f"Saved to: {content}")

# path = Path("/mnt/data/linkedin_algorithm_reflection.txt")
# path.write_text(content, encoding="utf-8")

# print(f"Saved to: {path}")


# 需求
# 讀取整份 txt 檔
# 統計以下關鍵字各出現幾次：
keywords = [
    "production",
    "algorithm",
    "state",
    "error",
    "Python",
]
# 最後輸出：
# {
#     "production": 5,
#     "algorithm": 4,
#     ...
# }
# 額外要求（順便練）
# 1. 忽略大小寫

# 例如：

# Algorithm
# algorithm
# ALGORITHM

# 都算同一個。

# 2. 練習：
# with open(...)
# .read()
# .lower()
# dict
# loop
# string count

# 額外挑戰（可選）

# 如果你寫完很順。

# 你可以再挑戰：

# 不用 .count()

# 而是：

# 自己 split
# 自己掃描
# 自己累積

# 這會更接近真正 parsing 思維。

# 這題其實很適合你現在。

# 因為它會把：

# file io
# dict
# string
# loop
# state accumulation

# 全部串在一起。

from typing import Dict, List

keywords = [
    "production",
    "algorithm",
    "state",
    "error",
    "python",
]

file_path = r'C:\Users\user\Desktop\啟動未來\文章\linkedin_algorithm_reflection.txt'

def read_file(file_path: str) -> file:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_keywords(file_path: str, keywords: List[str]) -> Dict[str, int]:

    content = read_file(file_path).lower()

    res = {}
    for keyword in keywords:
        res[keyword] = content.count(keyword)
        
    return res

result = count_keywords(file_path, keywords)

print(result)


def count_keywords_2(file_path: str, keywords: List[str]) -> Dict[str, int]:
    content = read_file(file_path).lower()

    res = {}
    
    words = content.split(' ')
    
    print('words', words)
    print('keywords', keywords)
    
    for key in keywords: # 以防文字裡完全沒出現，確保 key 清單都在
        res[key] = 0
        
    for word in words:
        word_clean = word.strip(".,!?():\"\n")
        print('clean:', word_clean)
        if word_clean in keywords:
            res[word_clean] = res.get(word_clean, 0) + 1
    return res

result_2 = count_keywords_2(file_path, keywords)


print('result count:', result)
print('result no count:', result_2)
print('keywords', keywords)