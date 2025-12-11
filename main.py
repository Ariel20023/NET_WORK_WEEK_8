from core.utils import *
from core.output_string import *

if __name__ == "__main__":
    while True:
        user_input = user_input()#מכניס מסכה וip
        ip_health_checks = ip_health_checks(user_input[0])#בודק אם ip תקין
        mask_health_checks = mask_health_checks(user_input[1])#בודק אם מסכה תקינה
        if ip_health_checks and mask_health_checks:#אם שניהם תקינים ממשיכים
            break
        else:
            continue

    ip_arr = converts_something_to_array(user_input[0])#אחרי הבדיקות הופכים ip  למערך לצורך חישובים
    mask_arr = converts_something_to_array(user_input[1])#אחרי הבדיקות הופכים mask  למערך לצורך חישובים
    ip_bin = dec_to_bin8(ip_arr)#הופך מדצימלי לבינארי
    mask_bin = dec_to_bin8(mask_arr)#הופך מדצימלי לבינארי
    net_work_address = net_work_address(ip_bin, mask_bin)#מחשב network בינארי
    nice_network_address = bin32_to_ip_or_mask_to_net_work_address_or_something(net_work_address)#מחשב network address בצורה יפה
    bin_to_cidr = bin_to_cidr(mask_bin)#הופך ל cider לצורך חישובים
    calc_broadcast = calc_broadcast(net_work_address, bin_to_cidr)#מחשבcalc_broadcast לפי cider ומחזיר בבינארי
    nice_broadcast= bin32_to_ip_or_mask_to_net_work_address_or_something(calc_broadcast)#מחשב broadcast בצורה יפה
    num_of_host = num_of_host(bin_to_cidr)#מחשב את כמות ה host








#-----------------------------------------------------------------------------------------------------------
#שליחה להדפסה
    format_input_ip = format_input_ip(user_input[0])
    format_subnet_mask = format_subnet_mask(user_input[0])
    format_network_address = format_network_address(nice_network_address)
    format_broadcast_address = format_broadcast_address(nice_broadcast)
    format_num_hosts = format_num_hosts(num_of_host)
    format_cidr_mask = format_cidr_mask(bin_to_cidr)
    write_output_file(format_input_ip, format_subnet_mask, format_network_address, format_broadcast_address,format_num_hosts, format_cidr_mask)  # פונקציה שכותבת לקובץ























