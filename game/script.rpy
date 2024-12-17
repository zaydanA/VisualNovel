# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define arya = Character("Arya", color="#ffffff",what_cps=2)
define bambang = Character("Bambang", color="#ffffff",what_cps=2) 
define bosbesar = Character("Bos Besar", color="#ffffff",what_cps=2) 
define kartika = Character("Kartika", color="#ffffff",what_cps=2) 
define dhiyal = Character("Dhiyal", color="#ffffff",what_cps=2) 
define tia = Character("Tia", color="#ffffff",what_cps=2) 
define ibuarya = Character("Ibu Arya", color="#ffffff",what_cps=2) 
define maya = Character("Maya", color="#ffffff",what_cps=2) 
define hendra = Character("Hendra", color="#ffffff",what_cps=2) 
define petugas = Character("Petugas", color="#ffffff",what_cps=2) 
define gubernur = Character("Gubernur", color="#ffffff",what_cps=2) 
define telepon = Character("TELEPON", color="#ffffff",what_cps=2) 
define pegawai1 = Character("Pegawai 1", color="#ffffff",what_cps=2) 
define pegawai2 = Character("Pegawai 2", color="#ffffff",what_cps=2) 

image aryanormal:
    "arya normal.png"
    zoom 0.3
image aryasmile:
    "arya smile.png"
    zoom 0.3
image aryapanik:
    "arya panik.png"
    zoom 0.3
image aryamarah:
    "arya marah.png"
    zoom 0.3
image aryasedih:
    "arya sedih.png"
    zoom 0.3
image aryasmile2:
    "arya smile2.png"
    zoom 0.3
image aryabingung:
    "arya bingung.png"
    zoom 0.3
image aryanelpon:
    "arya nelpon.png"
    zoom 0.3
image bambangnormal:
    "bambang normal.png"
    zoom 0.6
image bambangsenang:
    "bambang senang.png"
    zoom 0.6
image bambangmarah:
    "bambang marah.png"
    zoom 0.6
image bosbesarnormal:
    "bosbesar normal.png"
    zoom 0.3
image dhiyaltebak:
    "dhiyaltebak.png"
    zoom 0.3
    xzoom -1.0 
image dhiyalmarah:
    "dhiyalmarah.png"
    zoom 0.3
    xzoom -1.0 
image tabiranormal:
    "tabira.png"
    zoom 0.3
    xpos 0.8 
    xzoom -1.0 
image dhiyalcuriga:
    "dhiyal curiga.png"
    zoom 0.3
    xzoom -1.0 
image tiamarah:
    "tia marah.png"
    zoom 0.3
image tiapanik:
    "tia panik.png"
    zoom 0.3
image tianelpon:
    "tia nelpon.png"
    zoom 0.3
image tiasedih:
    "tia sedih.png"
    zoom 0.3
image tiabangga:
    "tia bangga.png"
    zoom 0.3
image mayanormal:
    "maya normal.png"
    zoom 0.3
image mayakecewa:
    "maya kecewa.png"
    zoom 0.3
image mayanelpon:
    "maya nelpon.png"
    zoom 0.3
image mayamic:
    "maya mic.png"
    zoom 0.3
image kartikanormal:
    "kartika normal.png"   
    zoom 0.53
image kartikasenang:
    "kartika senang.png"   
    zoom 0.53
image kartikasexy:
    "kartika sexy.png"   
    zoom 0.53
image gubernurnormal:
    "gubernur normal.png"
    zoom 0.3
image petugaskpknormal:
    "petugaskpk normal.png"
    zoom 0.3
image ibuaryanormal:
    "ibuaryasedih.png"
    zoom 0.4
    xpos 0.8  # Posisi horizontal 80% dari lebar layar
    xzoom -1.0 
image ibuaryasenang:
    "ibuarya senang.png"
    zoom 0.4
    xpos 0.8  # Posisi horizontal 80% dari lebar layar
    xzoom -1.0 

image hendranormal:
    "hendra normal.png"
    zoom 0.33
    xzoom -1.0 
image hendrasenyumlicik:
    "hendra senyumlicik.png"
    zoom 0.33
    xzoom -1.0 
image hendraketawa:
    "hendra ketawa.png"
    zoom 0.33
    xzoom -1.0 

image pegawai1normal:
    "pegawai1 normal.png"
    zoom 1.5
image pegawai2normal:
    "pegawai2 normal.png"
    zoom 1.55

image teleponnormal:
    "telepon.png"
    zoom 1.85
    
image emojiflat:
    Animation(
        im.Scale("emojiflat/flat1.png", 200, 200), 0.2,
        im.Scale("emojiflat/flat2.png", 200, 200), 0.2
    )
    zoom 0.5  
    ypos 300  
    linear 2.0 zoom 1.0 ypos 200  # Scale up and move upward
    repeat
image emojisenang:
    Animation(
        im.Scale("emojisenang/senang_fixx_1.png", 200, 200), 0.2,
        im.Scale("emojisenang/senang_fixx_2.png", 200, 200), 0.2,
        im.Scale("emojisenang/senang_fixx_3.png", 200, 200), 0.2,
        im.Scale("emojisenang/senang_fixx_4.png", 200, 200), 0.2,
        im.Scale("emojisenang/senang_fixx_5.png", 200, 200), 0.2,
        im.Scale("emojisenang/senang_fixx_6.png", 200, 200), 0.2,
    )
    zoom 0.5  
    ypos 300 
    linear 2.0 zoom 1.0 ypos 200  # Scale up and move upward
    repeat
