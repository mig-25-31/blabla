import math
def calculate_energy(A, theta):
    theta_rad = math.radians(theta)
    sin_kare = math.sin(theta_rad)**2
    kok_ici = A**2 - sin_kare
    if kok_ici < 0:
        return 0.0
    bolen = math.cos(theta_rad) + math.sqrt(kok_ici)
    bolunen = A + 1
    faktor = (bolen / bolunen) ** 2
    return 1.0 * faktor
if __name__ == "__main__":
    print("--- notronun enerjisini hesaplama ---")
    while True:
        try:
            inp_A = input("\nhedef kutle (A) degeri giriniz (sistemden cikmak icin;once gecersiz bir birime(ornegin bir harf) basip enter tusuma bastiktan sonra 'f' tusuna basiniz): ")
            if inp_A == 'f':
                break
            A = float(inp_A)
            inp_theta = input("sacilma acisi (derece): ")
            theta = float(inp_theta)
            if A < 1:
                print("hata: A degeri 1'den kucuk verilemez.")
                continue
            sonuc = calculate_energy(A, theta)
            print(f"son enerji durumu: {sonuc:.4f} MeV")
        except ValueError:
            print("sayi gir.")
