text = input("Enter text: ")
ending = input("Enter ending: ")

def solution(text, ending):
    end = len(ending)
    tex = len(text)
    for i in range (1, end+1):
        if tex<end:
            result = "False"
        elif text[-i]==ending[-i]:
            result = "True"
        else:
            result = "False"
    print(result)
solution(text, ending)