image emojihatidegdeg:
    Animation(
        im.Scale("emojihatidegdeg/hati degdeg fix1.png", 300, 300), 0.2,
        im.Scale("emojihatidegdeg/hati degdeg fix2.png", 300, 300), 0.2
    )
    zoom 0.5 
    ypos 300 
    linear 2.0 zoom 1.0 ypos 200  # Scale up and move upward
    repeat
image emojimarah:
    Animation(
        im.Scale("emojimarah/marah_1.png", 200, 200), 0.2,
        im.Scale("emojimarah/marah_2.png", 200, 200), 0.2,
        im.Scale("emojimarah/marah_3.png", 200, 200), 0.2,
        im.Scale("emojimarah/marah_4.png", 200, 200), 0.2,
        im.Scale("emojimarah/marah_5.png", 200, 200), 0.2,
        im.Scale("emojimarah/marah_6.png", 200, 200), 0.2,
        im.Scale("emojimarah/marah_7.png", 200, 200), 0.2,
        im.Scale("emojimarah/marah_8.png", 200, 200), 0.2,
    )
    zoom 0.5 
    ypos 300  
    linear 2.0 zoom 1.0 ypos 200  # Scale up and move upward
    repeat
image emojisedih:
    Animation(
        im.Scale("emojisedih/sedih1.png", 200, 200), 0.2,
        im.Scale("emojisedih/sedih2.png", 200, 200), 0.2,
        im.Scale("emojisedih/sedih3.png", 200, 200), 0.2,
        im.Scale("emojisedih/sedih4.png", 200, 200), 0.2,

    )
    zoom 0.5 
    ypos 300 
    linear 2.0 zoom 1.0 ypos 200  # Scale up and move upward
    repeat
image emojipatahhati:
    Animation(
        im.Scale("emojipatahhati/patah hati fix 1.png", 300, 300), 0.2,
        im.Scale("emojipatahhati/patah hati fix 2.png", 300, 300), 0.2,
        im.Scale("emojipatahhati/patah hati fix 3.png", 300, 300), 0.2,
        im.Scale("emojipatahhati/patah hati fix 4.png", 300, 300), 0.2,
        im.Scale("emojipatahhati/patah hati fix 5.png", 300, 300), 0.2,
    )
    zoom 0.5 
    ypos 300 
    linear 2.0 zoom 1.0 ypos 200  # Scale up and move upward
    repeat

transform midleft:
    xpos 0.2  
    ypos 1.0  
transform midright:
    xpos 0.8  
    ypos 1.0  

# The game starts here.
label start:
    show screen custom_game_menu_button
    scene bg depankantor
    play music "Lagu KWN Scene 1 Original.mp3" fadein 2 fadeout 2
    play sound "dialog.mp3"
    # play sound "audio 1.mp3"
    show aryasmile with easeinleft


    play sound "dialog.mp3"

    arya "Hari pertama sebagai PNS. Ayah selalu berpesan: 'Jabatan adalah amanah, bukan kesempatan.'"

    
    play sound "dialog.mp3"
    arya "Aku akan membuktikan bahwa masih ada harapan untuk birokrasi yang bersih."

    play sound "dialog.mp3"
    arya "Sekalian membanggakan keluargaku, deh."


    hide aryasmile2
    show aryanormal
    play sound "dialog.mp3"


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
    show emojisenang 
    play sound "dialog.mp3"
    arya "Aku masuk lebih awal aja deh, sekalian liatin berkas-berkas"



    scene bg kantorkeroco with wipeleft

    show aryanormal at left with easeinleft

    hide aryasmile

    play music "Lagu KWN Scene 2 HIJAU Original.mp3" fadein 2 fadeout 2
    $ renpy.pause(1)
    show bambangsenang at right with moveinright
    show emojisenang at Position(xpos=0.81, ypos=0.20)

    play sound "dialog.mp3"
    bambang "Wah, si anak baru rajin sekali. Saya melihat potensi bagus dalam dirimu."
    play sound "dialog.mp3"
    bambang "Arya, di sini kamu akan belajar banyak. Tapi ingat, tidak semua pelajaran ada di buku panduan."

    hide bambangsenang
    show bambangnormal at right
    play sound "dialog.mp3"
    bambang "Apakah kamu sudah mempelajari berkas-berkas itu untuk rapat nanti?"

    hide aryanormal
    show aryasmile at left
    play sound "dialog.mp3"
    arya "Sudah dong, Pak. Saya datang lebih awal untuk mempelajari berkas- berkas tersebut."
    play sound "dialog.mp3"
    arya "Saya ingin sekali membantu proyek ini."

    show aryasmile at left
    play sound "dialog.mp3"
    bambang "Baiklah, nanti jangan lupa untuk ikut rapat, ya. Proyek ini adalah proyek yang cukup besar, jadi harus serius."


    play sound "dialog.mp3"
    arya "Baik, Pak."

    jump b1
    return

