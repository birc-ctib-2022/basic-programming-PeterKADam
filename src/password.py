import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
# password = "Abemader99@"
is_valid = False

# Do all the requirement checks here.

if len(password) > 5 and len(password) < 17:
    # print("password length is valid")
    if any([ord(x) in [64, 36, 35] for x in password]):
        # print("special char is valid")
        if any([a.islower() for a in password]):
            # print("lower is valid")
            if any([a.isupper() for a in password]):
                # print("upper is valid")
                if any([a.isnumeric() for a in password]):
                    # print("numeric char is valid")
                    is_valid = True


print(is_valid)
