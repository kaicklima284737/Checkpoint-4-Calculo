# Checkpoint 4 — Limites, Desempenho de APIs e Streamlit

Projeto aplicado de modelagem matemática para análise do tempo de resposta de uma API conforme a carga aumenta.

## Arquivos

- `checkpoint.ipynb` — notebook principal, com a análise matemática, limites, simulações, gráficos, interpretações e o código completo que gera `app.py`, com explicações detalhadas sobre o conteúdo.
- `app.py` — aplicação interativa em Streamlit. Pode ser atualizado / reescrito no item ## 7. Aplicação interativa em Streamlit ## com uso de Path e código salvo no arquivo. Pode ser atualizado rodando o código do item 7.
- `requirements.txt` — dependências necessárias.
- `README.md` — instruções de execução.

## Modelo

O modelo adotado é:

$$
T(r)=\frac{1000}{50-r}
$$

onde:

- **`r`** é a carga em requisições por segundo (req/s);
- **`T(r)`**** é o tempo médio de resposta em milissegundos (ms);
- **`50 req/s`** é a capacidade máxima estimada no enunciado.

O modelo reproduz exatamente os valores fornecidos no teste de carga para 10, 20, 30, 35, 40, 45 e 48 req/s.

## Limite principal

$$
\lim_{r\to50^-}\frac{1000}{50-r}=+\infty
$$

Isso representa matematicamente uma assíntota vertical em `r = 50`. No contexto operacional, significa que a aproximação da capacidade estimada reduz fortemente a margem de segurança e faz o tempo de resposta crescer de forma muito acentuada.

## SLA de referência

Para tornar a análise operacional, o projeto adota **200 ms como SLA de referência**. Esse valor é uma premissa de análise, após analise do modelo e determinação do ponto máximo que a API funciona antes do crescimento ficar inviável.

Pelo modelo:

$$
T(45)=200\text{ ms}
$$

Assim, a região `r >= 45 req/s` é tratada como crítica nesta análise.

## Como executar

### 1. Instalar dependências

Instalar depêndencias do Arquivo para execução do código.

```bash
pip install -r requirements.txt

ou

py -m pip install -r requirements.txt
```

### 2. Executar o notebook

Abra `checkpoint.ipynb` no Jupyter Notebook, JupyterLab ou VS Code (Arquivo onde foi feito o código.) e execute todas as células em ordem, caso as instalações das dependências não derem para ser feitas.

O notebook contém uma célula que gera/atualiza o arquivo `app.py` e uma página dedicada na instalação dos recursos necéssarios para instalação deixadas como comentário. Caso não tenha as bibliotecas instaladas, é necessário visualizar o item 1, e instalar os arquivos %pip.

### 3. Executar o Streamlit

Depois de gerar o arquivo, execute no terminal do app.py ou pasta que o arquivo está localizado:

```bash
streamlit run app.py
```

Caso não consiga carregar utilizando o comando acima, execute o comando alternativo:
```bash
py -m streamlit run app.py
```

```bash
OBS:
```
Verifique se o caminho do arquivo está dentro do caminho:
```bash
PS C:\Users\user\Downloads\CP4 Cálculo>
```
Ou onde está localizado o arquivo, antes de executar os comandos no terminal, para evitar erro de não encontrar arquivo.

## Decisões técnicas

A capacidade teórica de 50 req/s não deve ser interpretada como uma capacidade segura de operação. O modelo mostra que o desempenho já se torna crítico antes desse ponto.

Recomenda-se preservar margem de capacidade e investigar escalabilidade horizontal/vertical, balanceamento de carga, cache, otimização de consultas e processamento assíncrono conforme os gargalos observados em medições reais.

| Nome:| RM:|
| ---:| ---:|
|Kaick Lima Silva       | 574060 |
|Gustavo Basso          | 572623 |
|Guilherme Salles       | 572933 |
|Pedro Feltrin          | 569038 |
|Guilherme Kozikoski    | 571611 |