label a2_2:
    
    show emojiflat 
    play sound "dialog.mp3"
    arya "Ah nanti aja, deh. Ngapain juga dateng awal."


    scene bg kantorkeroco with wipeleft

    show aryanormal at left

    play music "Lagu KWN Scene 2 MERAH Original.mp3" fadein 2 fadeout 2
    $ renpy.pause(1)

    show bambangmarah at right with moveinright

    show emojimarah at Position(xpos=0.81, ypos=0.20)
    play sound "dialog.mp3"
    hide aryanormal
    show aryapanik at left
    bambang "ARYA!!! Kenapa kamu datang telat sekali???? Malu-maluin pegawai lain aja."
    
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

    scene bg ruangrapat with wipeleft

    show kartikanormal with easeinright
    show aryanormal at left with easeinleft
    $ renpy.pause(1.5)

    show bosbesarnormal at right with easeinright

    play sound "dialog.mp3"

    bosbesar "Baik, untuk proyek kali ini akan ada kerja sama dengan berbagai pihak."
    play sound "dialog.mp3"
    bosbesar "Jika membutuhkan diskusi lebih lanjut, dipersilahkan. Yang paling penting, target mingguan harus tercapai."

    play sound "dialog.mp3"
    arya "Baik, Pak."

    hide bosbesarnormal with easeoutright

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
    show emojisenang at Position(xpos=0.2, ypos=0.25)
    
    play sound "dialog.mp3"
    arya "Wah, boleh aja. Mau jalan bareng ke sana juga?"
    

    play sound "dialog.mp3"
    kartika "Boleh, Mas."
    
    arya "*handphone Arya berdering*"
    play sound "dialog.mp3"
    kartika "Oh iya, Mas memangnya lagi engga ada urusan ya habis ini?"

    play sound "dialog.mp3"
    arya "Engga, kok.  Barusan itu ada telepon dari nomor yang tidak dikenal, kok. Jangan khawatir."


    hide kartikanormal
    show kartikasexy 
    show emojihatidegdeg at Position(xpos=0.5, ypos=0.35)
    play sound "dialog.mp3"
    kartika "Oke Mas, sebentar ya aku ke toilet dulu."
    
    hide emojisenang
    hide emojihatidegdeg
    hide kartikasexy with easeoutright
    $ renpy.pause(1.5)
    hide aryasmile
    show aryanormal at left
    show dhiyaltebak at right with easeinright
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

    hide dhiyaltebak
    show emojimarah at Position(xpos=0.2, ypos=0.25)
    show dhiyalmarah at right
    dhiyal "Makan berdua sama Mba Kartika lah, kamu kan punya istri, gimana sih!"

    hide aryanormal
    show aryamarah at left


    play sound "dialog.mp3"
    arya "Apaansih Yal, Orang saya mau bahas kerjaan doang, gak ada sangkut pautnya sama istri saya."

    hide dhiyalmarah with easeoutright
    play sound "dialog.mp3"
    show dhiyalmarah at center with easeinright
    show tabiranormal with easeinright
    dhiyal "Arya, saya kasih tau ya, pikir dua kali kalau mau apa-apa."

    play sound "dialog.mp3"
    dhiyal "Mba Kartika itu jagonya menghasut orang buat yang ngga ngga."

    play sound "dialog.mp3"
    arya "Ah ngawur nih Pak Dhiyal, saya gak akan aneh aneh kok."

    play sound "dialog.mp3"
    dhiyal "Udah intinya saya mau kasih warning aja, Mba Kartika bisa bawa pengaruh buruk kalau kamu gak hati-hati."


    hide dhiyalcuriga with easeoutright
    jump c4_2

label c3_2:

    show emojiflat at Position(xpos=0.2, ypos=0.25)
    hide aryanormal
    show aryasmile2 at left
    play music "Lagu KWN Scene 3 Original.mp3" fadein 2 fadeout 2
    play sound "dialog.mp3"
    arya "Aduh, maaf banget. Saya ada urusan lain habis ini, Mba Kartika."
    play sound "dialog.mp3"
    arya "Saya pamit duluan ya. Kita bahas besok pada saat jam kerja saja."

    hide kartikanormal
    show kartikasexy 
    show emojihatidegdeg at Position(xpos=0.5, ypos=0.35)
    play sound "dialog.mp3"
    kartika "Oke, Mas. Semangat yaa."
    
    hide emojiflat
    hide emojihatidegdeg

    hide kartikasexy with easeoutright
    jump c4_1

label c4_2:
    scene bg rumahmalam with wipeleft
    $ renpy.pause(1)
    show aryanormal at left with easeinleft
    $ renpy.pause(0.5)
    show tiamarah at right with easeinright
    play sound "dialog.mp3"
    hide aryanormal
    show aryapanik at left
    tia "Ya, kamu tuh dari mana aja sih?! Ditelepon berkali-kali gak diangkat!"


    hide aryapanik
    show aryasedih at left
    play sound "dialog.mp3"
    arya "Maaf sayang.. tadi ada meeting yang serius jadi aku silent hp aku, kenapa telepon aku sampe berkali-kali gitu?"
    play sound "dialog.mp3"
    tia "Aduh kamu tuh ya, ga habis pikir aku."
    play sound "dialog.mp3"
    tia "Kata dokter, Ibu kena diabetes Ya, butuh pengobatan secepatnya sebelum makin parah."

    hide aryasedih
    show aryapanik at left
    play sound "dialog.mp3"
    arya "Hah yang bener!? Terus Ibu gimana sekarang?"

    hide tiamarah
    show tiapanik at right
    play sound "dialog.mp3"
    tia "Tadi pertama denger Ibu shock berat dan langsung lemes gitu."
    tia "Aku gak tega banget lihatnya, tapi udah aku coba tenangin dan Ibu di kamar sekarang, nungguin kamu."

    jump c5

