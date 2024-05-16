string = 'bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd'
max_width = 9
def my_solution(string, max_width):
    all_together = []
    listy = list(string)
    all_together.append(listy[0:max_width])
    last_mod = 0
    for count, i in enumerate(listy):
        if count % max_width == 0 and count > max_width:
            all_together.append(listy[count-max_width:count])
            last_mod = count
    # add the ending on
    all_together.append(listy[last_mod:len(listy)])
    word = ''
    for i in all_together:
        word += f"{''.join(i)}\n"
    return word

def using_imports(string, max_width):
    import textwrap
    result=textwrap.fill(string,max_width)
    return result