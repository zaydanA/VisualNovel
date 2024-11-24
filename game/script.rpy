# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define arya = Character("Arya", color="#00008B",what_cps=2)
define bambang = Character("Bambang", color="#FFC0CB",what_cps=2) 
define bosbesar = Character("Bos Besar", color="#292929",what_cps=2) 
define kartika = Character("Kartika", color="#00ff4c",what_cps=2) 
define dhiyal = Character("Dhiyal", color="#cab600",what_cps=2) 
define tia = Character("Tia", color="#fdf7c1",what_cps=2) 
define ibuarya = Character("Ibu Arya", color="#0059ff",what_cps=2) 
define maya = Character("Maya", color="#0059ff",what_cps=2) 
define hendra = Character("Hendra", color="#6f00ff",what_cps=2) 

image aryanormal:
    "zeil normal.png"
    zoom 1.25
image aryasmile2:
    "zeil smile2.png"
    zoom 1.25
image aryasmile:
    "zeil smile.png"
    zoom 1.25
image aryamarah:
    "zeil angry.png"
    zoom 1.25
image aryabangga:
    "zeil delighted.png"
    zoom 1.25
image aryasedih:
    "zeil sad.png"
    zoom 1.25
image aryakaget:
    "zeil shocked.png"
    zoom 1.25
image aryasebel:
    "zeil annoyed.png"
    zoom 1.25
image aryanahansebel:
    "zeil annoyed.png"
    zoom 1.25
image bambang:
    "extra normal.png"
    zoom 1.25
image kartikanormal:
    "kartika normal.png"   
image pengusahanormal:
    "pengusaha normal.png"
    zoom 1.5
image dhiyalnormal:
    "dhiyal normal.png"
    zoom 1.75
image tianormal:
    "tia normal.png"
    zoom 1
image ibuaryanormal:
    "ibuarya normal.png"
    zoom 1.1 
image mayanormal:
    "maya normal.png"
    zoom 1.5
image hendranormal:
    "hendra normal.png"
    zoom 0.45
    
transform midleft:
    xpos 0.2  # Horizontal center (50% of the screen width)
    ypos 1.0  # Vertical center (50% of the screen height)
transform midright:
    xpos 0.8  # Horizontal center (50% of the screen width)
    ypos 1.0  # Vertical center (50% of the screen height)

# The game starts here.

label start:

    scene bg classroom

    # play sound "audio 1.mp3"

    show aryasmile with easeinleft

    play sound "dialog.mp3"
    # These display lines of dialogue.
    arya "Hari pertama sebagai PNS. Ayah selalu berpesan: 'Jabatan adalah amanah, bukan kesempatan.'"

    hide aryasmile    
    show aryabangga 
    
    play sound "dialog.mp3"
    arya "Aku akan membuktikan bahwa masih ada harapan untuk birokrasi yang bersih."

    hide aryabangga
    show aryasmile2
    play sound "dialog.mp3"
    arya "Sekalian membanggakan keluargaku, deh."


    hide aryasmile2
    show aryanormal
    play sound "dialog.mp3"
    # *melihat jam tangannya yang masih menunjukkan pukul 6.30*

    arya "Hmm.. masih ada 30 menit sebelum jam masuk kerja, sebaiknya ngapain ya?"

    menu:
        "Masuk lebih awal untuk mempelajari berkas-berkas":
            jump a2_1
        "Tunggu sebentar untuk mengamati lingkungan sekitar":
            jump a2_2
    return

label a2_1:

    hide aryanormal
    show aryasmile
    play sound "dialog.mp3"
    arya "Aku masuk lebih awal aja deh, sekalian liatin berkas-berkas"

    hide aryasmile

    scene bg gym with wipeleft

    show aryanormal at left with easeinleft

    $ renpy.pause(1)
    show bambang at right with moveinright

    play sound "dialog.mp3"
    bambang "Wah, si anak baru rajin sekali. Saya melihat potensi bagus dalam dirimu."
    play sound "dialog.mp3"
    bambang "Arya, di sini kamu akan belajar banyak. Tapi ingat, tidak semua pelajaran ada di buku panduan."
    play sound "dialog.mp3"
    bambang "Apakah kamu sudah mempelajari berkas-berkas itu untuk rapat nanti?"

    hide aryanormal
    show aryabangga at left
    play sound "dialog.mp3"
    arya "Sudah dong, Pak. Saya datang lebih awal untuk mempelajari berkas- berkas tersebut."
    play sound "dialog.mp3"
    arya "Saya ingin sekali membantu proyek ini."

    hide aryabangga
    show aryasmile at left
    play sound "dialog.mp3"
    bambang "Baiklah, nanti jangan lupa untuk ikut rapat, ya. Proyek ini adalah proyek yang cukup besar, jadi harus serius."


    play sound "dialog.mp3"
    arya "Baik, Pak."

    jump b1
    return

