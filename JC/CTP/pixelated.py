from PIL import Image
i1 = Image.open("CTP\scrambled1.png")
i2 = Image.open("CTP\scrambled2.png")
p1 = i1.load()
p2 = i2.load()

flag = Image.new("RGB", i1.size)
flagp = flag.load()
for r in range(i1.size[1]):
    for c in range(i1.size[0]):
        flagp[c, r] = (
            (p1[c, r][0] + p2[c, r][0]) % 256,
            (p1[c, r][1] + p2[c, r][1]) % 256,
            (p1[c, r][2] + p2[c, r][2]) % 256,
        )
flag.save("flag.png")
print("flag.png saved")