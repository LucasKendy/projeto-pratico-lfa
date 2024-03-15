from automathon import DFA

# cada estado representa um estado do treino do aluno
# "I" denota o estado inicial, "F" denota um estado final,
# estados "sk", com k inteiro, denotam estados que representam um treino de membros superiores
# estados "ik", com k inteiro, denotam estados que representam um treino de membros inferiores
# estados "mk", com k inteiro, denotam estados que representam um treino misto de membros inferiores e superiores
Q = {'I', 's1', 's2', 's3', 's4','s5','i1','i2','i3','i4','i5','m1','m2','m3','m4','m5','m6','F'}

# o alfabeto vai consistir dos possíveis exercícios a serem realizados pelo aluno
# AS = aquecimento de membros superiores
# AI = aquecimento de membros inferiores
# ES1, ES2, ..., ES6 = exercício 1 de membros superiores, exercício 2 de membros superiores, ..., exercício 6 de membros superiores
# EI1, EI2, ..., EI6 = exercício 1 de membros inferiores, exercício 2 de membros inferiores, ..., exercício 6 de membros inferiores
sigma = {'AS', 'AI', 'ES1', 'ES2', 'ES3', 'ES4', 'ES5', 'ES6', 'EI1', 'EI2', 'EI3', 'EI4', 'EI5', 'EI6', 'EI7'}

# cada transição de estado acontece a depender do exercício realizado pelo aluno
delta = { 'I' : {'AS' : 's1', 'AI' : 'i1'}, # caso o aluno comece com um aquecimento de membros superiores ou inferiores, o autômato vai esperar reconhecer um treino correspondente
         # também é esperado que o treino do aluno sempre comece com um aquecimento, de outra forma será considerado incorreto
          's1' : {'ES1' : 's2', 'ES2' : 's3', 'AI': 'm1'}, # o aluno pode escolher como primeiro exercícios de membros superiores ES1 ou ES2, ou pode escolher fazer um aqucimento de membros inferiores também, para partir para um treino misto
          's2' : {'ES3' : 's3'}, # caso o aluno tenha escolhido ES1 tal que chegou em s2, tem que também fazer ES3 para ter um treino adequado
          's3' : {'ES4' : 's4'}, # estando no estado de treino s3, o aluno deve, obrigatoriamente, fazer ES4 para progredir
          's4' : {'ES5' : 's5'}, # estando no estado de treino s4, o aluno deve, obrigatoriamente, fazer ES5 para progredir
          's5' : {'ES6' : 'F', 'AI': 'i1'}, # estando no estado de treino s5, o aluno pode escolher ou fazer o ES6 e finalizar seu treino, ou fazer um aquecimento de membros inferiores e fazer um treino de membros inferiores
          'i1' : {'EI1' : 'i2', 'EI2' : 'i2', 'AS': 'm1'}, # o aluno pode escolher como primeiro exercícios de membros inferiores EI1 ou EI2, ou pode escolher fazer um aqucimento de membros superiores também, para partir para um treino misto
          'i2' : {'EI3' : 'i3'}, # estando no estado de treino i2, o aluno deve, obrigatoriamente, fazer EI3 para progredir
          'i3' : {'EI4' : 'i4', 'EI5': 'i3'}, # estando no estado de treino i3, o aluno pode escolher fazer EI4 para progredir, ou pode optar por fazer EI5 e voltar a um estado de treino anterior pare refazer exercícios
          'i4' : {'EI6' : 'i5'}, # estando no estado de treino i4, o aluno deve, obrigatoriamente, fazer EI6 para progredir
          'i5' : {'EI7' : 'F', 'AS': 's1'}, # estando no estado de treino i5, o aluno pode escolher ou fazer o EI7 e finalizar seu treino, ou fazer um aquecimento de membros inferiores e fazer um treino de membros inferiores
          'm1' : {'ES1': 'm2', 'EI1': 'm2'}, # em um treino misto, estando no estado m1, o aluno pode escolher fazer tanto exercícios de membros superiores ES1 ou de membros inferiores EI1 para progredir
          'm2' : {'ES2': 'm3', 'EI3': 'm3'}, # em um treino misto, estando no estado m2, o aluno pode escolher fazer tanto exercícios de membros superiores ES2 ou de membros inferiores EI2 para progredir
          'm3' : {'ES3': 'm4', 'EI4': 'm4'}, # em um treino misto, estando no estado m3, o aluno pode escolher fazer tanto exercícios de membros superiores ES3 ou de membros inferiores EI3 para progredir
          'm4' : {'ES4': 'm5'}, # em um treino misto, estando no estado m4, o aluno deve fazer ES4 para progredir
          'm5' : {'EI4': 'm6', }, # em um treino misto, estando no estado m5, o aluno deve fazer EI4 para progredir
          'm6' : {'ES5': 'F', 'EI5': 'F', 'AS': 's1', 'AI': 'i1'}, # em um treino misto, estando no estado m6, pode escolher entre fazer ES5 ou EI5 para progredir e finalizar seu treino, ou fazer aquecimentos AS ou AI para realizar, também, os treinos correspondentes
          }
initial_state = 'I'

# existe somente um estado final, que é o estado em que o aluno completou o treino corretamente
# caso o aluno tenha feito algum exercício em ordem incorreta, ou parado o treino antes do esperado sem realizar todos os exercícios,
# o autômato não vai reconhecer a palavra (o que denotará que o treino feito pelo aluno não foi correto), ou porque acabou em um estado não final ou porque ocorreu alguma transição não prevista

F = {'F'}

automata = DFA(Q, sigma, delta, initial_state, F)

automata.view(
    file_name="checador-rotina-exercicios",
    node_attr={'fontsize': '20'},
    edge_attr={'fontsize': '20pt'}
)