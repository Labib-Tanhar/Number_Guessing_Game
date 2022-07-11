#cli based game
num = "12"
input_num = input("Guess a number ")

#programs

if num < input_num :
    print("Your number is too high")

elif num > input_num:
    print("Your number is too short")

else:
    print("Congratulation🎉, You've got the right number")

#MESSAGE
print("Want to play again?, Just Reload")