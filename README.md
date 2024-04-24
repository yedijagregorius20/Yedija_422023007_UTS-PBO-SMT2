Requirement Analysis & FURPS

        A.	Functional Requirement
                Pengelolaan Buku:
                •	Fungsi untuk menambahkan buku baru ke dalam sistem.
                •	Fungsi untuk menampilkan semua buku yang tersedia di perpustakaan.
                •	Fungsi untuk mencari buku berdasarkan judul atau pengarang.
                •	Fungsi untuk meminjam buku kepada anggota perpustakaan.
                •	Fungsi untuk mengembalikan buku yang dipinjam oleh anggota.
                
                Pengelolaan Anggota Perpustakaan:
                •	Fungsi untuk menambahkan anggota baru ke dalam sistem.
                •	Fungsi untuk memperbarui informasi anggota perpustakaan.
                •	Fungsi untuk mengelola informasi anggota, seperti nama dan ID.
                
                Pengelolaan Menu:
                •	Fungsi untuk menampilkan menu untuk pengguna perpustakaan, baik untuk pustakawan maupun anggota.
                •	Fungsi untuk menerima input dari pengguna dan memprosesnya sesuai dengan pilihan menu yang dipilih.
                Fungsi-fungsi Tambahan:
                •	Fungsi untuk menampilkan pesan kesalahan jika pilihan yang dimasukkan tidak valid.
                •	Fungsi untuk menangani interaksi dengan anggota yang meminjam atau mengembalikan buku.

          B.	Describe How
                Usability:
                Sistem ini memberikan antarmuka yang mudah digunakan baik untuk pustakawan maupun anggota perpustakaan. Pengguna dapat dengan mudah menambahkan, mencari, meminjam, dan mengembalikan buku dengan menggunakan menu yang disediakan.
                Informasi anggota dan buku tersimpan dengan baik dalam sistem, sehingga memungkinkan pengelolaan yang efisien dan pembaruan data secara tepat waktu.
                
                Reliability:
                Sistem memastikan keandalan dalam manajemen buku dan anggota perpustakaan dengan memvalidasi input pengguna dan memeriksa ketersediaan buku sebelum meminjamkannya kepada anggota.
                Data anggota dan buku disimpan dengan baik dalam struktur data yang sesuai, sehingga meminimalkan risiko kehilangan atau kerusakan informasi.
                
                Performance:
                Sistem ini dapat mengelola jumlah buku dan anggota perpustakaan yang besar dengan baik. Meskipun belum ada optimisasi khusus yang disertakan dalam kode, tetapi struktur data yang digunakan (misalnya, daftar untuk buku dan anggota) memungkinkan akses yang cepat dan efisien terhadap informasi yang diperlukan.
                Meskipun dalam implementasi yang lebih besar mungkin diperlukan optimisasi kinerja tambahan, seperti pengindeksan atau caching, untuk meningkatkan kinerja sistem secara keseluruhan.
                
                Supportiblity:
                Sistem ini menyediakan dukungan interaktif kepada pengguna melalui menu yang disediakan, sehingga memungkinkan pengguna untuk dengan mudah berinteraksi dengan sistem tanpa memerlukan pengetahuan teknis yang mendalam.
                Pesan kesalahan yang jelas dan panduan pengguna yang disediakan membantu pengguna dalam memahami bagaimana menggunakan sistem dengan benar.
                Potensi dukungan tambahan dapat meliputi integrasi dengan sistem manajemen database untuk menyimpan informasi secara permanen dan melindungi data dari kehilangan atau kerusakan.

          C.	Non-Functional Requirement
                1.	Kapabilitas, kesiapan kapasitas aplikasi untuk melakukan besar kecil banyaknya hal-hal yang dibutuhkan tanpa merusak kinerja. 
                2.	Kinerja, harus mampu bekerja dengan baik setiap fiturnya demi mendukung keberhasilan sistem.
                3.	Keamanan, kepastian keamanan setiap akun pengguna oleh aplikasi.
                4.	Ketahanan, kesediaan yang dipastikan ada untuk setiap pengguna kapanpun.


Identify Components

          Classes :
          •	Library: Mewakili entitas perpus, ini mengelola buku dan anggota.
          •	Book: Mewakili entitas buku dengan properti seperti judul, penulis, ISBN, dan ketersediaannya.
          •	Member: Untuk anggota perpustakaan dengan properti seperti nama, ID anggota, dan buku yang dipinjam.
          
          Object  :
          •	library: Sebuah turunan dari class ‘Library’.
          •	book: Contoh class ‘Book’ yang mewakili masing-masing buku.
          •	member: Contoh class ‘Member’ yang mewakili anggota perpustakaan.

          Methods :
            Library class:
            •	__init__(): Menginisialisasi library dengan daftar book dan anggota yang kosong.
            •	add_book(book): Menambahkan book ke perpustakaan.
            •	add_member(member): Menambahkan member ke perpustakaan.
            •	get_all_books(): Menampilkan semua book di perpustakaan.
            •	search_books(): Mencari book berdasarkan judul atau author.
            •	borrow_book(member, book): Mengizinkan member meminjam buku.
            •	return_book(member, book): Memungkinkan member mengembalikan buku.
            •	manage_member_info(): Mengelola informasi member (tambah/perbarui).
            
            Book class:
            •	__init__(title, author, isbn, available): Inisialisasi buku dengan propertinya.
            •	__repr__(): Representasi string dari buku.
            •	set_availability(is_available): Mengatur ketersediaan buku.
            •	print_log(): Prints informasi buku.
            
            Member class:
            •	__init__(name, member_id): Menginisialisasi member dengan propertinya.
            •	borrow_book(book): Membuat member bisa meminjam buku.
            •	return_book(book): Membuat member bisa mengembalikan buku.
            •	print_log(): Prints informasi anggota.
            
          Relationships:
          •	Library and Book: Perpustakaan berisi banyak buku, dikelola melalui metode seperti add_book, get_all_books, dan search_books.
          •	Library dan Member: Perpustakaan berisi banyak anggota, dikelola melalui metode seperti add_member dan manage_member_info.
          •	Member dan Book: Seorang anggota dapat meminjam banyak buku, dan satu buku dapat dipinjam oleh banyak anggota. Hubungan ini dikelola melalui                            metode seperti borrow_book dan return_book.
          Pada desain saya ini, kelas ‘Library’ bertindak sebagai pusat yang mengelola books dan member, sedangkan kelas ‘Book’ dan ‘Member’ mewakili entitas                 individu dalam sistem library. Program utama (‘main()’) berinteraksi dengan perpustakaan melalui pilihan menu yang disediakan untuk librarian dan                        member.

UML Diagrams

        User Roler (Actor): 
            -	User / Member (Pengguna)
            -	Librarian (Pustakawan)
            
        ![Use Case Diagram:](https://imgur.com/a/s2RhTGY)
        
        ![ Class Diagram:](https://imgur.com/a/VOaiZe8)


