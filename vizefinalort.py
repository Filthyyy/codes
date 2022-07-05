vize = input('Vize Notunuz : ')
final = input('Final Notunuz : ')
ortalama=(float(vize)*0.4)+(float(final)*0.6)
print("Ortalama :{0} ".format(ortalama))
if(int(ortalama)<40):
    print("Kaldınız")
elif(int(ortalama)>=40):
    print("Gectiniz")
