# Описание Директории
Здесь я буду размещать исходный код программы!

# Список API

- REST (https://aws.amazon.com/ru/what-is/restful-api/)
- GRAPHQL (https://graphql.org/)
- GRPC (https://grpc.io/)

## Пример форматирования кода на Python:

```py 
def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
```
