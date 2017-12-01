#Questão 1
vec<-c(26, NA, 72, 45, 12, 16, NA, 8)
#a)
vec1<-vec[c(1,length(vec))]
print(vec1)
#b)
print(append(vec,c(24, 13, 42),3))

#c)
print(prod(vec,na.rm = TRUE))

#d)
vec2<-vec[!is.na(vec)]
print(vec2)

#e)
print(vec2[vec2>mean(vec2)])

#f)
print()

#g
vec3<- c(14, 27, 45, 72, 19, -12)
vec4<- c(6, 9, 8, NA, 7, 5)
print(vec3+vec4+5)

#h