label c4_1:
    
    hide kartikanormal with easeoutright
    hide aryasmile2
    show aryanelpon at left
    show aryanelpon at midleft with move

    play sound "dialog.mp3"
    play music "Lagu KWN Scene 4 Original.mp3" fadein 2 fadeout 2
    arya "Halo sayang, kenapa tiba-tiba nelpon?"

    show tianelpon at right with easeinright
    play sound "dialog.mp3"
    tia "Ibu kamu sayang, dia tadi pagi tiba-tiba pusing"

    play sound "dialog.mp3"
    arya "Sayang, ibu sakit apa?"

    show tianelpon at midright with move
    play sound "dialog.mp3"
    tia "Tadi sore kan aku ke rumah sakit bareng Ibu buat ngambil hasil tes kesehatan Ibu."
    tia "Setelah dicek kata dokternya Ibu kena diabetes, Ya"

    hide aryanelpon
    show aryapanik at left 
    show aryapanik at midleft 
    play sound "dialog.mp3"
    arya "Hah yang bener!? Terus Ibu gimana sekarang?"


    play sound "dialog.mp3"
    tia "Tadi pertama denger Ibu shock berat dan langsung lemes gitu."
    tia "Aku gak tega banget lihatnya, tapi udah aku coba tenangin dan Ibu di kamar sekarang, nungguin kamu."

    jump c5

label c5:

    scene bg kamaribu with wipeleft
    show ibuaryanormal at right
    $ renpy.pause(1)
    show aryasedih at left with easeinleft

    play sound "dialog.mp3"
    arya "Bu, maaf Arya baru pulang, Arya sudah dengar dari Tia bu, Ibu gapapa?"

    play sound "dialog.mp3"
    ibuarya "Ibu nggak apa-apa, hanya kaget saja dan jadi gelisah."

    play sound "dialog.mp3"
    arya "Kata dokternya gimana Bu? Kapan pengobatannya bisa dimulai?"

    play sound "dialog.mp3"
    ibuarya "Segera setelah Ibu mendaftar dan biaya pengobatannya dibayar Nak, dokternya bilang harus secepatnya…"

    play sound "dialog.mp3"
    ibuarya "Nak, maaf ibu jadi beban buat kamu dan Tia."
    play sound "dialog.mp3"
    ibuarya "Seharusnya dengan posisimu sekarang Ibu gak perlu nambah beban kamu untuk mengeluarkan uang lagi.."

    hide aryasedih
    show aryasmile at left
    show aryasmile at midleft with move
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
    scene bg rumahmalam with wipeleft
    show aryabingung at left

    play sound "dialog.mp3"
    arya "Aduh, apa aku pinjem uang dulu ya, ke siapa ya enaknya."    

    hide aryabingung
    show aryanelpon at left
    show mayanelpon at right with easeinright
    play sound "dialog.mp3"
    arya "Halo Maya, maaf telepon kamu malem-malem gini, kamu lagi sibuk nggak? Aku mau minta tolong.."    

    play sound "dialog.mp3"
    maya "Halo Arya, kamu mau minta tolong apaan emangnya? Pasti aku coba bantu kok."


    play sound "dialog.mp3"
    arya "Anu May… Ibuku tadi sore didiagnosis kena Diabetes, aku harus cepet-cepet bayar biaya pengobatannya."    


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
    
    play sound "dialog.mp3"
    arya "Aduh May makasih banyak ya, nanti aku sampaikan salammu ke Ibu."
    
    jump d1

label c5_2:
    scene bg kantorkeroco with wipeleft
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
    show aryasmile2 at left
    play sound "dialog.mp3"
    arya "Eh gapapa Pak, aman kok Pak"

    show bg kantor with wipeleft


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

    hide aryasmile2
    show aryasedih at left
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

    hide hendranormal
    show hendrasenyumlicik at right

    play sound "dialog.mp3"
    hendra "Siapa bilang pinjamnya ke saya?"

    play sound "dialog.mp3"
    hendra "(bisik-bisik) Pinjam ke kantor."

    play sound "dialog.mp3"
    arya "Aduh pak nggak deh pak, saya gak berani."


    play sound "dialog.mp3"
    hendra "Kamu mau masalah kamu cepat selesai tidak? Saya yakin ibumu juga butuh diobati secepatnya."

    play sound "dialog.mp3"
    hendra "Saya bukannya mau gimana-gimana, hanya mau membantu cari jalan kok."

    hide aryasedih
    show aryapanik at left
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

    hide aryapanik
    show aryasedih at left
    play sound "dialog.mp3"
    arya "Baik pak, terimakasih banyak Pak Hendra untuk bantuannya."

    hide hendrasenyumlicik with easeoutright

    scene bg kantorkeroco
    
    show aryanormal at left with easeinleft
    $ renpy.pause(0.5)
    show dhiyalcuriga at right with easeinright

    play sound "dialog.mp3"
    dhiyal "Ya, habis diapain sama Pak Hendra?"

    play sound "dialog.mp3"
    arya "Ngga diapa-apain, justru saya yang minta tolong Pak Hendra."

    play sound "dialog.mp3"
    dhiyal "Curiga nih saya, minta tolong apaan tuh?"

    hide aryanormal
    show aryasmile at left
    play sound "dialog.mp3"
    arya "Ah ada deh pokoknya Yal."

    play sound "dialog.mp3"
    dhiyal "Waduh, coba tebak, bahasa indonesianya dari kata Criminal apa coba?"

    hide aryasmile
    show aryasmile2 at left

    play sound "dialog.mp3"
    arya "Aduh Pak saya lagi pusing, gak mood buat tebak-tebakan."

    menu:
        "Penjahit":
            play sound "dialog.mp3"
        "Pemahat":
            play sound "dialog.mp3"
        "Pak Hendra":
            play sound "dialog.mp3"
    
    show emojimarah at Position(xpos=0.2, ypos=0.25)
    dhiyal "Jawabannya Pak Hendra! Kalau urusannya sama Pak Hendra saya yakin dia ngajak kamu main kotor kan?"

    hide aryasmile2
    show aryamarah at left
    play sound "dialog.mp3"
    arya "Eh apaan sih ngga kok, jangan mikir aneh-aneh gitu ah Yal."

    play sound "dialog.mp3"
    dhiyal "Saya tau kok track record kelakuan-kelakuan Pak Hendra seperti apa."
    
    play sound "dialog.mp3"
    dhiyal "Awas Arya, main kotor ga akan berkah untuk kamu dan masa depanmu."

    hide aryamarah
    show aryanormal at left

    jump d1
    

