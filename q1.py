
total_number_of_t_shirt = input()

t_shirt_sizes = input()

n_request = input()

requested_sizes = input()
fulfil = [0 for i in range(int(n_request))]

available_sizes_split = t_shirt_sizes.split()
reqest_sizes_split = requested_sizes.split()

if int(n_request) > int(total_number_of_t_shirt):
    print("No")
    
t_shirt_dict = dict()

for i in range(int(total_number_of_t_shirt)):
    if available_sizes_split[i] in t_shirt_dict.keys():
        t_shirt_dict[available_sizes_split[i]] = t_shirt_dict[available_sizes_split[i]] + 1
    else:
        t_shirt_dict[available_sizes_split[i]] = 1
        

for i in range(int(n_request)):
    for j in range(int(total_number_of_t_shirt)):
        if reqest_sizes_split[i][-1] != 'S':
            if reqest_sizes_split[i] in available_sizes_split[j]:
                if t_shirt_dict[available_sizes_split[j]] > 0:
                    fulfil[i] = 1
                    break
        else:
            temp = reqest_sizes_split[i]
            while(temp != 'S'):
                if temp[1:] in available_sizes_split[j]:
                    fulfil[i] = 1
                    break
                temp = temp[1:]
            if 'M' in t_shirt_dict.keys() or 'L' in t_shirt_dict.keys():
                fulfil[i] = 1
                break


if sum(fulfil) == int(n_request):
    print("Yes")
else:
    print("No")