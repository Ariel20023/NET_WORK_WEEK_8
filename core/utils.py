def user_input():
    ip = input("enter ip in format x.x.x.x")
    mask = input("enter mask in format x.x.x.x")
    return ip,mask



def ip_health_checks(ip):
    try:
        ip_split = [int(x) for x in ip.split(".")]
    except:
        print("The IP is invalid. ")
        return False
    if len(ip_split) == 4:
        for i in ip_split:
            if i >= 0 and i < 256 and type(i) is int:
                continue
            else:
                print("The IP address is invalid.")
                return  False
        print("good")
        return  True
    print("The IP is invalid. ")
    return False




def mask_health_checks(mask):
    try:
        mask_split = [int(x) for x in mask.split(".")]
    except:
        print("The mask is invalid. ")
        return False
    if len(mask_split) == 4:
        for i in mask_split:
            if i >= 0 and i < 256 and type(i) is int:
                continue
            else:
                print("The mask address is invalid.")
                return  False
        print("good")
        return  True
    print("The mask is invalid. ")
    return False



def converts_something_to_array(something):#אחרי הבדיקות הופכים למערך לצורך חישובים
    return [int(x) for x in something.split(".")]



def dec_to_bin8(arr):#הופך מדצימלי לבינארי
    bits = ""
    for octet in arr:
        for i in range(7, -1, -1):
            bits += "1" if octet & (1 << i) else "0"
    return bits



def net_work_address(ip_bin,mask_bin):#מחשב network בינארי
        result = ""
        for i in range(32):
            if ip_bin[i] == "1" and mask_bin[i] == "1":
                result += "1"
            else:
                result += "0"
        return result


def bin_to_dec(binary):
    result = 0
    power = 0
    for i in range(len(binary) - 1, -1, -1):
        result += int(binary[i]) * (2 ** power)
        power += 1
    return result

def bin32_to_ip_or_mask_to_net_work_address_or_something(bin32):#מחשב network address
    arr = []
    for i in range(0, 32, 8):
        arr.append(bin_to_dec(bin32[i:i+8]))
    # print(arr)
    return arr


def bin_to_cidr(mask_binary):#הופך ל cider לצורך חישובים
    cider = 0
    for i in mask_binary:
        if i == "1":
            cider += 1
    return cider


def calc_broadcast(network_bin, cidr):#מחשבcalc_broadcast לפי cider ומחזיר בבינארי
    result = ""
    for i in range(32):
        if i < cidr:
            result += network_bin[i]
        else:
            result += "1"
    return result




#
# def ip_class(first_octet):# קובע את סוג הרשת לפי האוקטטה הראשונה
#
#     if first_octet <= 127:
#         return "CLASS A"
#     elif first_octet <= 191:
#         return " CLASS B"
#     elif first_octet <= 223:
#         return "CLASS C"
#     else:
#         return " Classless  "



def num_of_host(cidr):#מחשב מספר host באמצעות cider
    return 2**(32 - cidr)
























