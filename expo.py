# Efficiently exponentially its big numbers modulo n.
# In other words, (m^d) mod n
# Restrictions: d must be greater than 1
def expo(m, d, n):

    # Convert d into string of binary representation with leading 1 omitted,  e.g. 4 = "00"
    bin_str = ("{}".format(bin(d)[3:]))
    result = m # initialize result

    for bit in bin_str:
        result = (result ** 2) % n
        if bit == "1":
            result = (result * m) % n

    return result


#print(expo(10, 3, 56))
