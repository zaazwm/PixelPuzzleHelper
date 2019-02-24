MAP_SIZE = 15

def print_func(str_p):
    str1=''
    str2=''
    str3=''
    str4=''
    if len(str_p)>10:
        str1=str_p[:10] + '| '
        if len(str_p)>20:
            str2=str_p[10:20] + '| '
            if len(str_p)>30:
                str3=str_p[20:30] + '| '
                if len(str_p)>40:
                    str4=str_p[30:40] + '| '
                else:
                    str4=str_p[30:]
            else:
                str3=str_p[20:]
        else:
            str2=str_p[10:]
    else:
        str1=str_p

    print (str1+str2+str3+str4)


while True:
    nbs = raw_input('the numbers: ')
    if nbs.startswith('q'):
        break
    if ' ' not in nbs and len(nbs)>=3:
        nbs_list = list(nbs)
    else:
        nbs_list = nbs.split(' ')
    nbs_nums = []
    nbs_sum = 0
    for nb in nbs_list:
        nbs_nums.append(int(nb))
        nbs_sum+=int(nb)
    nbs_sum+=(len(nbs_nums)-1)
    nbs_res = []
    for nb in nbs_nums:
        nbs_res.append(max(nb-(MAP_SIZE-nbs_sum), 0))
    if sum(nbs_res)<=0:
        print_func('_ '*MAP_SIZE)
        continue

    prt_str = ''
    for i in range(len(nbs_nums)):
        if i>0:
            prt_str+='_ '
        prt_str+=('_ '*(nbs_nums[i]-nbs_res[i]))
        prt_str+=('o '*(nbs_res[i]))
    prt_str+=('_ '*(MAP_SIZE-(sum(nbs_nums)+len(nbs_nums)-1)))

    print_func(prt_str)
