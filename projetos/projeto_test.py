#PROJETO 1M 
#Nesse projeto criei um programa que resolve numericamente um pendulo de mola e um pendulo simples.

#Módulos usados ----------
import math
import matplotlib.pyplot as plt
import numpy as np                   #Biblioteca pra trabalhar com matrizes.
from matplotlib.animation import FuncAnimation  #classe de animação

#----------Definindo as funções-----------------------
#Função que gera arquivo de saida --------
def table_txt(l_generic,l_nomes,name):
    arq = open(name+".txt","w")
    arq.write(22*'  '+sistema+'\n')
    for n in l_nomes:
        arq.write(2*' '+ n +' ')
    arq.write('\n')
    for (i,valor) in enumerate(l_generic):
        arq.write(4*' '+ str(s1[i])+9*' '+ str(s2[i])+9*' '+ str(s3[i]) +9*' '+ str(s4[i])+9*' '+ str(s5[i])+9*' '+ str(s6[i])+9*' '+ str(s7[i])+9*' '+ str(s8[i]))
        arq.write('\n')
    arq.close()

#Função modulo e angulo---------------------
def modulo(g1,g2):
    '''Essa função calcula o módulo de um vetor genérico, usando a equação:\n
            |G| = sqrt(G1² + G2²)        '''
    g_mod = math.sqrt(g1*g1 + g2*g2)
    g_mod=round(g_mod,3)         #Limitar resultado a 4 casas decimais
    return g_mod

def teta_degrees(x_0,z_0):
    '''Função que calcula o angulo de inclinação em relação ao eixo do pêndulo em cada instante de tempo e para cada condição especifica.'''
    if z_0==0:
        teta = -math.atan(x_0/0.0001)
    elif z_0<0: #quadrante 4 e 3
        teta = -math.atan(x_0/z_0)
    elif x_0<0 and z_0>0: #quandrante 2 
        teta = math.atan(z_0/x_0) - math.pi/2
    elif x_0>0 and z_0>0: #quadrante 1 
        teta = math.pi/2 + math.atan(z_0/x_0)
    elif x_0 ==0 and z_0>0:
        teta = math.pi
    teta1=math.degrees(teta)
    list_te.append(teta1) #LEMBRAR DE TIRAR
    return teta

#Funções pêndulo de mola e simples. Os parametros g_0 e gn são genéricos. 
def aceleracao(k,m,r_mod,l0,v_mod):
    '''Função aceleração do pêndulo simples e de mola, sem definição de direção. Ela serve para o caso simples, quando o parametro k=0 e para mola, quando v_mod=0'''
    an = (bin3)*(2*k*(r_mod-l0)/m) - (bin1)*g*math.cos(theta) - (bin2)*2*(v_mod*v_mod)/l0
    an = round(an,3)
    return an

def incremento(var_t,g_0,pn):
    '''Função genérica de incremento. Soma o termo anterior a um novo, realizado em um pequeno intervalo de tempo.'''
    gn = g_0 + pn*var_t
    gn = round(gn,3)
    return gn

def energia(k,m,r_mod,l0,v_mod):
    en = k*((r_mod-l0)*(r_mod-l0))/2 +m*g*r_mod + m*(v_mod*v_mod)/2
    return en

#Função dos gráficos----------------
def plot_graf(listax,listay,nomex,nomey):
	plt.plot(listax,listay)
	plt.xlabel(nomex)
	plt.ylabel(nomey)
	plt.title(sistema)
	plt.show()
	plt.close()

#Função adiciona lista-------------------
def list_ad(l1,l2,l3,l4,l5,l6,l7,l8):
    list_z.append(l1)
    list_x.append(l2)
    list_mod_raio.append(l3)
    list_velz.append(l4)
    list_velx.append(l5)
    list_mod_vel.append(l6)
    list_time.append(l7)
    list_mod_acel.append(l8)

#---------------USUÁRIO ------------------------
print('\n','\n')
print('       ','Programa numérico pendulo \n',
      'by José Victor    ','     © Jacks coorp \n')
