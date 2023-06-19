

<h1 align="center">
  Airbnb - Predict
</h1>



## 💻 Projeto
Qual deverá ser o preço de aluguel do meu imóvel no Airbnb? (Apenas para RJ) - em Python com Pandas e SKlearn

Dando os devidos créditos e seguindo (parcialmente) os passos dessa análise: https://lnkd.in/d_UJyJzW

Recriei esse estudo para calcular qual "deverá" ser o valor cobrado ao alugar seu imóvel no RJ, utilizando algumas características do local como parâmetros para esse ensaio.

A base de dados que tive acesso foi de 2018 ao início de 2020. Tentei atualizar, mas há uma cobrança pelos dados mais atuais, então, deixei de lado(rs).

Alguns dos parâmetros de entrada são: latitude, longitude, número de quartos, camas, banheiros, quantos pessoas cabem, mês, ano...

Quanto ao resultado, achei interessante que o peso do mês e do ano não tiveram tanto impacto quanto pensei. Imaginava que a sazonalidade no Rio seria maior. Os parâmetros com maiores significância no peso do preço foram: quantidade de quartos, latitude, longitude e amenities(que seriam as comodidades).

Quem quiser dar uma olhadinha mais a fundo, embaixo está o repo que rodei a análise, que tem algumas explicações a mais.
Mas, resumidamente, os dados foram extraídos e valores irrelevantes, nulos ou que se destacavam dos demais foram tratados. Depois, foram rodados três modelos de previsão e foi escolhido o com 97% de assertividade. Por fim, o modelo treinado foi extraído para ser salvo.


## 🔨 Implementações

- [X] Análise dos dados
- [X] Visualização em gráficos
- [X] Previsão de preços


## ✨ Tecnologias

- [X] Pandas
- [X] sklearn
- [X] seaborn

