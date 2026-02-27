class NamaError (Exception):
    def __init__ (self, nama):
     self.nama = nama
     super().__init__(f"Nama {nama} terlalu pendek! Minimal 3 karakter.")

def validasi_nama():
    try:
       nama = input (" Nama : ")
       if len(nama) < 3 :
            raise NamaError(nama)
       return nama 
    
    except NamaError as e:
       print(f" [ERROR] {e}")
       return validasi_nama()

class UmurError (Exception):
   def __init__(self, umur):
      self.umur = umur
      super().__init__(f"Umur {umur} tidak memenuhi syarat (17-60 tahun)")

def validasi_umur():
    try:
       umur = int(input (" umur : "))
       if umur < 17 or umur > 60:
          raise UmurError(umur)
       return umur
    
    except UmurError as e:
       print(f" [ERROR] {e} ")
       return validasi_umur()
    
def validasi_email():
        try:
            email = input ("email :")
            if "@" not in email:
                raise ValueError ("Email tidak valid! Harus mengandung '@'.")
            return (email)

        except ValueError as e:
         print(f"[ERROR] {e}")
        return validasi_email()
   
def validasi_noHP():
        try:
            no_HP = int(input("No HP : "))
            if len(no_HP) >= 10 and len(no_HP) <= 13:
                return no_HP
            raise ValueError ("No HP tidak valid! Harus 10-13 digit angka.")
        except ValueError as e:
            print(f"[ERROR] {e}")
            return validasi_noHP ()
        finally:
            print ("Proses input selesai.")

def main():
    print ("=== REGISTRASI PESERTA SEMINAR ===")

    nama = validasi_nama()
    umur = validasi_umur()
    email = validasi_email()
    no_HP = validasi_noHP()

    print("=== DATA PESERTA ===")
    print(f"nama  : {nama}")
    print(f"umur  : {umur}")
    print(f"email : {email}")
    print(f"No_HP : {no_HP}")
    print(f"Status: TERDAFTAR")

if __name__ == "__main__":
        main()