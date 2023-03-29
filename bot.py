import pyautogui

while True:
     keep_button = pyautogui.locateOnScreen('keep_button.png', confidence=0.9)
     if keep_button:
          pyautogui.click(keep_button.left + 10, keep_button.top + 10)
          print("keep")
     else:
          sell_all_button = pyautogui.locateOnScreen('sell_all_button.png')
          if sell_all_button:
               pyautogui.click(sell_all_button.left + 10, sell_all_button.top + 10)
               print("sell all")
          else:
               # sell_all_over_button = pyautogui.locateOnScreen('sell_all_over_button.png')             
               # if sell_all_over_button:
               #      pyautogui.click(sell_all_over_button.left + 10, sell_all_over_button.top + 10)
               #      print("sell")

                    open_button = pyautogui.locateOnScreen('open_button.png')
                    if open_button:
                         pyautogui.click(open_button.left + 10, open_button.top + 10)
                         print("open")
                         while not pyautogui.locateOnScreen('sell_all_button.png'):
                                   pass

                    else:
                         open_button_2 = pyautogui.locateOnScreen('open_button_2.png')  
                         if open_button_2:
                              pyautogui.click(open_button_2.left + 10, open_button_2.top + 10)
                              print("open")
                              while not pyautogui.locateOnScreen('sell_all_button.png'):
                                   pass

