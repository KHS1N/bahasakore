def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def search_words(words, query):
    matching_words = [word for word in words if query in word]
    return matching_words

def main():
    file_path = 'kosa_kata.txt'
    words_list = load_words(file_path)
    
    print("Alat Pencarian Kosa Kata Bahasa Kore!")
    
    while True:
        print("\nMenu:")
        print("1. Pencarian B. Indonesia")
        print("2. Keluar")
        
        choice = input("Pilih menu (1/2): ")
        
        if choice == '1':
            query = input("\nMasukkan kata yang ingin dicari: ")
            matching_words = search_words(words_list, query)
            
            if matching_words:
                print(f"\nDitemukan {len(matching_words)} kata yang sesuai:")
                for word in matching_words:
                    print(word)
            else:
                print("Tidak ditemukan kata yang sesuai.")
        
        elif choice == '2':
            print("Terima kasih sudah menginstall kamus ini.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == '__main__':
    main()
