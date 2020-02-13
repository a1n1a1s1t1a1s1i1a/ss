import razkad, zakad


def main():
    print("ЧЕГО ХОТИТЕ?")
    k = input()
    if k == "zak":
        zakad.encode_to_morse(input())
    else:
        razkad.decode_from_morse(input())


main(












