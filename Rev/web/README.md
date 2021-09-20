# web

- First we have to find the version number that has the most 0s which is `100000000`

- Then slowly search for the version number by narrowing down the version from the largest one

For example:
  if `v10` exists but `v11` doesnt, that means v10 is the highest version number 

- In our case the highest was `130000000`, we can do the same thing here 

For example: 
  try `133000000` and `134000000`, the second one gives us a version not found, meaning `133000000` is our next version number

- Do that for every 0 until you get the `flag` executable

FINAL VERSION `v133791021`

# FLAG flag{h0w_l0ng_wher3_y0u_g0ne_f0r_3910512832}