label a2_2:

    play sound "dialog.mp3"
    arya "Ah nanti aja, deh. Ngapain juga dateng awal."

    hide aryasmile

    scene bg gym with wipeleft

    show aryanormal at left

    $ renpy.pause(1)
    show bambang at right with moveinright

    hide aryanormal
    show aryasedih at left
    play sound "dialog.mp3"
    bambang "ARYA!!! Kenapa kamu datang telat sekali???? Malu-maluin pegawai lain aja."
    
    hide aryasedih
    show aryanormal at left
    play sound "dialog.mp3"
    bambang "Arya, di sini kamu akan belajar banyak. Tapi ingat, tidak semua pelajaran ada di buku panduan."
    
    play sound "dialog.mp3"
    bambang "Apakah kamu sudah mempelajari berkas-berkas itu untuk rapat nanti?"

    play sound "dialog.mp3"
    arya "S-sudah, Pak."

    play sound "dialog.mp3"
    bambang "Baiklah, nanti jangan lupa untuk ikut rapat, ya. Proyek ini adalah proyek yang cukup besar, jadi harus serius."

    play sound "dialog.mp3"
    arya "Baik, Pak."

    jump b1


label b1: 

    scene bg classroom with wipeleft

    # play sound "audio 1.mp3"

    show aryanormal at left
    show kartikanormal
    $ renpy.pause(1.5)

    show pengusahanormal at right with easeinright

    play sound "dialog.mp3"
    # These display lines of dialogue.
    bosbesar "Baik, untuk proyek kali ini akan ada kerja sama dengan berbagai pihak."
    play sound "dialog.mp3"
    bosbesar "Jika membutuhkan diskusi lebih lanjut, dipersilahkan. Yang paling penting, target mingguan harus tercapai."

    play sound "dialog.mp3"
    arya "Baik, Pak."

    hide pengusahanormal with easeoutright
    play sound "dialog.mp3"
    kartika "Mas Arya, mungkin kita bisa diskusi lebih lanjut tentang proyek ini sambil makan malam?"

    menu:
        "Menerima ajakan":
            jump c3_1
        "Menolak secara halus":
            jump c3_2

label c3_1:
    
    hide aryanormal
    show aryasmile at left
    play sound "dialog.mp3"
    arya "Wah, boleh aja. Mau jalan bareng ke sana juga?"

    play sound "dialog.mp3"
    kartika "Boleh, Mas."
    
    arya "*handphone Arya berdering*"
    play sound "dialog.mp3"
    kartika "Oh iya, Mas memangnya lagi engga ada urusan ya habis ini?"

    play sound "dialog.mp3"
    arya "Engga, kok.  Barusan itu ada telepon dari nomor yang tidak dikenal, kok. Jangan khawatir."

    play sound "dialog.mp3"
    kartika "Oke Mas, sebentar ya aku ke toilet dulu."
    hide kartikanormal with easeoutright
    $ renpy.pause(1.5)
    show dhiyalnormal at right with easeinright
    play sound "dialog.mp3"
    dhiyal "Arya! Makanan, makanan apa yang kalau dimakan bikin dosa?"

    play sound "dialog.mp3"
    arya "Waduh apa tuh Yal?"

    menu:
        "Sate Kelinci":
            play sound "dialog.mp3"
        "Makanan basi":
            play sound "dialog.mp3"
        "Makan berdua sama Kartika":
            play sound "dialog.mp3"

    dhiyal "Makan berdua sama Mba Kartika lah, kamu kan punya istri, gimana sih!"

    hide aryasmile
    show aryasebel at left
    play sound "dialog.mp3"
    arya "Apaansih Yal, Orang saya mau bahas kerjaan doang, gak ada sangkut pautnya sama istri saya."

    play sound "dialog.mp3"
    dhiyal "Arya, saya kasih tau ya, pikir dua kali kalau mau apa-apa."

    play sound "dialog.mp3"
    dhiyal "Mba Kartika itu jagonya menghasut orang buat yang ngga ngga."

    play sound "dialog.mp3"
    arya "Ah ngawur nih Pak Dhiyal, saya gak akan aneh aneh kok."

    play sound "dialog.mp3"
    dhiyal "Udah intinya saya mau kasih warning aja, Mba Kartika bisa bawa pengaruh buruk kalau kamu gak hati-hati."


    hide dhiyalnormal with easeoutright
    jump c4_2

