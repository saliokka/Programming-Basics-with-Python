change = float(input())
# превръщаме парите в стотинки.
change = int(change * 100)
coins_counter = 0
coins_counter += change // 200 # 2.40 = 2 levove
change %= 200 # 2.40 = 40 stotinki
# repeat
coins_counter += change // 100
change %= 100
coins_counter += change // 50
change %= 50
coins_counter += change // 20
change %= 20
coins_counter += change // 10
change %= 10
coins_counter += change // 5
change %= 5
coins_counter += change // 2
change %= 2
coins_counter += change // 1
change %= 1

print(coins_counter)