label c5_3:
    scene bg room with wipeleft
    show aryasedih at left with easeinleft
    $ renpy.pause(1)
    show tiasedih at right with easeinright

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
    scene bg kantor with wipeleft
    show aryasmile2 at left with easeinleft
    $ renpy.pause(1)
    play sound "dialog.mp3"
    arya "(Suatu hari di kantor Arya menemukan dokumen kecurangan tender besar. Hendra terlibat, begitu juga Kartika.)"
    show hendrasenyumlicik at right with easeinright


    play sound "dialog.mp3"
    play music "Lagu KWN Scene 5 Original.mp3" fadein 2 fadeout 2
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
    show tiapanik at right with easeinright
    
    play sound "dialog.mp3"
    tia "Kamu gapapa, sayang? Gimana di kantor hari ini?"
    
    hide aryanormal
    show aryasedih at left
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

    jump e1

label d1_2:
    hide hendranormal with easeoutright
    hide aryanormal with easeoutleft
    
    scene bg room with wipeleft

    show aryasedih at left with easeinleft
    $ renpy.pause(1)
    show tiasedih at right with easeinright
    
    play sound "dialog.mp3"
    tia "Sayang, kamu sakit? Kenapa muka kamu pucet banget?"
    

    play sound "dialog.mp3"
    arya "Aku kebingungan.."
    
    play sound "dialog.mp3"
    tia "Masalah kerja ya? Kamu kan selalu cerita sama aku.. Kali ini juga gapapa, cerita aja."
    
    play sound "dialog.mp3"
    arya "Aku nemuin kasus, Tia, kasus besar Pak Hendra."
    
    hide tiasedih
    show tiapanik at right

    play sound "dialog.mp3"
    arya "Aku harus ngelaporin ini, aku tau. Tapi aku harus bicara dulu dengan Pak Hendra atau engga ya, Ti? Aku bingung…"

    play sound "dialog.mp3"
    tia "Apapun itu, kamu harus tetap berada di jalan yang benar ya, sayang?"

    scene bg kantor with wipeleft

    show hendrasenyumlicik at right
    $ renpy.pause(1)
    show aryanormal at left with easeinleft

    play sound "dialog.mp3"
    hendra "Anak muda, kamu pintar. Sayang kalau karir bagusmu harus berakhir cepat. Mari kita bicarakan dengan kepala dingin."
    play sound "dialog.mp3"
    hendra "Dengar baik baik nak, saya bisa membantu kamu naik jabatan dengan cepat dan mudah."
    play sound "dialog.mp3"
    hendra "Ignorance is bliss. Kita lewati saja ini dengan rapi ya?"
    
    hide aryanormal
    show aryasmile2 at left
    play sound "dialog.mp3"
    arya "Baik pak."
    $ renpy.pause(1)

    play sound "dialog.mp3"
    arya "Untungnya bagi saya, pak?"

    hide hendrasenyumlicik
    show hendraketawa at right

    play sound "dialog.mp3"
    hendra "(Terbahak-bahak seram)"

    play sound "dialog.mp3"
    arya "Saya butuh pak. Bukan bapak saja."


    play sound "dialog.mp3"
    hendra "(Tertawa perlahan) Tentu saja. Brilian. Kamu ingin berapa? 5x 10x dari biaya pengobatan ibu kamu?"
    
    hide aryasmile
    show aryasedih at left
    play sound "dialog.mp3"
    arya "S-saya.."

    hide hendraketawa
    show hendrasenyumlicik at right
    play sound "dialog.mp3"
    hendra "Tidak ada yang terjadi di kantor ini yang saya tidak ketahui tentu saja, Arya. Masalah uang, gampang."

    play sound "dialog.mp3"
    hendra "Kamu serahkan pada saya. Aman… selama kamu (menaikkan tangannya ke mulut membuat isyarat 'diam')"
    hide aryasedih
    show aryasmile2 at left
    play sound "dialog.mp3"
    arya "(Mengangguk pelan)"

    scene bg rooftop with wipeleft

    show dhiyalcuriga at right 
    $ renpy.pause(1.0)
    show aryasedih at left with easeinleft

    play sound "dialog.mp3"
    arya "Yal, saya-(omongannya dipotong Dhiyal)"

    play sound "dialog.mp3"
    dhiyal "Arya, kamu paham gak sih kita menolak korupsi artinya kita memilih untuk jadi bagian dari solusi, sesimpel itu."

    play sound "dialog.mp3"
    dhiyal "Koruptor-koruptor gak mikirin perasaan keluarga dan teman-teman mereka yang kecewa kalau tau yang sebenarnya."

    play sound "dialog.mp3"
    dhiyal "Korupsi menghancurkan keadilan dan merampas hak-hak rakyat, Ya. Saya miris sekali melihat negara ini."

    play sound "dialog.mp3"
    dhiyal "Ayo Arya kita seharusnya bisa lebih bijak."

    jump e2

