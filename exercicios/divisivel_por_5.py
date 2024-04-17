def main():
    start_number = 1
    end_number = int(input("Até qual número você quer chegar? "))
    skip = int(input("De quantos números você quer pular? "))

    current_number = start_number

    while current_number <= end_number:
        if current_number % 5 == 0:
            print("O número {} é divisível por 5. O programa será encerrado.".format(current_number))
            break
        else:
            print("Número:", current_number)
        
        current_number += skip

    print("Programa encerrado.")

if __name__ == "__main__":
    main()