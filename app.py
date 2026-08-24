import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

CAPACIDADE = 50.0
SLA_MS = 200.0

st.set_page_config(
    page_title="Análise de desempenho da API",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>

    * {
        font-family: 'Arial', sans-serif;
        font-size: 1.8rem;
    }

    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
    }

    .formula {
        padding: 0.9rem 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 2rem;
        font-weight: 600;
        margin: 1rem 0;
    }

    .details {
        font-size: 1.7rem;
        margin-top: 0.5rem;
        background-color: #f0f0f0;
        padding: 0.8rem;
        border-radius: 8px;
    }

        /* Ver informações sobre o modelo */
        [data-testid="stExpander"] summary p {
        font-size: 1.8rem !important;
        font-weight: 600;
        #Comando acima para modificar o texto do botão do expandir

    </style>
    """,
    unsafe_allow_html=True,
)


def tempo_resposta(resposta):
    # Modelo: T(r) = 1000 / (50 - r)
    return 1000.0 / (CAPACIDADE - resposta)


st.markdown(
    '<div class="main-title">📊 Análise de desempenho da API</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
        'Modelo matemático para analisar o tempo de resposta conforme a carga aumenta.'
    '</div>',
    unsafe_allow_html=True,
)


with st.container(border=True):

    st.markdown("### Modelo matemático")

    st.markdown(
        '<div class="formula">'
            'T(r) = 1000 / (50 − r)'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="details">'
            '<b>(R)</b> representa a carga em requisições por segundo (req/s) || ' 
            '<b> T(R) o tempo médio de resposta (ms).</b> || '
            ' A capacidade estimada é <b>50 req/s</b>.'
        '</div>',
        unsafe_allow_html=True,
    )


st.markdown("### 🎚️ Controle de carga")

r = st.slider(
    "Quantidade de requisições por segundo",
    min_value=0.0,
    max_value=49.99,
    value=40.0,
    step=0.1,
)


t = tempo_resposta(r)
distancia = CAPACIDADE - r


col1, col2, col3 = st.columns(3)

col1.metric(
    "Carga selecionada",
    f"{r:.1f} req/s"
)

col2.metric(
    "Tempo previsto",
    f"{t:.2f} ms"
)

col3.metric(
    "Margem até a capacidade",
    f"{distancia:.1f} req/s"
)


if r >= 48:

    st.error(
        "🔴 Região crítica: a carga está muito próxima da capacidade estimada. "
        "O modelo prevê crescimento muito acentuado do tempo de resposta."
    )

elif r >= 45:

    st.warning(
        "🟠 Atenção: a carga está na região em que o tempo previsto "
        "atinge ou ultrapassa o SLA de 200 ms."
    )

else:

    st.success(
        "🟢 A carga está abaixo da região crítica definida nesta análise."
    )


if t <= SLA_MS:

    st.info(
        f"Tempo previsto: **{t:.2f} ms** — "
        f"dentro do SLA de referência de **{SLA_MS:.0f} ms**."
    )

else:

    st.warning(
        f"Tempo previsto: **{t:.2f} ms** — "
        f"acima do SLA de referência de **{SLA_MS:.0f} ms**."
    )


st.markdown("### 📈 Comportamento do modelo")

# Evita desenhar o ponto r=50,
# onde a função não é definida.
x = np.linspace(0, 49.99, 800)
y = tempo_resposta(x)


fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    x,
    y,
    linewidth=2,
    label="T(r) = 1000 / (50 - r)"
)

ax.axvline(
    CAPACIDADE,
    linestyle="--",
    label="Assíntota: r = 50 req/s"
)

ax.axvspan(
    45,
    49.9,
    alpha=0.12,
    label="Região crítica: r ≥ 45"
)

ax.scatter(
    [r],
    [t],
    s=80,
    zorder=5,
    label="Carga selecionada"
)

ax.axhline(
    SLA_MS,
    linestyle=":",
    label="SLA: 200 ms"
)

ax.set_xlabel(
    "Carga (requisições por segundo)"
)

ax.set_ylabel(
    "Tempo médio de resposta (ms)"
)

ax.set_xlim(
    0,
    50.5
)

ax.set_ylim(
    0,
    min(max(550, t * 1.1), 1200)
)

ax.grid(
    True,
    alpha=0.25
)

ax.legend()

st.pyplot(fig)

plt.close(fig)


st.markdown("### 📌 Interpretação")

st.markdown(
    '<div class="details">'
        'Quanto mais a carga se aproxima de 50 req/s pela esquerda, menor fica o '
        'denominador da função e maior fica o tempo previsto. Portanto, operar '
        'continuamente perto da capacidade máxima reduz a margem de segurança.'
    '</div>',
    unsafe_allow_html=True,
)


with st.expander("Ver informações sobre o modelo"):

    st.markdown(
        '<div class="details">'
            '<b>Capacidade estimada:</b> 50 req/s<br>'
            '<b>SLA de referência:</b> 200 ms<br>'
            '<b>Limite crítico:</b> r = 45 req/s<br>'
            '<b>Assíntota vertical:</b> r = 50 req/s<br>'
            '<b>Domínio operacional:</b> 0 ≤ r &lt; 50'
        '</div>',
        unsafe_allow_html=True,

    )



st.markdown(
    '<div class="details">'
        '<b>Observação:</b> o modelo é uma aproximação matemática baseada nos dados '
        'fornecidos no teste de carga; não substitui medições reais de latência, '
        'throughput, erros, CPU, memória, banco de dados e comportamento sob concorrência.'
    '</div>',
    unsafe_allow_html=True,
)


