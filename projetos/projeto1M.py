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
    '''Função que calcula o angulo em função da posição do objeto em um instante de tempo.'''
    if z_0<=0: #quadrante 4 e 3
        teta = -math.atan(x_0/z_0)
    elif x_0<=0 and z_0>0: #quandrante 2 
        teta = math.atan(z_0/x_0) - math.pi/2
    elif x_0>=0 and z_0>0: #quadrante 1 
        teta = math.pi/2 + math.atan(z_0/x_0)
    teta1=math.degrees(teta)
    list_te.append(teta1) #LEMBRAR DE TIRAR
    return teta

#Funções pẽndulo de mola. Os parametros g_0 e gn são genéricos. 
def aceleracao(k,m,r_mod,l0,v_mod,ang):
    '''Função aceleração do pêndulo sem definição de direção'''
    an = (k*(r_mod-l0)/m) + ang*(v_mod**2)/r_mod
    an = round(an,3)
    return an
def incremento(var_t,g_0,pn):
    '''Função genérica de incremento. Soma o termo anterior a um novo, realizado em um pequeno intervalo de tempo.'''
    gn = g_0 + pn*var_t
    gn = round(gn,3)
    return gn

#Função dos gráficos----------------
def plot_graf(listax,listay,nomex,nomey):
	plt.plot(listax,listay)
	plt.xlabel(nomex)
	plt.ylabel(nomey)
	plt.title('Pendulo de mola')
	plt.show()
	plt.close()

#Definindo as listas de dados, master(aninhada) e labels------------------------------- 
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

#-----------Usuário------------------------
print('\n','\n')
print('       Programa numérico pendulo        \n',
      'by José Victor    ','     © Jacks coorp \n', 
      '##### Solução do movimento de um pêndulo de mola #####')
print('Entre com os parametros do problema.')
mass = float(input(' Massa do objeto em kg: '))
kons = float(input(' Constante elastica da mola em N/m: '))
lnat = float(input(' Comprimento natural da mola em m: '))
print('Quais coordenadas de posição inicial do pêndulo em m?')
x_ini = float(input('Em x: '))
x_ini = round(x_ini,3)
z_ini = float(input('Em z: '))
z_ini = round(z_ini,3)
print('Qual intervalo de tempo de oscilação em segundos?')
####t_ini = float(input(' tempo inicial: '))
t_fin = int(input(' tempo final: '))

#Estrutura sequencial-------------------
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
    m_acel = modulo(ax,az)                    #modulo da aceleração
    m_vel = modulo(velx,velz)                 #modulo da velocidade
    m_raio = modulo(x_ini,z_ini)              #modulo do raio
    theta=teta_degrees(x_ini,z_ini)           #Angulo no instante t+n*dt
    t_cont = t_cont + dt                      #contador de tempo
    t_cont = round(t_cont,3)
    ax = - aceleracao(kons,mass,m_raio,lnat,m_vel,math.cos(theta))*(math.sin(theta)) #acel. em x
    az = - g + aceleracao(kons,mass,m_raio,lnat,m_vel,1)*(math.cos(theta)) #acel. em z
    list_ad(z_ini,x_ini,m_raio,velz,velx,m_vel,t_cont,m_acel) #adiciona nas listas
    
#------------Animação do pêndulo------------------
'''# Limite da imagem em função do tamanho da mola
def anime(n):
    spring.set_data([ 0.0, list_x[n] ], [ 0.0, list_z[n] ])
    mass.set_data([ list_x[n] ], [list_z[n]])
    return spring, mass

#Origem = plt.plot([ 0.0 ], [ 0.0 ], 'ro')
n_f=len(list_z)
fig, ax = plt.subplots()
ln, = plt.plot([], [], 'ro', animated = True)
spring, = plt.plot([], [], 'b-', linewidth = 1)
mass, = plt.plot([], [], 'ro', markersize = 5)
plt.xlim(-10.0 * lnat, 10.0 * lnat)
plt.ylim(-8.0 * lnat, 8.0* lnat)
plt.xlabel('Eixo X(m)')
plt.ylabel('Eixo Z(m)')
plt.title('Pendulo de mola')

ani = FuncAnimation(fig, anime, n_f, interval= 0.001, blit=True)
plt.show()
plt.close()'''

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


print('Bye')

'''#if cond == condu:
    print('##### Solução do movimento de um pêndulo simples #####')'''
    