label d1_3:

    scene bg kantorkeroco with wipeleft
    show kartikanormal at right with easeinright
    $ renpy.pause(0.5)
    show aryamarah at left with easeinleft 
    
    play sound "dialog.mp3"
    arya "Aku tahu Kar, apa yang kamu lakukan dengan Pak Hendra."

    play sound "dialog.mp3"
    kartika "M-maksud kamu apa, Arya?"

    play sound "dialog.mp3"
    arya "Tender itu, aku tahu."

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

    hide aryamarah
    show aryasedih at left
    play sound "dialog.mp3"
    arya "Iya."

    
    jump e3


label e1:
    play sound "scene.mp3"
    scene bg kpk with wipeleft
    play music "Lagu KWN Scene 6 A.mp3" fadein 2 fadeout 2

    #petugas KPK
    show petugaskpknormal at right
    $ renpy.pause(1)
    show aryanormal at left with easeinleft

    play sound "dialog.mp3"
    arya "Ini semua bukti yang saya punya. Proyek ini sudah dirancang untuk menguntungkan pihak tertentu sejak awal."
    play sound "dialog.mp3"
    arya "Mereka harus dihentikan."
    
    play sound "dialog.mp3"
    petugas "(mengangguk, melihat dokumen dengan ekspresi serius)"
    play sound "dialog.mp3"
    petugas "Kami akan menindaklanjuti laporan ini. Tidak mudah melakukan ini, apalagi di posisi Anda."
    play sound "dialog.mp3"
    petugas "Saya pastikan Anda telah memilih jalan yang benar."

    scene bg kpk2 with wipeleft
    
    show aryanormal at left
    $ renpy.pause(1)
    show mayanormal at right with easeinright

    play sound "dialog.mp3"
    maya "Kamu bener-bener ngelakuin ini, Arya. Ini berita besar."
    play sound "dialog.mp3"
    maya "Aku secepatnya bakal mempublikasikan kasus ini. Akhirnya ya kita bisa ngungkapin semuanya ke publik."
    

    hide aryanormal
    show aryasmile at left

    play sound "dialog.mp3"
    arya "Aku cuma ngelakuin hal yang emang harus dilakukan."
    play sound "dialog.mp3"
    arya "Ini gak gampang sama sekali, banyak tekanan, banyak tawaran. Makasih banyak bantuannya ya May."

    play sound "dialog.mp3"
    maya "Kamu yang harusnya dapet penghargaan. Aku cuma ngelakuin tugasku sebagai jurnalis."
    play sound "dialog.mp3"
    maya "Tapi kamu bener-bener berani menghadapi mereka."

    
    scene bg pemerintah with wipeleft

    show aryanormal at left with easeinleft
    $ renpy.pause(1)
    #gubernur
    show gubernurnormal at right with easeinright

    play sound "dialog.mp3"
    gubernur "Arya, keputusan membongkar kasus ini adalah langkah yang tidak mudah. Integritas yang luar biasa."
    play sound "dialog.mp3"
    gubernur "Karena itu, saya ingin menaikkan jabatan kamu. Negara ini butuh orang-orang seperti kamu."

    hide aryanormal
    show aryasmile at left

    play sound "dialog.mp3"
    arya "Terima kasih, pak. Saya hanya ingin membuktikan bahwa birokrasi masih bisa bersih."

    hide gubernurnormal with easeoutright

    show mayamic with easeinright
    play sound "dialog.mp3"
    maya "Bagaimana rasanya, Arya? Berhasil membongkar korupsi setelah semua yang kamu lalui?"

    play sound "dialog.mp3"
    arya "Jika ini memberiku lebih banyak kesempatan untuk menjaga integritas, aku akan menghadapinya."

    play sound "dialog.mp3"
    arya "Aku tidak akan mengubah prinsipku."

    play sound "dialog.mp3"
    maya "Aku percaya sama kamu, Arya. Kamu layak berada di sini."

    play sound "dialog.mp3"
    maya "Aku yakin kamu akan terus berjuang untuk kebenaran."

    hide aryasmile
    show aryasmile2 at left 
    play sound "dialog.mp3"
    arya "Dan aku tahu, selama ada orang seperti kamu, aku tidak akan berjuang sendirian"

    scene bg rumah with wipeleft
    show ibuaryasenang at right
    $ renpy.pause(1)
    show aryanormal at left with easeinleft

    play sound "dialog.mp3"
    ibuarya "Nak, ibu sudah mendengar semuanya."

    play sound "dialog.mp3"
    ibuarya "Kamu sudah melakukan hal yang benar. Ibu bangga sekali padamu."

    hide aryanormal
    show aryasmile at left
    play sound "dialog.mp3"
    arya "Arya hanya melakukan apa yang seharusnya dilakukan, Bu.."

    play sound "dialog.mp3"
    arya "Semua ini untuk membuktikan bahwa kita bisa hidup tanpa harus tunduk pada korupsi."

    play sound "dialog.mp3"
    ibuarya "Kamu  membuktikan kalau nilai nilai yang ibu dan ayah ajarkan selama ini gak sia-sia."

    play sound "dialog.mp3"
    ibuarya "Kamu sudah menjadi anak yang ibu impikan, makasih ya Nak."

    show tiabangga at right with easeinright
    show tiabangga at midright with move
    play sound "dialog.mp3"
    tia "Aku tau kamu bisa, Arya. kamu pilih jalan yang sulit tapi itulah yang membuat kamu berbeda."

    play sound "dialog.mp3"
    arya "Terima kasih, Sayang. Kalau bukan karena kamu, mungkin aku udah tersesat dalam pilihan yang salah."

    play sound "dialog.mp3"
    tia "Kamu gaakan tersesat. Kamu tau mana yang benar dan salah. Itulah kenapa aku selalu percaya sama kamu."
    
    jump epilog

