# dados de uma classe do ensino médio
#           N,  Nome,             por,mat,qui,fis,bio,his,geo,soc,fil,ing,art
classe = [[ 123,'Joao da Silva', [9.0,8.5,7.5,4.5,8.5,9.0,6.5,8.5,9.0,6.0,9.5]],\
          [ 273,'José de Souza', [7.5,4.5,9.0,6.0,8.5,9.0,6.5,8.5,9.5,9.0,8.5]],\
          [ 391,'Luana Alves',   [9.5,9.0,8.5,7.5,8.5,9.0,6.5,8.5,4.5,9.0,6.0]],\
          [ 465,'Maria Silva',   [8.5,9.0,7.5,4.5,9.0,6.0,9.0,8.5,6.5,8.5,9.5]]]

def existeOAluno (num):
    linha = 0
    while linha <len(classe):
        if classe [linha][0]==num:
            return True

            linha += 1

    return False


