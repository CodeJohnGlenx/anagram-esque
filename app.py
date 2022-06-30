from flask import Flask, render_template, request

"""
use:
Binary searches a string partially or fully in a given list

parameters:
search_arr : list() - list of string values where search_str will be searched
left : int - left side of the search_arr 
right: int - right side of the search_arr
search_str : string - string to be searched in search_arr 
partial : boolean - partially matches a string using startswith()
"""
def binarySearch(search_arr, left, right, search_str, partial):
    if right >= left:
        # get middle of left and right part of search_arr
        mid = left + (right - left) // 2

        # partial binary search and return the index if matched
        if partial == True and search_arr[mid].startswith(search_str):
            return mid
        # standard binary search and return the index if matched
        elif partial == False and search_arr[mid] == search_str:
            return mid
        
        # perform binary search on the left side of the mid/search_arr
        elif search_arr[mid] > search_str:
            return binarySearch(search_arr, left, mid-1, search_str, partial)
        
        # perform binary search on the right side of the mid/search_arr
        else:
            return binarySearch(search_arr, mid + 1, right, search_str, partial)
    else:
        return -1


"""
use:
generates a permutation of letters that is present in dict_words from the given array

parameters:
dict_words : list() - list of words or string values
string: string - initial and permutation value of letters that is based from array
array : list() - list of letters to be permutted
out_pern: dict() of set() - store/add permuation of strings that exists in dict_words
"""
def permute(dict_words, string, array, out_perm):
    # iterate every letter
    for i in range(len(array)):
        # concatenate current character to string
        str = string + array[i]
        arr = array.copy()

        # remove current character from array
        arr.pop(i)

        """
        Here, backtracking occurs when a permutation of a string (incomplete set of characters)  
        does not start with any of the values present in dict_words. Permutation is performed if 
        a set of incomplete characters of a string starts with any of of the values in dict_words.
        """
        # perform partial binary search
        if binarySearch(dict_words, 0, len(dict_words)-1, str, True) != -1:
            # perform full binary search
            if binarySearch(dict_words, 0, len(dict_words)-1, str, False) != -1:
                # add permutation of a string to out_perm if it exists in dict_words
                out_perm[len(str)].add(str)
            # continue permutation if permuation of string starts with any of the values in dict_words 
            permute(dict_words, str, arr, out_perm)

# store dictionary words in this list
dict_words = []

# initialize Flask app
app = Flask(__name__)

# read words from eng_words.txt and store it in dict_words
with open('eng_words.txt', errors='ignore') as f:
    dict_words = f.read().splitlines()

# home page
@app.route("/")
def home_page():
    # get value of input text (letters)
    input_letters = request.args.get('solve-text')

    # check if there is an input
    if input_letters != None:
        # remove trailing and leading white spaces in input_letters then convert it into lowercase
        input_letters = input_letters.strip().lower()

        # display error if length of input is 0 or greater than 14
        if len(input_letters) < 1 or len(input_letters) > 14:
            return render_template("index.html", alert_type="alert-danger")
        # display error if input contains non-alphabetical characters
        elif not input_letters.isalpha():
            return render_template("index.html", alert_type="alert-danger")
        # if input is alphabetical
        elif input_letters.isalpha():
            perm_out = dict()
            # create a dict() of set() values and length of word as the key
            for i in range(len(input_letters)):
                perm_out[i+1] = set()

            # perform permutation and generate words from input that is present in dict_words
            permute(dict_words, '', list(input_letters), perm_out)

            # remove items that have empty set() values
            perm_out = {k: v for k, v in perm_out.items() if v}

            # export the generated words (perm_out) to home page
            return render_template("index.html", perm_out=perm_out, alert_type=None)
    return render_template("index.html", alert_type="alert-info")









