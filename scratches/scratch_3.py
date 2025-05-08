txt1 = 'hj-e-uad-yhn'
txt2 = 'oetmal-epto'
txt = ''
i = 0
while i < len(txt2):
   txt = txt + txt1[i] + txt2[i]
   i += 1
if len(txt1 + txt2) % 2 == 1:
    txt = txt + txt[i]
print(txt)