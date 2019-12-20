from G8RNG import XOROSHIRO,Raid

PID = 0x9c86F7F8
EC = 0x9dffc477
IVs = [14, 31, 31, 31, 10, 24]
usefilters = True
MaxResults = 1000

shiny_type = False
ABILITY    = [1]
NATURE     = ["QUIRKY", "ADAMANT"]
FLAG       = True

HP  = [31]
Atk = [0, 31]
Def = [31]
SpA = [31]
SpD = [31]
Spe = [0, 31]

# Desired IVs
# V6 = [31, 31, 31, 31, 31, 31]
# S0 = [31, 31, 31, 31, 31, 00]
# A0 = [31, 00, 31, 31, 31, 31]
# A0S0 = [31, 00, 31, 31, 31, 00]

# Find seeds
results = Raid.getseeds(EC, PID, IVs)

if len(results) == 0:
    print("No raid seed")
else:  
    for result in results:
        if result[1] > 0:
            print(f"seed = 0x{result[0]:016X}\nPerfect IVs:{result[1]}")
            r = Raid(result[0],flawlessiv=result[1], HA=0, RandomGender=0)
            r.print()
        else:
            print(f"seed = 0x{result[0]:016X}\n(Shiny locked!) Perfect IVs:{-result[1]}")
            r = Raid(result[0],flawlessiv=-result[1], HA=1, RandomGender=0)
            r.print()

# Calc frames
if len(results) > 0:
    print(f"\n\nResults:")
    seed = results[0][0]
    i = 0
    while i < MaxResults:
        r = Raid(seed, flawlessiv=4, HA=1, RandomGender=0, ability=ABILITY, nature=NATURE, flg=FLAG)
        seed = XOROSHIRO(seed).next()
        if usefilters:
            if shiny_type:
                if r.ShinyType != "None":
                    if r.print():
                        print("the " + str(i) + " days!\n")
            elif (not HP or r.IVs[0] in HP) and (not Atk or r.IVs[1] in Atk) and (not Def or r.IVs[2] in Def) and (not SpA or r.IVs[3] in SpA) and (not SpD or r.IVs[4] in SpD) and (not Spe or r.IVs[5] in Spe):
                if r.print():
                    print("the " + str(i) + " days!\n")
        else:
            if r.print():
                print("the " + str(i) + " days!\n")

        i += 1
