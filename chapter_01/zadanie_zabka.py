def main(x, y, s):
    res = int((y - x) / s)
    if (y - x) % s == 0:
        return res
    else:
        return res + 1


if __name__ == "__main__":
    values = input("podaj \n1)pozycje zabki, \n2)koniec drogi, " + \
        "\n3)dlugosc skoku \noddzielone spacjami\n")
    # values = "10 85 30"
    data = values.split()
    x, y, s = int(data[0]), int(data[1]), int(data[2])

    result = main(x, y, s)
    print("\n" + "zabka skoczy najmniej " + str(result) + " skokow")
