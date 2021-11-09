1    # Juego ESCAPE
2    
3    
4    #Opciones
5    opciones={
6    "A":"Acercarte a la ventana y gritar",
7    "B":"Realizar búsqueda exhaustiva",
8    "C":"Dormir un poco para recuperarte del dolor "
9     }
10   opciones2={
11   "A": "Visualizar las fotos",
12   "B": "Buscar algo para defenderte",
13   "C": "Lamer la sangre contaminada"
14   }
15   opciones3={
16   "A": "Intentar abrir la puerta de esa habitación",
17   "B": "Volver por el túnel a la anterior habitación e intentar abrir la puerta"	
18   }
19   opciones4={
20   "A": "Utilizar tu herramienta para combatirlo y huir",
21   "B": "Dejar que te coma para que no se muera de hambre"
22   }
23   opciones5={
24   "A": "Tomar agua estancada del piso",
25   "B": "Comer la rata que te miraba mientras dormías",
26   "C": "Meditar"
27   }
28   opciones6={
29   "A": "Agarrar las fotos",
30   "B": "Quemar las fotos",
31   "C": "Buscar algo para defenderte"
32   }
33   opciones7={
34   "A": "Hacer flexiones de brazos",
35   "B": "Correr en circulos"
36   }
37   punto=0
38   
39   #Funciones
40   def finsi():
41   	print("Fin. Gracias por jugar :)")
42   	exit()
43   def anykey():
44   	anykey=input("Ingrese cualquier tecla para proceder: ")
45   	print("--------------------------------------")
46   def puntos():
47   	print("AVISO >> Sumaste 10 puntos IQ por elegir la mejor opción")
48   def puntosObt():
49   	print(f"En total ganaste {punto} puntos")
50   def enter():
51   	print()
52   def conteo(n):
53   	if n == 0:
54   		exit()
55   	else:
56   		print(n)
57   		conteo(n-1)
58   
59   #Inicio
60   preg=input("¿Quiere jugar? <si/no> ")
61   enter()
62   preg=preg.lower()
63   while preg!="si" and preg!="no": 
64   	preg=input("Colocá un caracter permitido <si/no> ") 
65   	preg=preg.lower()
66   if preg=="no":
67   	enter()
68   	print("Entonces... ¿Qué haces acá?")
69   	puntosObt()
70   	exit()
71   elif preg=="si":
72   	enter()
73   	puntos()
74   	punto+=10
75   	enter()
76   	print('''Te despertaste en una habitacióna oscura... no sabes donde estás
77   ni por qué te duele la cabeza. ¿Qué deseas hacer?''')
78   	enter()
79   
80   #OPCIONES 1
81   for key, values in opciones.items(): 
82   	print(key,'-',values)
83   enter()
84   seleccion=input("Elige opción: ")
85   seleccion=seleccion.upper()
86   enter()
87   while not seleccion in opciones:# filtro APB
88   	print(f"'{seleccion.lower()}' no es una opción válida")
89   	seleccion=input("Elige opción: ")
90   	seleccion=seleccion.upper()
91   	enter()
92   if seleccion=='A':
93   	print('''Te diriges hacia la ventana y al mirar hacia afuera te asombras...
94   te encuentras en lo alto de una montaña... nadie te escuchará por lo que
95   decides escapar ya. Comienza examinando la habitación''') 
96   	enter()
97   	anykey()
98   	punto+=5
99   	enter()
100  	print('''¡Enhorabuena! encontraste una puerta en el suelo (pero que está cerrada)
101  y un túnel el cual podrás utilizar.''')
102  	enter()
103  	anykey()
104  elif seleccion=='B':
105  	puntos()
106  	print("Mejoras la habilidad para elaborar herramientas")
107  	punto+=10
108  	enter()
109  	print('''¡Enhorabuena! encontraste una puerta en el suelo (pero que está cerrada)
110  y un túnel el cual podrás utilizar.''')
111  	enter()
112  	anykey()
113  elif seleccion=='C':
114  	print("Dormiste 18 horas... tienes hambre y sed. Será mejor que salgas de ahí ahora")
115  	enter()
116  	punto-=3
117  	for key, values in opciones5.items(): #OPCIONES 5
118  		print(key,"-",values)
119  	enter()
120  	seleccion=input("Elige opción: ") 
121  	seleccion=seleccion.upper() 
122  	enter()
123  	while not seleccion in opciones5:
124  		print(f"'{seleccion.lower()}'no es una opción válida")
125  		seleccion=input("Elige opcion: ")
126  		seleccion=seleccion.upper()
127  		enter()
128  	if seleccion=='B':
129  		print('''Acabas de descubrir que la carne cruda te gusta...
130  por lo que comienzas a comerte un dedo''')
131  		enter()
132  		anykey()
133  		enter()
134  		print("Mueres debido a la sobredosis de carne consumida")
135  		enter()
136  		puntosObt()
137  		finsi()
138  		exit()
139  	elif seleccion=='C':
140  		print('''Luego de meditar durante 2 días consigues los 7 Chakras logrando aumentar
141  tus capacidades físicas y psíquicas.
142  Además, consigues controlar el 97% de tu actividad cerebral por lo que eres
143  capaz de transformarte en materia oscura, el famoso modo god.''')
144  		enter()
145  		mod=input("Para modificar tiempo y espacio apriete cualquier tecla: ")
146  		punto+=999993
147  		print("--------------------------------------------------------")
148  		puntosObt()
149  		enter()
150  		print("Hola profesor... lo estaba esperando...")
151  		conteo(3)
152  	elif seleccion=='A':
153  		punto+=1
154  		print('''Ugh el sabor dejaba bastante que desear... pero la hidratación te dió fuerzas 
155  para seguir con el escape. ¿Qué deseas hacer? ''')
156  		enter()
157  		del(opciones["C"])
158  		for key, values in opciones.items(): #OPCIONES 1 corta
159  			print(key,"-",values)
160  		enter()
161  		seleccion=input("Elige opción: ")
162  		seleccion=seleccion.upper()
163  		enter()
164  		while not seleccion in opciones:
165  			print(f"'{seleccion.lower()}' no es una opción válida")
166  			seleccion=input("Elige opción: ")
167  			seleccion=seleccion.upper()
168  			enter()
169  		if seleccion=='A':
170  			print("Te diriges hacia la ventana y al mirar hacia afuera te asombras... te encuentras en lo alto de una montaña... nadie te escuchará por lo que decides examinar la habitación") 
171  			enter()
172  			anykey()
173  			punto+=3
174  			enter()
175  			print('''¡Enhorabuena! encontraste una puerta en el suelo (pero que está cerrada)
176  y un túnel el cual podrás utilizar.''')
177  			enter()
178  			anykey()
179  		elif seleccion=='B':
180  			puntos()
181  			enter()
182  			punto+=10
183  			print("Mejoras la habilidad para elaborar herramientas")
184  			enter()
185  			print('''¡Enhorabuena! encontraste una puerta en el suelo (pero que está cerrada)
186  y un túnel el cual podrás utilizar.''')
187  			enter()
188  			anykey()
189  enter()
190  print("Empiezas a arrastrarte...")
191  print("Luego de unos minutos llegas a otra habitación...")
192  enter()
193  print('''¿Qué es esto? Parece una sala de cirugías. Hay una cama llena de sangre y
194  en la pared fotos de cerebros y de pacientes atados.
195  Aquí hay otra puerta... pero también está cerrada''')
196  enter()
197  for key, values in opciones2.items(): #OPCIONES 2
198  	print(key,"-",values)
199  enter()
200  seleccion=input("Elige opción: ")
201  seleccion=seleccion.upper()
202  enter()
203  while not seleccion in opciones2:
204  	print(f"'{seleccion.lower()}'no es una opción válida")
205  	seleccion=input("Elige opción: ")
206  	seleccion=seleccion.upper()
207  	enter()
208  	
209  if seleccion=='A':
210  	print('''IMAGEN >> Aparece Robert, el director del manicomio, con un grupo de médicos. 
211  Se ven sonrientes ya que la operación fue un éxito. Vaya... pobre gente''') 
212  	enter()
213  	anykey()
214  	enter()
215  	punto+=4
216  	for key, values in opciones6.items(): #OPCIONES 6
217  		print(key,'-',values)
218  	enter()
219  	seleccion=input("Elige opción: ")
220  	seleccion=seleccion.upper()
221  	enter()
222  	while not seleccion in opciones6:
223  		print(f"'{seleccion.lower()}' no es una opción válida")
224  		seleccion=input("Elige opcion: ")
225  		seleccion=seleccion.upper()
226  		enter()
227  	if seleccion=='A':
228  		print('''Perfecto, te servirá de prueba para llevarlo a la corte.
229  De repente... escuchas un golpe en la puerta...
230  por lo que decides buscar algo para defenderte''')
231  		enter()
232  		anykey()
233  		enter()
234  		print("Logras sacar un palo de la cama y gracias a la roca del piso lo vuelves filoso. Te servirá como herramienta y arma de defensa")
235  		enter()
236  	elif seleccion=='B':
237  		print('''Mejor olvidar ese pasado oscuro...
238  De repente... escuchas un golpe en la puerta... 
239  por lo que decides buscar algo para defenderte''')
240  		enter()
241  	elif seleccion=='C':
242  		print("Logras sacar un palo de la cama y gracias a la roca del piso lo vuelves filoso. Te servirá como herramienta y arma de defensa")
243  		enter()
244  elif seleccion=='B':#opcion B
245  	puntos()
246  	punto+=10
247  	print("Mejoras la habilidad para luchar")
248  	enter()
249  	print("Logras sacar un palo de la cama y gracias a la roca del piso lo vuelves filoso. Te servirá como herramienta y arma de defensa")
250  	enter()
251  elif seleccion=='C':
252  	print("Mm estaba deliciosa")
253  	enter()
254  	for key, values in opciones7.items():# #OPCIONES 7
255  		print(key,'-',values)
256  	enter()
257  	seleccion=input("Elige opción: ")
258  	seleccion=seleccion.upper()
259  	enter()
260  	while not seleccion in opciones7:
261  		print(f"'{seleccion.lower()}' no es una opción válida")
262  		seleccion=input("Elige opcion: ")
263  		seleccion=seleccion.upper()
264  		enter()
265  	if seleccion=='A' or 'B':
266  		print('''Espera que estas haciendo.. se ve que te ha hecho efecto la sangre...
267  Al cabo de unos minutos te desmayas. Ahora estás en un lugar mejor.''')
268  		enter()
269  		puntosObt()
270  		finsi()
271  for key, values in opciones3.items():# #OPCIONES 3
272  	print(key,'-',values)
273  enter()
274  seleccion=input("Elige opción: ")
275  seleccion=seleccion.upper()
276  enter()
277  while not seleccion in opciones3:
278  	print(f"'{seleccion.lower()}' no es una opción válida")
279  	seleccion=input("Elige opcion: ")
280  	seleccion=seleccion.upper()
281  	enter()
282  
283  if seleccion=='A':
284  	print('''Excelente! Pudiste romper la cerradura. Al abrir la puerta, pisas una baldosa
285  y casi te caes al vacío! Por lo que retrocedes y decides intentar abrir la otra puerta''') 
286  	enter()
287  	anykey()
288  	enter()
289  	punto+=5
290  	print("Al volver, abres exitosamente la puerta! Pero aparece un león hambriento!!")
291  	enter()
292  
293  elif seleccion=='B':#opcion B
294  	puntos()
295  	punto+=10
296  	print("Mejoras la habilidad alpina")
297  	enter()
298  	print("Al volver, abres exitosamente la puerta, pero aparece un león hambriento!!")
299  	enter()
300  
301  for key, values in opciones4.items(): #OPCIONES 4
302  	print(key,"-",values)
303  enter()
304  seleccion=input("Elige opción: ")
305  seleccion=seleccion.upper()
306  enter()
307  while not seleccion in opciones4:
308  	print(f"'{seleccion.lower()}' no es una opción válida")
309  	seleccion=input("Elige opción: ")
310  	seleccion=seleccion.upper()
311  	enter()	
312  
313  if seleccion=='A':
314  	print('''Luego de una lucha de titantes logras escapar del Manicomio. Sientes la brisa
315  del mediodía. Tu próximo desafío será salir de esa montaña...
316  Nos vemos en otro programa''') 
317  	enter()
318  	puntosObt()
319  	finsi()	
320  	exit()
321  elif seleccion=='B':
322  	print('''Te honran en tu lápida por ayudar a la conservación del león ya que estaba
323  en peligro de extinción''')
324  	enter()
325  	puntosObt()
326  	finsi()
327  	exit()