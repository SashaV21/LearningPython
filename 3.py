elf = int(input())
gnom = int(input())
person = int(input())

f_elf = elf // 10
s_elf = elf % 10

f_gnom = elf // 10
s_gnom = elf % 10

f_person = person // 10
s_person = person % 10

if f_elf == f_gnom == f_person:
    print(f_elf)
elif s_elf == s_gnom == s_person:
    print(s_elf)
else:
    print("NO")