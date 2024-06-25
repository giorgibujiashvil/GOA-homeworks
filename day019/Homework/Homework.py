"""1) 
ნამრავლის გამოთვლა: დაწერეთ ალგორითმი, რომელიც დაბეჭდავს სიის ყველა ელემენტის ნამრავლს."""

def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

my_list = [1, 2, 3, 4, 5]
print(multiply_list(my_list))



"""2)
უარყოფითი რიცხვების ამოღება: დაწერეთ ალგორითმი, რომელიც მიიღებს მთელ რიცხვთა სიას და ამოიღებს ყველა უარყოფით რიცხვს, დაბეჭდავს ახალ სიას ამ ელემენტების გარეშე."""

def filter_negative_numbers(lst):
    result = [num for num in lst if num < 0]
    return result

my_list = [1, -2, 3, -4, 5, -6]
print(filter_negative_numbers(my_list))



"""3)
საშუალოს პოვნა: დაწერეთ ალგორითმი, რომელიც მიიღებს სიას და დააბრუნებს მის საშუალო არითმეტიკულს."""

def average(lst):
    if len(lst) == 0:
        return 0  # თუ სია ცარიელია, დააბრუნებს 0-ს
    return sum(lst) / len(lst)

my_list = [10, 5, 9, 8, 7]
print(average(my_list))




"""4)
სიების შეერთება: დაწერეთ ალგორითმი, რომელიც მიიღებს ორ რიცხვთა სიას, გააერთიანებს მათ ერთ სიაში და ამ სახით დაბეჭდავს."""

def merge_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list


list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(merge_lists(list1, list2))



"""5)
დუბლიკატების სია: დაწერეთ ალგორითმი, რომელიც მიიღებს სიას. თქვენ შემდეგ ამ სიის დუბლიკატებს გადაიტანთ ახალ სიაში და დაბეჭდავთ მას."""

def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

my_list = [1, 2, 2, 3, 4, 4, 4, 5]
print( find_duplicates(my_list))