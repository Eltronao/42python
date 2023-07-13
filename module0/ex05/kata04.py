
kata = (0, 4, 132.42222, 10000, 12345.67)

def main():
    print("module_{:02d}, ex_{:02d} : {}, {:.2e}, {:.2e}".format(kata[0], kata[1], round(kata[2], 2), kata[3], kata[4], ))

main()