label c3_2:

    hide aryanormal
    show aryasmile2 at left
    play sound "dialog.mp3"
    arya "Aduh, maaf banget. Saya ada urusan lain habis ini, Mba Kartika."
    play sound "dialog.mp3"
    arya "Saya pamit duluan ya. Kita bahas besok pada saat jam kerja saja."

    play sound "dialog.mp3"
    kartika "Oke, Mas. Semangat yaa."
    
    jump c4_1

label c4_2:
    scene bg gym with wipeleft
    $ renpy.pause(1)
    show aryanormal at left with easeinleft
    $ renpy.pause(0.5)
    show tianormal at right with easeinright
    play sound "dialog.mp3"
    hide aryanormal
    show aryakaget at left
    tia "Ya, kamu tuh dari mana aja sih?! Ditelepon berkali-kali gak diangkat!"

    hide aryakaget
    show aryanormal at left
    play sound "dialog.mp3"
    arya "Maaf sayang.. tadi ada meeting yang serius jadi aku silent hp aku, kenapa telepon aku sampe berkali-kali gitu?"

    play sound "dialog.mp3"
    tia "Aduh kamu tuh ya, ga habis pikir aku."
    play sound "dialog.mp3"
    tia "Kata dokter, Ibu kena diabetes Ya, butuh pengobatan secepatnya sebelum makin parah."

    hide aryanormal
    show aryakaget at left
    play sound "dialog.mp3"
    arya "Hah yang bener!? Terus Ibu gimana sekarang?"

    play sound "dialog.mp3"
    tia "Tadi pertama denger Ibu shock berat dan langsung lemes gitu."
    tia "Aku gak tega banget lihatnya, tapi udah aku coba tenangin dan Ibu di kamar sekarang, nungguin kamu."

    jump c5

label c4_1:
    hide kartikanormal with easeoutright
    hide aryasmile2
    show aryasmile at left
    show aryasmile at midleft with move

    play sound "dialog.mp3"
    arya "Halo sayang, kenapa tiba-tiba nelpon?"

    show tianormal at right with easeinright
    play sound "dialog.mp3"
    tia "Ibu kamu sayang, dia tadi pagi tiba-tiba pusing"

    play sound "dialog.mp3"
    arya "Sayang, ibu sakit apa?"

    show tianormal at midright with move
    play sound "dialog.mp3"
    tia "Tadi sore kan aku ke rumah sakit bareng Ibu buat ngambil hasil tes kesehatan Ibu."
    tia "Setelah dicek kata dokternya Ibu kena diabetes, Ya"

    hide aryasmile
    show aryakaget at left 
    show aryakaget at midleft 
    play sound "dialog.mp3"
    arya "Hah yang bener!? Terus Ibu gimana sekarang?"


    play sound "dialog.mp3"
    tia "Tadi pertama denger Ibu shock berat dan langsung lemes gitu."
    tia "Aku gak tega banget lihatnya, tapi udah aku coba tenangin dan Ibu di kamar sekarang, nungguin kamu."

    jump c5

label c5:

    scene bg classroom with wipeleft
    show ibuaryanormal at left
    $ renpy.pause(1)
    show aryasedih at right with easeinright

    play sound "dialog.mp3"
    arya "Bu, maaf Arya baru pulang, Arya sudah dengar dari Tia bu, Ibu gapapa?"

    play sound "dialog.mp3"
    ibuarya "Ibu nggak apa-apa, hanya kaget saja dan jadi gelisah."

    play sound "dialog.mp3"
    arya "Kata dokternya gimana Bu? Kapan pengobatannya bisa dimulai?"

    hide aryasedih
    show aryanormal at right
    play sound "dialog.mp3"
    ibuarya "Segera setelah Ibu mendaftar dan biaya pengobatannya dibayar Nak, dokternya bilang harus secepatnya…"

    play sound "dialog.mp3"
    ibuarya "Nak, maaf ibu jadi beban buat kamu dan Tia."
    play sound "dialog.mp3"
    ibuarya "Seharusnya dengan posisimu sekarang Ibu gak perlu nambah beban kamu untuk mengeluarkan uang lagi.."

    hide aryanormal
    show aryasmile at right
    play sound "dialog.mp3"
    arya "Ngga apa apa bu, Arya bisa membiayai pengobatan ibu kok, Ibu tenang aja ya biar Arya urus semuanya."

    menu:
        "Mencari pinjaman legal":
            jump c5_1
        "Menerima tawaran 'bantuan' dari Hendra":
            jump c5_2
        "Mencari penghasilan tambahan yang legal":
            jump c5_3

