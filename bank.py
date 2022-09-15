#Tugas Algoritma Pemrograman

def greeting(tatya):
    tatya = tatya.strip().lower()
    if "hello" in tatya:
        print("$0")
    elif tatya[0] == "h":
        print("$20")
    else:
        print("$100")

velo = input("Input Greeting: ")
greeting(velo)