import random

def generate_constrained_combinations():
    """
    生成滿足以下所有規則的 9 組四位數組合：
    1. 四位數內部不得有重複的數字。
    2. 9 組四位數中的第一位數、第二位數、第三位數、第四位數，
       都只能出現一次（即每位數上的數字在所有 9 組中是 1~9 的排列）。
    3. 9 組四位數中，任意一組的第一位數與第四位數，不得為其他組的第四位數與第一位數。
       例如：8926 和 6358 這兩組就不行。
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

        combinations_as_lists = [] # 將組合儲存為數字列表，便於規則檢查
        all_rules_met_for_this_attempt = True

        # --- 步驟 1: 構建組合並檢查規則 1 (內部數字不重複) ---
        for i in range(9): # 遍歷 9 組組合
            d1 = pos1_digits[i]
            d2 = pos2_digits[i]
            d3 = pos3_digits[i]
            d4 = pos4_digits[i]

            current_combination_digits = [d1, d2, d3, d4]

            # 檢查規則 1：當前四位數內部是否有重複的數字
            if len(set(current_combination_digits)) != 4:
                all_rules_met_for_this_attempt = False # 發現不符合規則 1 的情況
                # print(f"DEBUG: 規則 1 在第 {i+1} 組組合中被違反：{current_combination_digits}。重新嘗試生成。")
                break # 跳出當前迴圈，重新生成所有的位數排列
            
            combinations_as_lists.append(current_combination_digits)
        
        # 如果有任何一組違反了規則 1，則重新開始整個生成過程
        if not all_rules_met_for_this_attempt:
            continue # 跳到 while True 迴圈的下一次迭代

        # --- 步驟 2: 檢查規則 3 (首尾數字反向對稱性) ---
        # 只有在所有組合都滿足規則 1 的前提下，才檢查規則 3
        for i in range(9):
            comb_A = combinations_as_lists[i]
            d1A = comb_A[0]
            d4A = comb_A[3]

            for j in range(i + 1, 9): # 檢查與其他不同的組合
                comb_B = combinations_as_lists[j]
                d1B = comb_B[0]
                d4B = comb_B[3]

                # 檢查規則 3：(第一位數 A == 第四位數 B) 且 (第四位數 A == 第一位數 B)
                if (d1A == d4B and d4A == d1B):
                    all_rules_met_for_this_attempt = False
                    # print(f"DEBUG: 規則 3 被違反！組合 {comb_A} 和 {comb_B} 產生衝突。重新嘗試生成。")
                    break # 規則 3 被違反，跳出內層迴圈
            
            if not all_rules_met_for_this_attempt:
                break # 如果內層迴圈發現衝突，跳出外層迴圈
        
        # 如果經過所有檢查，所有規則都滿足，則返回結果
        if all_rules_met_for_this_attempt:
            # 將數字列表轉換為字串格式以便輸出
            return ["".join(map(str, combo)) for combo in combinations_as_lists]

# 執行並獲取結果
print("正在生成符合所有規則的 9 組四位數組合，這可能需要多次嘗試和一些時間...")
generated_combinations = generate_constrained_combinations()

# 輸出結果
print("\n生成的 9 組四位數組合：")
for i, combo in enumerate(generated_combinations):
    print(f"{combo}")

# 驗證所有規則 (可選，但對於理解和確認很重要)
print("\n--- 驗證所有規則 ---")

# 驗證規則 2 (每位數在 9 組中都只出現一次)
pos1_list = [int(s[0]) for s in generated_combinations]
pos2_list = [int(s[1]) for s in generated_combinations]
pos3_list = [int(s[2]) for s in generated_combinations]
pos4_list = [int(s[3]) for s in generated_combinations]

print(f"第一位數列表：{pos1_list} (不重複: {len(set(pos1_list)) == 9})")
print(f"第二位數列表：{pos2_list} (不重複: {len(set(pos2_list)) == 9})")
print(f"第三位數列表：{pos3_list} (不重複: {len(set(pos3_list)) == 9})")
print(f"第四位數列表：{pos4_list} (不重複: {len(set(pos4_list)) == 9})")

# 驗證規則 1 (四位數內部數字不重複)
for i, combo_str in enumerate(generated_combinations):
    digits = [int(d) for d in combo_str]
    print(f"第 {i+1} 組 {combo_str} 內部數字不重複: {len(set(digits)) == 4}")

# 驗證規則 3 (首尾數字反向對稱性)
rule3_violation_found = False
for i in range(9):
    comb_A_str = generated_combinations[i]
    d1A_str = comb_A_str[0]
    d4A_str = comb_A_str[3]

    for j in range(i + 1, 9):
        comb_B_str = generated_combinations[j]
        d1B_str = comb_B_str[0]
        d4B_str = comb_B_str[3]

        if (d1A_str == d4B_str and d4A_str == d1B_str):
            print(f"規則 3 違反！組合 {comb_A_str} 和 {comb_B_str} 發生衝突。")
            rule3_violation_found = True
            break
    if rule3_violation_found:
        break

if not rule3_violation_found:
    print("規則 3: 未發現衝突。")
