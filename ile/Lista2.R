#Lista2
diretorio <- "D:\\Google Drive\\Pos-Graduação\\Ciencia de Dados e Big Data\\Introdução às Linguagens Estatísticas\\Listas\\"
setwd(diretorio)
#Questão 2.1
arquivo<-"20170501_CEIS.csv"
df <- read.csv(arquivo, sep = ';', header=TRUE)
print(dim(df)[1])
#Questão 2.2
library(readxl)
library(openxlsx)
arquivo<- "DadosColetados_PerfilGovTI 2014.xlsx"
df <- read_excel(arquivo,skip=2)
print(dim(df)[1])
#Questão 2.3
library(sqldf)
conexao <- file('ESCOLAS.CSV')
escolas_rio <- sqldf('select * from conexao where  FK_COD_MUNICIPIO == 3304557 and ID_DEPENDENCIA_ADM == 3', file.format = list(sep='|'))
print(head(escolas_rio))