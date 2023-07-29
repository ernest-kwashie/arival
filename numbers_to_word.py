def number_to_word(num):
    word_dict = {
        0: "zero", 10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }
    if num in word_dict:
        return word_dict[num]
    elif num < 20:
        # For numbers 1 to 19, return individual words.
        word_dict = {
            1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
            7: "seven", 8: "eight", 9: "nine", 11: "eleven", 12: "twelve",
            13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
            17: "seventeen", 18: "eighteen", 19: "nineteen"
        }
        return word_dict[num]
    else:
        # For numbers above 20, return the wordy version for tens and ones separately.
        tens_digit = num // 10 * 10
        ones_digit = num % 10
        return f"{word_dict[tens_digit]}-{word_dict[ones_digit]}"

def main():
    for num in range(101):
        if num % 10 == 0:
            print(number_to_word(num))
        else:
            print(num)

if __name__ == "__main__":
    main()