label c5_1:
    scene bg gym with wipeleft
    show aryanahansebel at left

    play sound "dialog.mp3"
    arya "Aduh, apa aku pinjem uang dulu ya, ke siapa ya enaknya."    

    hide aryanahansebel
    show aryanormal at left
    show mayanormal at right with easeinright
    play sound "dialog.mp3"
    arya "Halo Maya, maaf telepon kamu malem-malem gini, kamu lagi sibuk nggak? Aku mau minta tolong.."    

    play sound "dialog.mp3"
    maya "Halo Arya, kamu mau minta tolong apaan emangnya? Pasti aku coba bantu kok."

    hide aryanormal
    show aryasmile at left
    play sound "dialog.mp3"
    arya "Anu May… Ibuku tadi sore didiagnosis kena Diabetes, aku harus cepet-cepet bayar biaya pengobatannya."    
    hide aryasmile
    show aryasedih at left
    play sound "dialog.mp3"
    arya "Aku sama Tia lagi gak punya cukup uang karena akupun baru dapat kerja, jadi…"    

    play sound "dialog.mp3"
    maya "Oh butuh pinjaman uang, Ya?"

    play sound "dialog.mp3"
    arya "Iya May… Aduh aku tuh sebenernya gak enak banget sama kamu."
    play sound "dialog.mp3"
    arya "aku bingung harus minta tolong siapa lagi.."

    play sound "dialog.mp3"
    maya "Boleh aja sih, Ya, nanti kamu chat aja perlu berapa dan nomor rekening kamu berapa yaa."

    play sound "dialog.mp3"
    arya "Serius, May? Gapapa kah? Maaf banget ya, May"
    
    play sound "dialog.mp3"
    maya "Iya gapapa lah Ya kayak baru kenal aja, aku gak tega juga sama Ibu kamu, semoga Ibu kamu cepet sembuh ya."
    
    hide aryasedih
    show aryasmile at left
    play sound "dialog.mp3"
    arya "Aduh May makasih banyak ya, nanti aku sampaikan salammu ke Ibu."
    
    jump d1

