import random

def generate_constrained_combinations():
    """
    生成滿足以下規則的 9 組四位數組合：
    1. 四位數內部不得有重複的數字。
    2. 9 組四位數中的第一位數、第二位數、第三位數、第四位數，
       都只能出現一次（即每位數上的數字在所有 9 組中是 1~9 的排列）。
    """
    
    # 循環直到找到符合所有規則的組合
    while True:
        # 為了滿足規則 2，我們需要為每個「位數」創建一個 1 到 9 的隨機排列。
        # 這些排列將成為我們四位數的「列」。
        
        pos1_digits = list(range(1, 10)) # 第一位數的數字
        random.shuffle(pos1_digits)

        pos2_digits = list(range(1, 10)) # 第二位數的數字
        random.shuffle(pos2_digits)

        pos3_digits = list(range(1, 10)) # 第三位數的數字
        random.shuffle(pos3_digits)

        pos4_digits = list(range(1, 10)) # 第四位數的數字
        random.shuffle(pos4_digits)

        combinations = []
        all_rules_met_for_this_attempt = True

        # 現在，從這四個排列中，逐一取出數字來構成 9 組四位數。
        for i in range(9): # 遍歷 9 組組合
            d1 = pos1_digits[i]
            d2 = pos2_digits[i]
            d3 = pos3_digits[i]
            d4 = pos4_digits[i]

            current_combination_digits = [d1, d2, d3, d4]

            # 檢查規則 1：當前四位數內部是否有重複的數字
            # 如果集合的長度不等於 4，表示有重複數字
            if len(set(current_combination_digits)) != 4:
                all_rules_met_for_this_attempt = False # 發現不符合規則 1 的情況
                # print(f"DEBUG: 規則 1 在第 {i+1} 組組合中被違反：{current_combination_digits}。重新嘗試生成。")
                break # 跳出當前迴圈，重新生成所有的列

            combinations.append("".join(map(str, current_combination_digits)))
        
        # 如果經過 9 次檢查後，所有的組合都滿足規則 1，則返回結果
        if all_rules_met_for_this_attempt:
            return combinations
        # 如果沒有，while 迴圈會自動再次運行，生成新的列排列並重新檢查。

# 執行並獲取結果
print("正在生成符合規則的 9 組四位數組合，可能需要多次嘗試...")
generated_combinations = generate_constrained_combinations()

# 輸出結果
print("\n生成的 9 組四位數組合：")
for i, combo in enumerate(generated_combinations):
    print(f"第 {i+1} 組: {combo}")

# 驗證規則 (可選，但對於理解和確認很重要)
print("\n--- 驗證規則 ---")

# 提取每個位置的數字，以便驗證規則 2
pos1_list = [int(s[0]) for s in generated_combinations]
pos2_list = [int(s[1]) for s in generated_combinations]
pos3_list = [int(s[2]) for s in generated_combinations]
pos4_list = [int(s[3]) for s in generated_combinations]

print(f"第一位數列表：{pos1_list} (不重複: {len(set(pos1_list)) == 9})")
print(f"第二位數列表：{pos2_list} (不重複: {len(set(pos2_list)) == 9})")
print(f"第三位數列表：{pos3_list} (不重複: {len(set(pos3_list)) == 9})")
print(f"第四位數列表：{pos4_list} (不重複: {len(set(pos4_list)) == 9})")

for i, combo_str in enumerate(generated_combinations):
    digits = [int(d) for d in combo_str]
    print(f"第 {i+1} 組 {combo_str} 內部數字不重複: {len(set(digits)) == 4}")
