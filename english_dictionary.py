import json

dic_data = """{
  "anopheles" : "A genus of mosquitoes which are secondary hosts of the malaria parasites, and whose bite is the usual, if not the only, means of infecting human beings with malaria. Several species are found in the United States. They may be distinguished from the ordinary mosquitoes of the genus Culex by the long slender palpi, nearly equaling the beak in length, while those of the female Culex are very short. They also assume different positions when resting, Culex usually holding the body parallel to the surface on which it rests and keeping the head and beak bent at an angle, while Anopheles holds the body at an angle with the surface and the head and beak in line with it. Unless they become themselves infected by previously biting a subject affected with malaria, the insects cannot transmit the disease.",
  "uniclinal" : "See Nonoclinal.",
  "sarong" : "A sort of petticoat worn by both sexes in Java and the Malay Archipelago. Balfour (Cyc. of India)",
  "turcoman" : "1. A member of a tribe of Turanians inhabiting a region east of the Caspian Sea. 2. A Turcoman carpet. Turcoman carpet or rug, a kind of carpet or rug supposed to be made by the Turcomans.",
  "corrugator" : "A muscle which contracts the skin of the forehead into wrinkles.",
  "self-murder" : "Suicide.",
  "anacardium" : "A genus of plants including the cashew tree. See Cashew.", "sunken" : "Lying on the bottom of a river or other water; sunk.",
  "fisetic" : "Pertaining to fustet or fisetin.",
  "boarder" : "1. One who has food statedly at another's table, or meals and lodgings in his house, for pay, or compensation of any kind. 2. (Naut.)  One who boards a ship; one selected to board an enemy's ship. Totten.",
  "niobate" : "Same as Columbate.",
  "challengeable" : "That may be challenged.",
  "yelper" : "An animal that yelps, or makes a yelping noise. Specifically: (Zoöl.) (a) The avocet; -- so called from its sharp, shrill cry. [Prov. Eng.] (b) The tattler. [Local, U. S.]",
  "moonbeam" : "A ray of light from the moon.",
  "impleader" : "One who prosecutes or sues another.",
  "stelleridan" : "A starfish, or brittle star."
  
}"""

user1 = input("kelime giriniz:")

x = json.loads(dic_data)

if user1 in x:
    print("%s girdiğiniz kelime sözlükte bulunmuştur." %user1)
    print("Anlam:", x[user1])
else:
    print("%s girdiğiniz kelime sözlükte bulunamamıştır." %user1)