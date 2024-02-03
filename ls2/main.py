# method -> for -> count -> 2 -> 

# def unique(numbers): 
#     if numbers is None or len(numbers) < 1:
#         return []
#     unique_values = list()
#     for number in numbers: 
#         if numbers.count(number) < 2: 
#             unique_values.append(number)
#         elif not unique_values.count(number):
#             unique_values.append(number)
#     return unique_values


# def unique(numbers): 
#     if numbers is None or len(numbers) < 1:
#         return []
#     elif len(numbers) == 1:
#         return numbers
#     return list(set(numbers))

# exaple_1 = [1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 9]
# exaple_2 = [1]
# exaple_3 = []
# print(unique(exaple_1))
# print(unique(exaple_2))
# print(unique(exaple_3))

# list , tuple, dict -> set 

# def intersection(set1, set2):
#     result_set = set()
#     for element in set1:
#         if element in set2:
#             result_set.add(element)
#     return result_set

# def custom_intersection_of_lists(list1, list2):
#     return list(intersection(set(list1), set(list2)))

# def intersection_of_lists(list1, list2):
#     return list(set(list1).intersection(set(list2)))

# list_a = [1, 2, 3, 4, 5]
# list_b = [3, 4, 5, 6, 7]
# result = intersection_of_lists(list_a, list_b)
# print(result)  # Ожидаемый результат: [3, 4, 5]

# def merge_interests(*user_dicts):
#     merged = set()

#     for user_dict in user_dicts:
#         for interests in user_dict.values():
#             merged.update(interests)
#     return merged

# user1 = {'Alice': {'music', 'movies', 'books'}}
# user2 = {'Bob': {'sports', 'music', 'cooking'}}
# user3 = {'Charlie': {'movies', 'cooking', 'travel'}}

# result = merge_interests(user1, user2, user3)

# print(result)
# Ожидаемый результат: {'music', 'movies', 'books', 'sports', 'cooking', 'travel'}

from time import perf_counter
from functools import wraps

def memoize(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        
        return cache[key]
    
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    start = perf_counter()
    f = fibonacci(300)
    end = perf_counter()
    print(f)
    print(f"Time: {end - start} seconds\n")

# def my_decarator(func):
#     def wrapper():
#         print("Что - то до начала")
#         func()
#         print("Что - то после")
#     return wrapper

# @my_decarator
# def my_func():
#     print("Hello World")

# my_func()