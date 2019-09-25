on_pan = int(input())
minut = int(input())
cutlet = int(input())


side_cutlet = cutlet * 2
n_fry_up = (side_cutlet + on_pan - 1) // on_pan
if (n_fry_up == 1):
    n_fry_up = 2
all_minut = n_fry_up * minut
print(all_minut)