label c5_2:
    scene bg gym with wipeleft
    show aryanormal at left
    $ renpy.pause(1)
    show hendranormal at right with easeinright

    play sound "dialog.mp3"
    hendra "Masih pagi udah loyo aja nih, ada apa Arya?"

    hide aryanormal
    show aryasmile2 at left
    play sound "dialog.mp3"
    arya "Eh Pak Hendra, nggak ada apa-apa pak, lagi banyak pikiran saja haha"

    play sound "dialog.mp3"
    hendra "Waduh berat tuh kayaknya, sini Ya ikut ke ruangan saya sebentar"

    hide aryasmile2
    show aryasmile at left
    play sound "dialog.mp3"
    arya "Eh gapapa Pak, aman kok Pak"

    show bg classroom with wipeleft

    hide aryasmile
    show aryanormal at left
    play sound "dialog.mp3"
    hendra "Jadi ada apa sih, coba cerita ke saya, masalah pekerjaan?"

    play sound "dialog.mp3"
    arya "Bukan kok Pak, masalah rumah saja."

    play sound "dialog.mp3"
    hendra "Nih saya kasih tau, masalah rumah biasanya bisa sangat mengganggu pekerjaan."
    play sound "dialog.mp3"
    hendra "Saya gak mau bawahan bawahan saya kinerjanya terganggu."

    play sound "dialog.mp3"
    arya "(ngomong dalam hati) Apa ini kesempatanku untuk minta bantuan Pak Hendra terkait masalah Ibu ya?"

    play sound "dialog.mp3"
    hendra "Gimana Ya? Apa masih gak mau cerita?"

    play sound "dialog.mp3"
    arya "Sebenarnya gini Pak, Ibu saya kemarin didiagnosa terkena Diabetes, dan saya lagi cukup kesulitan…"

    play sound "dialog.mp3"
    hendra "Kesulitan dalam masalah uang?"

    play sound "dialog.mp3"
    arya "Iya kurang lebih begitu pak, masalahnya uangnya dibutuhkan secepatnya."

    play sound "dialog.mp3"
    hendra "Gimana kalau saya bilang saya bisa bantu kamu?"

    play sound "dialog.mp3"
    arya "Aduh nggak deh pak saya gak berani minjam-minjam uang ke atasan."

    play sound "dialog.mp3"
    hendra "Siapa bilang pinjamnya ke saya?"

    play sound "dialog.mp3"
    hendra "(bisik-bisik) Pinjam ke kantor"

    play sound "dialog.mp3"
    arya "Aduh pak nggak deh pak, saya gak berani."

    play sound "dialog.mp3"
    hendra "Kamu mau masalah kamu cepat selesai tidak? Saya yakin ibumu juga butuh diobati secepatnya."

    play sound "dialog.mp3"
    hendra "Saya bukannya mau gimana-gimana, hanya mau membantu cari jalan kok."

    play sound "dialog.mp3"
    arya "Ta…tapi saya gak tahu caranya Pak, saya malu juga kalau satu kantor tahu kelakuan saya si pegawai baru ini."

    play sound "dialog.mp3"
    hendra "Satu kantor gak perlu tahu Ya, bahkan cukup kamu dan saya saja yang tahu, saya bisa bantu kok agar rapih dan bersih."

    play sound "dialog.mp3"
    hendra "Ayo Ya, demi Ibumu."

    play sound "dialog.mp3"
    arya "Jadi apa yang perlu saya lakukan Pak?"

    play sound "dialog.mp3"
    hendra "Nanti jam 4 sore kamu datang lagi ke ruangan ini, kita bicarakan semuanya."

    play sound "dialog.mp3"
    arya "Baik pak, terimakasih banyak Pak Hendra untuk bantuannya."

    hide hendranormal with easeoutright

    scene bg gym
    
    show aryanormal at left with easeinleft
    $ renpy.pause(0.5)
    show dhiyalnormal at right with easeinright

    play sound "dialog.mp3"
    dhiyal "Ya, habis diapain sama Pak Hendra?"

    play sound "dialog.mp3"
    arya "Ngga diapa-apain, justru saya yang minta tolong Pak Hendra."

    play sound "dialog.mp3"
    dhiyal "Curiga nih saya, minta tolong apaan tuh?"

    play sound "dialog.mp3"
    arya "Ah ada deh pokoknya Yal."

    play sound "dialog.mp3"
    dhiyal "Waduh, coba tebak, bahasa indonesianya dari kata Criminal apa coba?"

    hide aryanormal
    show aryanahansebel at left
    play sound "dialog.mp3"
    arya "Aduh Pak saya lagi pusing, gak mood buat tebak-tebakan."

    menu:
        "Penjahit":
            play sound "dialog.mp3"
        "Pemahat":
            play sound "dialog.mp3"
        "Pak Hendra":
            play sound "dialog.mp3"
    
    dhiyal "Jawabannya Pak Hendra! Kalau urusannya sama Pak Hendra saya yakin dia ngajak kamu main kotor kan?"

    play sound "dialog.mp3"
    arya "Eh apaan sih ngga kok, jangan mikir aneh-aneh gitu ah Yal."

    play sound "dialog.mp3"
    dhiyal "Saya tau kok track record kelakuan-kelakuan Pak Hendra seperti apa."
    
    play sound "dialog.mp3"
    dhiyal "Awas Arya, main kotor ga akan berkah untuk kamu dan masa depanmu."

    hide aryanahansebel
    show aryanormal at left

    jump d1
    

