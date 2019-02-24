MAP_SIZE = 15

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
        print ('_ '*MAP_SIZE)
        continue

    prt_str = ''
    for i in range(len(nbs_nums)):
        if i>0:
            prt_str+='_ '
        prt_str+=('_ '*(nbs_nums[i]-nbs_res[i]))
        prt_str+=('o '*(nbs_res[i]))
    prt_str+=('_ '*(MAP_SIZE-(sum(nbs_nums)+len(nbs_nums)-1)))

    print prt_str
