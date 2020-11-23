from math import log10

def sinal(x):
    '''Função sinal. Retorna -1 se x<0, 0 se x=0 e 1 se x>0.'''
    if x>0:
        return 1.0
    elif x<0:
        return -1.0
    else:
        return 0.0

def raizbi(f,a,b,dx=0.002):
    '''Método da busca incremetal de raíz.\nProcura uma raíz no intervalo [a,b]. Retorna um resultado (raiz,erro).'''
    x1=a
    f1=f(x1)
    x2=a+dx
    f2=f(x2)
    while sinal(f1)==sinal(f2):
        if x1>=b:
                return str('Sem raíz no intervalo '+'['+str(a)+','+str(b)+']')
        x1=x2
        f1=f(x1)
        x2=x1+dx
        f2=f(x2)
        media=(x1+x2)/2
    return media

def eq_geral(H):
    Ka=1.75e-5
    Ca=0.1
    Cs=0.01
    Kw=1e-14
    return H**3+(Cs+Ka)*H**2-(Kw+Ka*Ca)*H-Ka*Kw  

resultado=raizbi(eq_geral,1e-7,1,1e-8) 
resultado=round(-log10(resultado),3)
erro=abs(round(100*(resultado-3.757)/resultado,3))
print('Valor sem aproximar=', resultado)
print('Aproximação de Henderson-Hasselbach = 3.757')
print('Erro em relação a aproximação =',str(erro)+'%')
    
    
    
