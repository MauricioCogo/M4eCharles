from src.charles import Charles


def main():
    charles = Charles()

    print("Charles iniciado.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        prompt = input("Você: ")

        if prompt.lower() == "sair":
            break

        response = charles.ask(prompt)

        print(f"\nCharles: {response}\n")


if __name__ == "__main__":
    main()