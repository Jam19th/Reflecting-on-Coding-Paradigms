def flatten_and_sort(lst):
    output = []
    for item in lst:
        if type(item) == list:
            for subitem in item:
                output.append(subitem)
        else:
            output.append(item)
            
    return sorted(output)

nested = [[1, 3, 5], [100], [2, 4, 6]]

output = flatten_and_sort(nested)
print(output)

print(nested)

'''
How does this solution ensure data immutability?

The solution creates a new list and adds the items from the input list to the new list. The input list is not modified.
'''

'''
Is this solution a pure function? Why or why not?

Yes, this solution is a pure function. It does not modify the input list and it does not have any side effects.
'''

'''
Is this solution a higher order function? Why or why not?

No, this solution is not a higher order function. It does not take a function as an argument and it does not return a function.
'''

'''
Would it have been easier to solve this problem using a different programming style?

Yes, it would have been easier to solve this problem using a different programming style. For example, it would have been easier to solve this problem using a functional programming style.
'''

'''
Why in particular is functional programming a helpful paradigm when solving this problem?

Functional programming is a helpful paradigm when solving this problem because it allows us to write code that is easier to read and understand. It also allows us to write code that is easier to test and debug.
'''