label e2:
    scene bg kantor with wipeleft
    show hendrasenyumlicik at right
    $ renpy.pause(1)
    show aryanormal at left with easeinleft

    play sound "dialog.mp3"
    hendra "Kamu bekerja keras, Arya. Ini hanya sedikit apresiasi dari kami."

    play sound "dialog.mp3"
    hendra "Anggap saja sebagai bonus kecil untuk semua dedikasi yang sudah kamu tunjukkan."

    hide aryanormal

    show aryasmile2 at left
    play music "Lagu KWN Scene 6 B.mp3" fadein 2 fadeout 2
    play sound "dialog.mp3"
    arya "Ini… terlalu banyak, Pak. Saya tidak bisa menerima ini."

    play sound "dialog.mp3"
    hendra "Arya, ini bukan suap. Anggap saja sebagai penghargaan. Lagipula, kamu tidak melakukan sesuatu yang salah, kan?"

    play sound "dialog.mp3"
    hendra "Kamu hanya ingin menjalankan tugasmu. Tak ada yang tau, tak ada yang akan bertanya."

    play sound "dialog.mp3"
    arya "Baiklah pak… saya terima."

    play sound "dialog.mp3"
    hendra "Bagus, Arya. Kamu membuat keputusan yang bijak. Karirmu akan baik-baik saja di sini."

    play sound "dialog.mp3"
    hendra "Kamu akan naik jabatan. Percayalah, ini baru permulaan."

    scene bg rumah with wipeleft
    show ibuaryanormal at right
    $ renpy.pause(1)
    show aryanormal at left with easeinleft

    play sound "dialog.mp3"
    ibuarya "Nak, kamu sering pulang larut sekarang. Ibu mulai merasa ada yang tidak beres. Apa yang sebenarnya terjadi?"

    play sound "dialog.mp3"
    arya "Ini cuma masalah pekerjaan, bu. Aku sibuk, banyak tanggung jawab baru."

    play sound "dialog.mp3"
    ibuarya "Tapi kenapa rasanya kamu makin jauh, nak?"

    play sound "dialog.mp3"
    ibuarya "Ibu gak mau kamu tersesat dalam pekerjaan sampai melupakan apa yang sebenarnya penting."
    
    hide aryanormal
    show aryasmile2 at left
    play sound "dialog.mp3"
    arya "Aku... hanya ingin memastikan kita aman, bu."

    play sound "dialog.mp3"
    ibuarya "Apa ini benar benar untuk kita, atau kamu mulai kehilangan dirimu sendiri?"
    
    $ renpy.pause(1)

    scene bg kantorarya with wipeleft
    
    show aryanormal at left
    $ renpy.pause(1)
    show hendrasenyumlicik at right with easeinright
    
    play sound "dialog.mp3"
    hendra "Bagaimana rasanya , Arya? Semua berjalan mulus, kan? Lihat dirimu sekarang. Pejabat muda yang karirnya melesat."
    
    hide aryanormal
    show aryasmile at left
    play sound "dialog.mp3"
    arya "Ya, pak. Terima kasih atas bantuannya selama ini."
    
    play sound "dialog.mp3"
    hendra "Jangan khawatir, Arya. Dunia ini memang keras, tapi kita tahu bagaimana memainkannya.."
    
    play sound "dialog.mp3"
    hendra "Yang penting, jangan terlalu banyak bertanya. Nikmati saja posisimu sekarang."

    scene bg kantorkeroco with wipeleft

    show aryanormal at left
    $ renpy.pause(1)
    show mayakecewa at right with easeinright
    show emojipatahhati at Position(xpos=0.8, ypos=0.3)
    play sound "dialog.mp3"
    maya "Arya, aku dengar rumor tentang kamu… kamu beneran nerima uang dari Pak Hendra?"

    show emojiflat at Position(xpos=0.2, ypos=0.25)
    play sound "dialog.mp3"
    arya "Maya, aku terpaksa… ibuku sakit, aku perlu uang untuk pengobatannya. Aku gak punya pilihan lain May."

    play sound "dialog.mp3"
    maya "Kamu tuh selalu punya pilihan, Arya! Kamu bisa bilang tidak, kamu bisa nolak."

    play sound "dialog.mp3"
    maya "Sekarang kamu tuh sama aja sama mereka. Kamu pikir abis ini aku masih bisa percaya kamu? Ngga Ya."
    
    play sound "dialog.mp3"
    arya "Maya, ini cuman sekali kok. Aku janji gak akan gini lagi. Aku hanya... Aku..."
    
    play sound "dialog.mp3"
    maya "Udah terlambat, Arya. kamu mungkin gak akan ngelakuin hal ini lagi, tapi semuanya udah rusak sekarang."

    play sound "dialog.mp3"
    maya "Integritas kamu, kepercayaan kamu, semuanya, apa sih yang ada di otak kamu?!"

    play sound "dialog.mp3"
    maya "Aku harap, uang itu layak untuk kehilangan segalanya."
    hide emojipatahhati
    hide mayakecewa with easeoutright

    jump epilog





