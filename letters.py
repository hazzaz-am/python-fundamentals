def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]

    for name in names:
        print(write_letter(name, "Princes Peach"))


def write_letter(receiver, sender):
    return f"""
    Dear {receiver},
    You are cordially invited to a ball dance.

    Sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
  """


main()
