## Tutorial aula SparkR

### Instalação na sandbox 2.4 da Hortonworks

no root, digitar na linha de comando:

```
mv /etc/yum.repos.d/sandbox.repo ~/
mv /etc/yum.repos.d/HDP-UTILS.repo ~/
mv /etc/yum.repos.d/HDP.repo ~/

sudo yum install R
```

### Passo 15 da prática

Usar

`./usr/hdp/current/spark-client/bin/sparkR --packages com.databricks:spark-csv_2.10:1.5.0`
