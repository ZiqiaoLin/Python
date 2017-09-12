def counting_letters(str,desired_letter):
    """
    (str) -> number
    Return the number of certain letter of an input string
    >>> counting_letters("banana","a")
    3
    """


    count = 0
    #desired_letter = input("please give me an letter you want:")
    for letter in str:
        if (letter == desired_letter):
            count = count + 1
    print(count)