label e3:
    scene bg kantorkeroco with wipeleft
    
    show aryanormal
    play music "Lagu KWN Scene 5 Original.mp3" fadein 2 fadeout 2
    play sound "dialog.mp3"
    arya "Ini dia... semua bukti yang aku butuhkan."

    play sound "dialog.mp3"
    arya "Semua ini akan mengubah segalanya, tapi... risiko terlalu besar. Apakah aku siap?"
    
    hide aryanormal
    show aryanelpon
    show aryanelpon at left with move

    play sound "dialog.mp3"
    arya "Halo, Maya."

    show mayanelpon at right with easeinright
    play sound "dialog.mp3"
    maya "Arya, aku udah siap. Data yang kamu kirimin besar banget."

    play sound "dialog.mp3"
    maya "Ini bisa jadi skandal paling besar yang pernah kita publikasikan."

    play sound "dialog.mp3"
    arya "Aku tau. Tapi konsekuensinya juga besar, May. Mereka pasti bakal ngelakuin segala cara untuk menghentikan kita."

    play sound "dialog.mp3"
    arya "Hendra dan Kartika bukan orang yang bisa kita anggap remeh."

    play sound "dialog.mp3"
    maya "Arya, kamu udah melangkah sejauh ini. Ini bukan cuman tentang kita lagi. Semua orang berhak tau."

    play sound "dialog.mp3"
    maya "Kalau kamu mundur, korupsi bakal terus menggerogoti sistem. Kamu juga tau sendiri apa yang akan terjadi."

    play sound "dialog.mp3"
    arya "Iya May kamu bener."

    play sound "dialog.mp3"
    arya "Aku udah berkomitmen buat memperbaiki sistem dari dalam. Kita harus bongkar, gak peduli risikonya."

    scene bg kantormaya with wipeleft

    show mayanormal at right
    $ renpy.pause(1)
    show aryanormal at left with easeinleft

    play sound "dialog.mp3"
    maya "Udah siap menggemparkan semua pegawai kantor?"

    play sound "dialog.mp3"
    arya "Ini gak gampang. Aku gak tau apa yang bisa terjadi setelah ini. Tapi aku tau ini langkah yang harus aku ambil."

    play sound "dialog.mp3"
    maya "Kita tau risikonya. Aku udah siap. Tapi yang penting, Arya, kamu gak sendirian. Kita bakal bongkar bareng-bareng."

    play sound "dialog.mp3"
    arya "Iya May, aku cuman berharap kita bisa bertahan sampai akhir."

    scene bg rumahmalam with wipeleft

    show aryanormal at left with easeinleft
    $ renpy.pause(1)
    hide aryanormal
    show aryanelpon at left 
    show teleponnormal at right with easeinright

    play sound "dialog.mp3"
    telepon "Jangan bermain-main dengan api, Arya. Kamu tahu apa yang bisa terjadi kalau kamu terus menggali lebih dalam."

    play sound "dialog.mp3"
    arya "Jika kamu pikir bisa menghentikan aku dengan ancaman ini, kamu salah. Aku gak akan pernah mundur."

    play sound "dialog.mp3"
    telepon "Kita lihat saja nanti."

    scene bg publikasi with wipeleft

    show aryanormal at left with easeinleft
    show mayanormal at right with easeinright

    play sound "dialog.mp3"
    maya "Ini dia, Arya. Begitu kita tekan tombol ini, gak ada jalan kembali."

    play sound "dialog.mp3"
    arya "Aku tau May dan aku siap."

    play sound "dialog.mp3"
    maya "Kamu tau gak sih Ya, banyak orang yang bakal terinspirasi sama apa yang kamu lakuin ini."

    play sound "dialog.mp3"
    maya "Kamu gak cuman membongkar korupsi ini, kamu juga nunjukkin bahwa masih ada harapan untuk birokrasi bersih."

    hide aryanormal
    show aryasmile at left
    play sound "dialog.mp3"
    arya "Iya itu tujuan awalku. Semoga yang kita lakuin ini membuka jalan bagi pegawai-pegawai muda lainnya."
    
    play sound "dialog.mp3"
    maya "Oke, saatnya kita mulai revolusi."

    scene bg kantorkeroco with wipeleft
    show aryanormal with easeinleft
    $ renpy.pause(1)
    
    show pegawai1normal at right with easeinright
    play music "Lagu KWN Scene 6 C.mp3" fadein 2 fadeout 2

    play sound "dialog.mp3"
    pegawai1 "Pak Arya, kami hanya ingin bilang, kami sangat terinspirasi oleh keberanian Bapak."

    play sound "dialog.mp3"
    pegawai1 "Apa yang Bapak lakukan memberikan kai harapan bahwa kita bisa membuat perubahan."
    
    show pegawai2normal at left with easeinleft

    play sound "dialog.mp3"
    pegawai2 "Benar pak. Kami tidak menyangka ada seseorang yang berani melawan sistem seperti ini dari dalam."

    play sound "dialog.mp3"
    pegawai2 "Terima kasih sudah menunjukkan jalannya."
    
    hide aryanormal
    show aryasmile

    play sound "dialog.mp3"
    arya "Terima kasih. Perubahan tidak akan datang dengan mudah."

    play sound "dialog.mp3"
    arya "Selama kita berkomitmen pada integritas dan kebenaran, kita pasti bisa membuat perbedaan."

    scene bg rooftop with wipeleft
    show aryasmile at left with easeinleft
    show mayanormal at right with easeinright
    
    play sound "dialog.mp3"
    maya "Kamu berhasil, Arya. Kita berhasil!"

    play sound "dialog.mp3"
    arya "Iya May, tapi ini baru permulaan. Masih banyak yang harus kita lakuin."

    show mayanormal at midright with move
    play sound "dialog.mp3"
    maya "Tapi seenggaknya, kamu udah nunjukkin ke dunia bahwa perubahan itu sangat mungkin."

    hide aryasmile
    show aryanormal at left
    show aryanormal at midleft with move
    play sound "dialog.mp3"
    arya "Iya, dan aku akan terus berjuang."

    jump epilog

label epilog:
    scene bg kantorkeroco with wipeleft
    $ renpy.pause(2)