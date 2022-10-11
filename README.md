<h1 align = "center"><b>Projetos de Cálculo Numérico</b></h1>

Esse repositório foi construído para organizar os projetos relacionados a conteúdos de Cálculo Numérico e relacionados.

## **Índice de projetos:**

- [Integral de Riemman](#1-integral-de-riemann)
- [Convolução de Sinais no Tempo Discreto (LSTI)]


## **1. Integral de Riemann**

![Badge Conclusao](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)



### 📄 **Descrição do projeto**:

Esse projeto calcula de forma gráfica as interações de uma integral de riemann sobre uma função $f(x) = -\dfrac{x^3}{100}(10-x)$ no intervalo fechado $[0, 10]$, e mostra o valor aproximado da integração para uma quantidade de retângulos aproximadores de 1 até 100.

### 📲 **Funcionalidades**:

- `Interatividade`: O script utiliza A ferramenta Slider da biblioteca do Streamlit, que permite a variação do parâmetro de entrada que cuida das divisões da área em N retângulos diferentes. E isso trás uma variedade de gráficos para valores diferentes de N.

- `Gráficos`: Com o uso do Matplotlib, é mostrada a função $f(x)$ e também os retângulos alinhados à direita para cada subintervalo.

- `Página web`: Com o uso do Streamlit, também é possível montar um documento semelhante ao markdown para mostrar um pouco da contextualização teórica do problema. Como também é feito no Jupyter Notebook anexado no repositório.


### 🛠️ **Tecnologias utilizadas**:

- [Streamlit](https://streamlit.io/): Tecnologia para gerar o modelo interativo com parâmetros variáveis utilizando sliders.

    ![Na imagem, uma demonstração da utilização do slider, no website gerado pelo Streamlit e verificando a quantidade de retângulos em cima da curva da função.](https://i.imgur.com/CSn6mCl.gif)

- [Numpy](https://numpy.org/): Biblioteca de computação numérica em Python, que organiza as estruturas de dados em arrays e possibilita algumas operações com arranjos n-dimensionais.
- [Matplotlib](https://matplotlib.org/): Biblioteca utilizada para computar graficamente os dados processados através dos arrays do Numpy.


## **2. Convolução de Sinais no Tempo Discreto (LSTI)**
![Badge Conclusao](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)


### 📄 **Descrição do projeto**:

Algoritmo que calcula a convolução numérica de dois sinais descritos por funções de sinais. O modelo matemático utilizado inverte e atrasa um sinal no tempo enquanto mantém o outro, calculando assim a expressão: 

$$
y[n] = x[n]*h[n] = \displaystyle\sum_{\tau = -\infty}^{\infty} x[\tau]h[n-\tau]
$$

### 📲 **Funcionalidades**:

- `Programação Dinâmica`: O script realiza a leitura de arquivos de texto (.txt) para executar código Python. As várias funções de sinais definidas dentro do escopo analisado são produtos da utilização de um arquivo de texto formatado executado através do método `exec()`. 

- `Gráficos`: Com o uso do Matplotlib, é mostrada a função de sinal $x(t)$, $h(t)$ e também a sua convolução, $y(t) = x(t) * h(t)$. Os gráficos, que representam sinais descritos, são construídos utilizando o método `stem`.



### 🛠️ **Tecnologias utilizadas**:

- [Numpy](https://numpy.org/): Biblioteca de computação numérica em Python, que organiza as estruturas de dados em arrays e possibilita algumas operações com arranjos n-dimensionais.
- [Matplotlib](https://matplotlib.org/): Biblioteca utilizada para computar graficamente os dados processados através dos arrays do Numpy.


## **3. Exemplo de Espaço Normado (Geometria do Taxista)**





