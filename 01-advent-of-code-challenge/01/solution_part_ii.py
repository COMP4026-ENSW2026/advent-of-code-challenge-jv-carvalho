calorias = []
caloria_atual_elfo = []
with open('Input.txt', 'r') as f:
  for line in f:
    if line.strip(): 
      caloria_atual_elfo.append(int(line))
    else:  
      calorias.append(caloria_atual_elfo)
      caloria_atual_elfo = []  

if caloria_atual_elfo:
  calorias.append(caloria_atual_elfo)

calorias = sorted(calorias, key=sum, reverse=True)

top_calorias = calorias[:3]

total_calorias = sum(sum(elfo_calorias) for elfo_calorias in top_calorias)
