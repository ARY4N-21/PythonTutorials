# curr_light = input("Which light color in traffic: ")
# if curr_light == "red":
#     print("STOP")
# elif curr_light == "yellow":
#     print("WAIT")
# elif curr_light == "green":
#     print("GO")
# else:
#     print("Invalid Light Color")

# loyalty_cust = input("Are you a premium card holder? (yes/no): ").strip().lower() # strip is used for trimming
# total_bill = 120
# disc = 0
# if loyalty_cust == "yes" and total_bill > 100:
#     # 20% discount
#     disc = 20
#     print(f"{disc}% discount applied")
#     total_bill = total_bill - ((float(total_bill) / 100) * 20)
# elif total_bill > 100:
#     # 10% discount
#     disc = 10
#     print(f"{disc}% discount applied")
#     total_bill = total_bill - ((float(total_bill) / 100) * 10)
# else:
#     print(f"{disc}% discount applied")

# print("Final Bill:", total_bill)




# Switch or Match Statement
http_status = 201
match http_status:
    case 200 | 201:
        print("Success")
    case 404:
        print("Not Found")
    case 400:
        print("Bad Request")
    case 500 | 501:
        print("Server Error")
    case _: # default case
        print("Unknown")