cond4='s'
while cond4=='s':                  #Condição de loop fim - inicio do programa
	cond0=1
	while cond0 ==1 or 2:
		print('       ','Menu incial \n Digite 1 para Pêndulo de Mola e 2 para Pêndulo simples.')
		cond0 = int(input('====> '))
	#Pendulo de mola parametros:
		if cond0==1:
			print('##### Solução do movimento de um pêndulo de mola #####')
			print('Entre com os parametros do problema.')
			mass = float(input(' Massa do objeto em kg: '))
			kons = float(input(' Constante elastica da mola em N/m: '))
			lnat = float(input(' Comprimento natural da mola em m: '))
			print('Quais coordenadas de posição inicial do pêndulo em m?')
			x_ini = float(input('Em x: '))
			x_ini = round(x_ini,3)
			z_ini = float(input('Em z: '))
			z_ini = round(z_ini,3)
			print('Qual tempo de oscilação em segundos?')
			t_fin = int(input(' tempo final: '))
	#condições para formatação pendulo de mola ------
			sistema = 'Pêndulo de mola'
			bin1 = 1
			bin2 = 0  #Condição para função funcionar no p.mola.
			bin3 = 1
			string_energ = 'mgr + m|v|²/2 + [k(r-l0)²]/2 = cte'
			break

	#Pendulo de simples parametros:
		if cond0==2:
			print('##### Solução do movimento de um pêndulo simples #####')
			print('Entre com os parametros do problema.')
			mass = float(input(' Massa do objeto em kg: '))
			print('Quais coordenadas de posição inicial do pêndulo em m?')
			x_ini = float(input('Em x: '))
			x_ini = round(x_ini,3)
			z_ini = float(input('Em z: '))
			z_ini = round(z_ini,3)
			lnat = modulo(z_ini,x_ini)
			print('O tamanho do fio é ',lnat,' m')
			print('Qual tempo de oscilação em segundos?')
			t_fin = int(input(' tempo final: '))
	#condições para formatação pendulo simples -----
			sistema = 'Pêndulo simples'
			kons = 0
			bin1 = -1
			bin2 = -1 #Condição para função funcionar no p.Simples
			bin3 = 0
			string_energ = 'mgr + m|v|²/2 = cte'
			break
		else:
			print('Opção invalida. \n')

	#Definindo as listas de dados, master(aninhada) e labels. Tambem ZERA listas e variaveis pra nova aplicação------------------------------- 
	list_te = [] #LEMBRAR DE TIRAR
	s1=list_z = []
	s2=list_x = []
	s3=list_velz = []
	s4=list_velx = []
	s5=list_mod_vel = []
	s6=list_time = []
	s7=list_mod_raio = []
	s8=list_mod_acel = []
	list_master = [s1,s2,s3,s4,s5,s6,s7,s8]
	list_label = ["Eixo Z(m)","Eixo x(m)","Vel. z(m/s)","Vel. x(m/s)", "velocidade(m/s)", "Tempo(s)","Posição(m)","Aceleração(m/s²)"]

	#--------Estrutura sequencial------------------
	ax=0.000
	az=0.000
	t_cont=0.000
	velx=0.000
	velz=0.000
	g=9.780318   #no nivel do mar
	dt=0.006      #variação de tempo

	while t_cont<=t_fin:
	    velx = incremento(dt,velx,ax)             #incremento em Vx
	    velz = incremento(dt,velz,az)             #incremento em Vz
	    x_ini = incremento(dt,x_ini,velx)         #incremento em X
	    z_ini = incremento(dt,z_ini,velz)         #incremento em Z
	    theta=teta_degrees(x_ini,z_ini)           #Angulo no instante t+n*dt    
	    m_acel = modulo(ax,az)                    #modulo da aceleração
	    m_vel = modulo(velx,velz)                 #modulo da velocidade
	    m_raio = modulo(x_ini,z_ini)              #modulo do raio
	    t_cont = t_cont + dt                      #contador de tempo
	    t_cont = round(t_cont,3)
	    ax = - aceleracao(kons,mass,m_raio,lnat,m_vel)*(math.sin(theta)) #acel. em x
	    az = - g + aceleracao(kons,mass,m_raio,lnat,m_vel)*(math.cos(theta)) #acel. em z
	    list_ad(z_ini,x_ini,m_raio,velz,velx,m_vel,t_cont,m_acel) #adiciona nas listas

	#------Conservação de energia------------
	n_q = len(s7)
	cc=n_q-1
	ei = energia(kons,mass,s7[0],lnat,s5[0])  
	ei = round(ei,3) #energia inicial
	ef = energia(kons,mass,s7[cc],lnat,s5[cc])
	ef = round(ef,3) #energia final
	print('\n',7*' ',' Energia do sistema\n', 
	      'Todas as forças envolvidas são conservativas, isso significa que a energia deve se conservar. \n',
	       9*' ',string_energ,'\n	\n')         
	print('Energia inicial = {} J e Energia final = {} J.'.format(ei,ef))
	if ei == ef:
	    print('Energia se conserva!')
	else:
	    print('A energia não se conservou.\n')

	#--------------Interação gráfica------------------
	cond1=input('Deseja visualizar no gráfico? [s/n]: ')
	while cond1=='s': 
		print('Escolha entre as opções abaixo: ')
		for (i, valor) in enumerate(list_label):
		    print(i, valor)
		opx=int(input('Eixo x '))
		opz=int(input('Eixo z '))
		plot_graf(list_master[opx], list_master[opz], list_label[opx], list_label[opz])	
		cond1=input('Deseja visualizar outro gŕafico? [s/n]: ')

	#-------------------Saida dos dados ---------------------------	
	cond2=input('Deseja salvar os resultados em arquivo? [s/n] ')
	if cond2=='s':
		n_arq=input('Nome do arquivo de saida: ')
		table_txt(list_x,list_label,n_arq)

	#------------Animação do pêndulo------------------
	cond3=input('Deseja ver animação do pêndulo? [s/n] ')
	if cond3=='s':
		#Origem = plt.plot([ 0.0 ], [ 0.0 ], 'ro')
		fig, ax = plt.subplots()
		ln, = plt.plot([], [], 'ro', animated = True)
		spring, = plt.plot([], [], 'b-', linewidth = 2)
		mass, = plt.plot([], [], 'ro', markersize = 4)
		xdata, ydata = list_x , list_z

		def init():
		    plt.xlim(-9.0 * lnat, 9.0 * lnat)
		    plt.ylim(-8.0 * lnat, 8.0* lnat)
		    return ln,

		def anime(n):
		    spring.set_data([ 0.0, list_x[n] ], [ 0.0, list_z[n] ])
		    mass.set_data([ list_x[n] ], [list_z[n]])
		    ln.set_data(xdata[n], ydata[n])
		    return spring, mass

		plt.xlabel('Eixo X(m)')
		plt.ylabel('Eixo Z(m)')
		plt.title(sistema)
		ani = FuncAnimation(fig, anime, n_q, interval=0.006, init_func=init, blit=True)
		plt.show()
		plt.close()
	cond4=input('Deseja voltar para o menu inicial? [s/n] ')
	print('\n')
print('Bye')    