label c5_3:
    scene bg room with wipeleft
    show aryanormal at left
    $ renpy.pause(1)
    show tianormal at right with easeinright

    play sound "dialog.mp3"
    tia "Jadi gimana Ya? Apa kita punya uang buat bayar pengobatan Ibu? Biayanya gak murah loh Ya."

    play sound "dialog.mp3"
    arya "Aku juga bingung Ti, padahal uang kita pas-pasan banget buat biaya kehidupan sehari-hari."

    play sound "dialog.mp3"
    tia "Gimana kalau kita pinjem aja? Aku gak tega liat Ibu."

    play sound "dialog.mp3"
    arya "Tapi pinjem ke siapa Ti, aku gak tenang ah pinjem pinjem uang gitu."
    play sound "dialog.mp3"
    arya "Apa aku jual aja laptop aku ya?"

    play sound "dialog.mp3"
    tia "Eh tapi nanti kerjaan kamu gimana, Ya?"

    play sound "dialog.mp3"
    arya "Aku bisa pake komputer kantor aja dulu sementara."

    play sound "dialog.mp3"
    arya "Tapi itu berarti aku terpaksa lebih sering di kantor karena gaada laptop di rumah, gapapa kan Ti"

    play sound "dialog.mp3"
    tia "Eh ya itu terserah kamu Ya, aku bakal dukung keputusan kamu."

    play sound "dialog.mp3"
    tia "kalau kamu beneran mau jual laptopnya aku bakal bantu sebarin ke temen-temenku, siapa tau ada yang tertarik."

    play sound "dialog.mp3"
    arya "Makasih ya sayang, iya kayaknya aku bakal jual aja deh."

    jump d1

label d1:
    scene bg classroom with wipeleft
    show aryanormal at left with easeinleft
    $ renpy.pause(1)
    show hendranormal at right with easeinright

    play sound "dialog.mp3"
    hendra "Anak muda, kamu pintar. Sayang kalau karir bagusmu harus berakhir cepat. Mari kita bicarakan dengan kepala dingin."

    menu:
        "Laporkan ke KPK":
            jump d1_1
        "Terima suap":
            jump d1_2
        "Cari bukti lebih banyak":
            jump d1_3

label d1_1:
    play sound "dialog.mp3"
    hendra "Dengar baik baik nak, saya bisa membantu kamu naik jabatan dengan cepat dan mudah."
    play sound "dialog.mp3"
    hendra "Ignorance is bliss. Kita lewati saja ini dengan rapi ya?"
    
    play sound "dialog.mp3"
    arya "Baik pak."
    hide hendranormal with easeoutright
    hide aryanormal with easeoutleft
    
    scene bg room with wipeleft

    show aryanormal at left with easeinleft
    $ renpy.pause(1)
    show tianormal at right with easeinright
    
    play sound "dialog.mp3"
    tia "Kamu gapapa, sayang? Gimana di kantor hari ini?"
    
    play sound "dialog.mp3"
    arya "… Pak Hendra korupsi. Aku gak tenang, Ti. Aku mau lapor ke KPK."
    
    play sound "dialog.mp3"
    arya "Kamu yakin? Kamu butuh bukti yang cukup, Ya. Itu jalan yang berbahaya banget."
    
    play sound "dialog.mp3"
    tia "Ibu kamu lagi sakit, kamu gak usah bawa bawa masalah lain lagi.. Kita fokus ke Ibu dulu aja ya?"
    
    play sound "dialog.mp3"
    arya "Justru karena itu aku gak tenang kerja… Aku mau selesain masalah ini sebelum aku kebawa-bawa."

    play sound "dialog.mp3"
    arya "(Keesokan harinya Arya membawa dokumen tersebut ke kantor KPK)"

