def size_of_str(str):
    return len(str)

def concat_strings(first, second):
    return first + second

def duplicate_string(str, copy):
    return str*copy
    # return new string which is copy of str copy times
    # example -> duplicate_string('s', 2) == 'ss'

def reverse(str):
    return str[::-1]
    # return reverse of the string

def is_substring(str, substr):
    return substr in str
    # return true if substr is the substring of str, false otherwise


