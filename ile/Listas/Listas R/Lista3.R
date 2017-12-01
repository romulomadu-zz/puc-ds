#3.1
df<-mtcars
print(head(df))    
#3.2
print(names(df))
#3.3
print(c("Linhas: ",dim(df)[1],"Colunas: ",dim(df)[2]))
#3.4
print(mean(df$mpg))
#3.5
print(c("Max:",max(df$disp),"Min:",min(df$disp)))  
#3.6
print(cor(df["mpg"],df['wt']))
#3.7
print(df[df$mpg>20 & df$hp>90,])
#3.8
names(df)[names(df) == 'carb'] <- 'qtd_carburadores'
print(names(df))
#3.9
df<-within(df, rm("qsec"))
print(names(df))
#3.10
dfs <- subset(df,select = c("mpg", "wt", "cyl"))
print(head(dfs))
#3.11
dfs <- dfs[,c("cyl", "mpg", "wt")]
print(colnames(dfs))
#3.12
print(rownames(dfs))
#3.13
print(dfs[rownames(dfs)==rownames(dfs)[15],])
#3.14
print(mean(dfs[dfs$cyl==6,]$mpg))
#3.15
print(max(dfs$cyl)*min(dfs$wt))
#3.16
mask <- rownames(dfs)==rownames(dfs)[4]|rownames(dfs)==rownames(dfs)[10]|rownames(dfs)==rownames(dfs)[19]
print(df[mask,c("mpg", "drat", "vs")])
#3.17
print(sum(df$cyl+df$qtd_carburadores))

