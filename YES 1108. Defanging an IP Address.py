# YES 1108. Defanging an IP Address

# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
def defangIPaddr(address):
    dot = ''
    for ad in address:
        if ad == '.':
            ad = '[.]'
        dot += ad
    return dot


# 2 solution  return '[.]'.join(address.split('.'))
# 3 solution return address.replace('.', '[.]')


print(defangIPaddr("1.1.1.1"))
print(defangIPaddr("255.100.50.0"))