label d1_2:
    hide hendranormal with easeoutright
    hide aryanormal with easeoutleft
    
    scene bg room with wipeleft

    show aryanormal at left with easeinleft
    $ renpy.pause(1)
    show tianormal at right with easeinright
    
    play sound "dialog.mp3"
    tia "Sayang, kamu sakit? Kenapa muka kamu pucet banget?"
    
    play sound "dialog.mp3"
    arya "Aku kebingungan.."
    
    play sound "dialog.mp3"
    tia"Masalah kerja ya? Kamu kan selalu cerita sama aku.. Kali ini juga gapapa, cerita aja."
    
    play sound "dialog.mp3"
    arya "Aku nemuin kasus, Tia, kasus besar Pak Hendra."
    
    play sound "dialog.mp3"
    tia "(Melihat Arya dengan wajah khawatir dan bingung)"

    play sound "dialog.mp3"
    arya "Aku harus ngelaporin ini, aku tau. Tapi aku harus bicara dulu dengan Pak Hendra atau engga ya, Ti? Aku bingung…"

    play sound "dialog.mp3"
    tia "(Berpikir sejenak) Apapun itu, kamu harus tetap berada di jalan yang benar ya, sayang?"

    scene bg classroom with wipeleft

    show hendranormal at left
    $ renpy.pause(1)
    show aryanormal at right with easeinright

    play sound "dialog.mp3"
    hendra "Anak muda, kamu pintar. Sayang kalau karir bagusmu harus berakhir cepat. Mari kita bicarakan dengan kepala dingin."
    play sound "dialog.mp3"
    hendra "Dengar baik baik nak, saya bisa membantu kamu naik jabatan dengan cepat dan mudah."
    play sound "dialog.mp3"
    hendra "Ignorance is bliss. Kita lewati saja ini dengan rapi ya?"
    
    play sound "dialog.mp3"
    arya "Baik pak."
    $ renpy.pause(1)
    play sound "dialog.mp3"
    arya "Untungnya bagi saya, pak?"

    play sound "dialog.mp3"
    hendra "(Terbahak-bahak seram)"

    play sound "dialog.mp3"
    arya "Saya butuh pak. Bukan bapak saja."

    play sound "dialog.mp3"
    hendra "(Tertawa perlahan) Tentu saja. Brilian. Kamu ingin berapa? 5x 10x dari biaya pengobatan ibu kamu?"

    play sound "dialog.mp3"
    arya "S-saya.."

    play sound "dialog.mp3"
    hendra "Tidak ada yang terjadi di kantor ini yang saya tidak ketahui tentu saja, Arya. Masalah uang, gampang."

    play sound "dialog.mp3"
    hendra "Kamu serahkan pada saya. Aman… selama kamu (menaikkan tangannya ke mulut membuat isyarat 'diam')"

    play sound "dialog.mp3"
    arya "(Mengangguk pelan)"

    scene bg rooftop with wipeleft

    show dhiyalnormal at left 
    $ renpy.pause(1.0)
    show aryanormal at right with easeinright

    play sound "dialog.mp3"
    arya "Yal, saya-(omongannya dipotong Dhiyal)"

    play sound "dialog.mp3"
    dhiyal "Arya, kamu paham gak sih ketika kita menolak korupsi itu artinya kita memilih untuk jadi bagian dari solusi, sesimpel itu."

    play sound "dialog.mp3"
    dhiyal " Koruptor-koruptor kadang gak mikirin perasaan keluarga dan teman-teman mereka yang kecewa kalau tau yang sebenarnya."

    play sound "dialog.mp3"
    dhiyal "Korupsi menghancurkan keadilan dan merampas hak-hak rakyat, Ya. Saya miris sekali melihat negara ini banyak sekali koruptornya."

    play sound "dialog.mp3"
    dhiyal "Ayo Arya kita seharusnya bisa lebih bijak."

label d1_3:

    scene bg gym with wipeleft
    show kartikanormal at left
    $ renpy.pause(0.5)
    show aryamarah at right with easeinright 
    
    play sound "dialog.mp3"
    arya "Aku tahu Kar, apa yang kamu lakukan dengan Pak Hendra."

    play sound "dialog.mp3"
    kartika "M-maksud kamu apa, Arya?"

    play sound "dialog.mp3"
    arya "(Memosisikan badan dengan tegap) Tender itu, aku tahu."

    play sound "dialog.mp3"
    kartika "(Menunduk dan perlahan menangis)"

    play sound "dialog.mp3"
    arya "Kamu sendiri yang setuju, Kartika. Nangis gak ada gunanya sekarang."

    play sound "dialog.mp3"
    kartika "A-apa yang h-harus aku lakukan sekarang, Arya?"

    play sound "dialog.mp3"
    arya "Kamu serahkan kasus-kasus Pak Hendra yang lain, Kar. Aku akan coba bantu memperbaiki nama baik kamu."

    play sound "dialog.mp3"
    kartika "Benarkah, A-arya?"

    play sound "dialog.mp3"
    arya "(Mengangguk yakin)"

    play sound "dialog.mp3"
    kartika "M-maksud kamu apa, Arya?"

    play sound "dialog.mp3"
    arya "Aku tahu Kar, apa yang kamu lakukan dengan Pak Hendra."

    play sound "dialog.mp3"
    kartika "M-maksud kamu apa, Arya?"