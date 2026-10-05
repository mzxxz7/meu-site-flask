from flask import Flask, render_template_string, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

# ============================================================
# CONFIGURAÇÕES
# ============================================================

NOME_ESTETICA = "Fernanda Feminina"
WHATSAPP = "5534998882876"
INSTAGRAM = "@fernandafeminina"
ENDERECO = "Rua Aristides Mendonça, 25 - Taiaman, Uberlândia - MG"

# ============================================================
# HORÁRIOS
# ============================================================

def gerar_horarios():
    """
    Gera horários entre 08:00 e 19:00.
    Intervalo padrão de 45 minutos.
    Você pode alterar para 30, 45, 50 ou 55 minutos.
    """

    horarios = []

    inicio = datetime.strptime("08:00", "%H:%M")
    fim = datetime.strptime("19:00", "%H:%M")

    intervalo = timedelta(minutes=45)

    horario_atual = inicio

    while horario_atual <= fim:
        horarios.append(horario_atual.strftime("%H:%M"))
        horario_atual += intervalo

    return horarios


HORARIOS = gerar_horarios()

# ============================================================
# HTML DA PÁGINA
# ============================================================

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Fernanda Feminina | Estética</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: "Segoe UI", Arial, sans-serif;
            background: #f8f0eb;
            color: #4d3935;
        }

        /* =========================
           HEADER
        ========================= */

        header {
            background: #f4dfd9;
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 15px rgba(80, 50, 40, 0.08);
        }

        .logo {
            font-size: 26px;
            font-weight: 600;
            color: #9b6b68;
        }

        nav a {
            text-decoration: none;
            color: #654c48;
            margin-left: 25px;
            font-size: 15px;
        }

        nav a:hover {
            color: #b87978;
        }

        /* =========================
           HERO
        ========================= */

        .hero {
            min-height: 600px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 80px 20px;

            background:
                linear-gradient(
                    rgba(248, 240, 235, 0.88),
                    rgba(248, 240, 235, 0.95)
                ),
                radial-gradient(
                    circle at top right,
                    #e9c5c2,
                    transparent 40%
                );
        }

        .hero-content {
            max-width: 800px;
        }

        .hero h1 {
            font-family: Georgia, serif;
            font-size: 65px;
            color: #8f6260;
            margin-bottom: 20px;
        }

        .hero h2 {
            font-weight: 400;
            font-size: 25px;
            color: #705451;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 17px;
            line-height: 1.8;
            max-width: 650px;
            margin: auto;
            color: #735e59;
        }

        .botao {
            display: inline-block;
            margin-top: 30px;
            padding: 15px 30px;
            border-radius: 30px;
            background: #b77b78;
            color: white;
            text-decoration: none;
            font-weight: 600;
            transition: 0.3s;
        }

        .botao:hover {
            background: #965f5d;
            transform: translateY(-2px);
        }

        /* =========================
           SEÇÕES
        ========================= */

        section {
            padding: 80px 8%;
        }

        .titulo {
            text-align: center;
            margin-bottom: 45px;
        }

        .titulo h2 {
            font-family: Georgia, serif;
            font-size: 38px;
            color: #8f6260;
            margin-bottom: 10px;
        }

        .titulo p {
            color: #806a65;
        }

        /* =========================
           SERVIÇOS
        ========================= */

        .servicos {
            background: #fffaf7;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
            max-width: 1000px;
            margin: auto;
        }

        .card {
            background: #f7e7e2;
            padding: 35px 25px;
            text-align: center;
            border-radius: 20px;
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(100, 60, 50, 0.1);
        }

        .card .icone {
            font-size: 40px;
            margin-bottom: 15px;
        }

        .card h3 {
            color: #8f6260;
            margin-bottom: 10px;
        }

        .card p {
            color: #806a65;
            line-height: 1.6;
        }

        /* =========================
           AGENDAMENTO
        ========================= */

        .agendamento {
            background: #f2dfda;
        }

        .agenda-container {
            max-width: 850px;
            margin: auto;
            background: #fffaf7;
            padding: 40px;
            border-radius: 25px;
            box-shadow: 0 10px 35px rgba(80, 50, 40, 0.08);
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        label {
            font-weight: 600;
            color: #684e49;
        }

        input,
        select {
            width: 100%;
            padding: 14px;
            border: 1px solid #dec4bd;
            border-radius: 10px;
            background: white;
            color: #604a45;
            font-size: 15px;
            margin-top: 7px;
        }

        input:focus,
        select:focus {
            outline: none;
            border-color: #b77b78;
        }

        .horarios {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin-top: 10px;
        }

        .horario {
            border: 1px solid #d9b8b2;
            background: #fff;
            padding: 12px;
            border-radius: 10px;
            cursor: pointer;
            text-align: center;
            transition: 0.2s;
        }

        .horario:hover {
            background: #f1d9d5;
        }

        .horario input {
            display: none;
        }

        .horario:has(input:checked) {
            background: #b77b78;
            color: white;
            border-color: #b77b78;
        }

        .botao-agendar {
            border: none;
            padding: 16px;
            border-radius: 30px;
            background: #a96d6a;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        .botao-agendar:hover {
            background: #8f5c59;
        }

        .aviso {
            background: #f8ebe7;
            border-left: 4px solid #b77b78;
            padding: 18px;
            margin-top: 25px;
            border-radius: 8px;
            line-height: 1.6;
        }

        /* =========================
           CONTATO
        ========================= */

        .contato {
            background: #fffaf7;
            text-align: center;
        }

        .contato-box {
            max-width: 700px;
            margin: auto;
        }

        .contato p {
            margin: 15px 0;
            font-size: 17px;
        }

        .whatsapp {
            background: #7eaa7b;
        }

        .whatsapp:hover {
            background: #628d60;
        }

        /* =========================
           RODAPÉ
        ========================= */

        footer {
            background: #5f4743;
            color: #f9eeeb;
            text-align: center;
            padding: 30px 20px;
        }

        footer p {
            margin: 7px;
        }

        /* =========================
           RESPONSIVO
        ========================= */

        @media (max-width: 800px) {

            header {
                flex-direction: column;
                gap: 15px;
            }

            nav a {
                margin: 0 7px;
            }

            .hero h1 {
                font-size: 45px;
            }

            .cards {
                grid-template-columns: 1fr;
            }

            .horarios {
                grid-template-columns: repeat(3, 1fr);
            }

            .agenda-container {
                padding: 25px;
            }
        }

        @media (max-width: 450px) {

            .horarios {
                grid-template-columns: repeat(2, 1fr);
            }

            .hero h1 {
                font-size: 38px;
            }
        }

    </style>

</head>

<body>

<!-- =====================================================
     HEADER
===================================================== -->

<header>

    <div class="logo">
        Fernanda Feminina
    </div>

    <nav>
        <a href="#inicio">Início</a>
        <a href="#servicos">Serviços</a>
        <a href="#agendamento">Agendamento</a>
        <a href="#contato">Contato</a>
    </nav>

</header>


<!-- =====================================================
     HERO
===================================================== -->

<section class="hero" id="inicio">

    <div class="hero-content">

        <h1>Fernanda Feminina</h1>

        <h2>Realçando sua beleza com carinho e cuidado.</h2>

        <p>
            Um espaço pensado para você se cuidar, relaxar
            e valorizar ainda mais a sua beleza.
        </p>

        <a href="#agendamento" class="botao">
            Agendar meu horário
        </a>

    </div>

</section>


<!-- =====================================================
     SERVIÇOS
===================================================== -->

<section class="servicos" id="servicos">

    <div class="titulo">

        <h2>Cuidados para você</h2>

        <p>
            Momentos especiais de beleza e autocuidado.
        </p>

    </div>

    <div class="cards">

        <div class="card">

            <div class="icone">✨</div>

            <h3>Beleza</h3>

            <p>
                Cuidados pensados para realçar
                sua beleza natural.
            </p>

        </div>


        <div class="card">

            <div class="icone">🌸</div>

            <h3>Autocuidado</h3>

            <p>
                Um momento para você relaxar
                e cuidar de si mesma.
            </p>

        </div>


        <div class="card">

            <div class="icone">💗</div>

            <h3>Atendimento</h3>

            <p>
                Atendimento feminino com carinho,
                atenção e dedicação.
            </p>

        </div>

    </div>

</section>


<!-- =====================================================
     AGENDAMENTO
===================================================== -->

<section class="agendamento" id="agendamento">

    <div class="titulo">

        <h2>Agende seu horário</h2>

        <p>
            Escolha a data e o horário que deseja.
        </p>

    </div>


    <div class="agenda-container">

        <form method="POST" action="/agendar">

            <div>

                <label>
                    Seu nome
                </label>

                <input
                    type="text"
                    name="nome"
                    placeholder="Digite seu nome"
                    required
                >

            </div>


            <div>

                <label>
                    WhatsApp
                </label>

                <input
                    type="tel"
                    name="telefone"
                    placeholder="(34) 99988-2876"
                    required
                >

            </div>


            <div>

                <label>
                    Escolha a data
                </label>

                <input
                    type="date"
                    name="data"
                    required
                >

            </div>


            <div>

                <label>
                    Escolha o horário
                </label>

                <div class="horarios">

                    {% for horario in horarios %}

                        <label class="horario">

                            <input
                                type="radio"
                                name="horario"
                                value="{{ horario }}"
                                required
                            >

                            {{ horario }}

                        </label>

                    {% endfor %}

                </div>

            </div>


            <div>

                <label>
                    Observação
                </label>

                <input
                    type="text"
                    name="observacao"
                    placeholder="Alguma observação? (opcional)"
                >

            </div>


            <button
                type="submit"
                class="botao-agendar"
            >
                Solicitar agendamento
            </button>

        </form>


        <div class="aviso">

            <strong>💗 Importante:</strong>

            <br>

            Caso não encontre o horário que deseja,
            entre em contato conosco pelo WhatsApp.

            <br><br>

            Podemos verificar a disponibilidade de
            <strong>encaixes</strong> e outras possibilidades
            de horários.

        </div>

    </div>

</section>


<!-- =====================================================
     CONTATO
===================================================== -->

<section class="contato" id="contato">

    <div class="titulo">

        <h2>Entre em contato</h2>

        <p>
            Estamos à disposição para tirar suas dúvidas.
        </p>

    </div>


    <div class="contato-box">

        <p>
            📱 <strong>WhatsApp:</strong>
            (34) 99888-2876
        </p>

        <p>
            📸 <strong>Instagram:</strong>
            {{ instagram }}
        </p>

        <p>
            📍 <strong>Endereço:</strong>
            {{ endereco }}
        </p>


        <a
            class="botao whatsapp"
            href="https://wa.me/{{ whatsapp }}"
            target="_blank"
        >
            Falar pelo WhatsApp
        </a>

    </div>

</section>


<!-- =====================================================
     FOOTER
===================================================== -->

<footer>

    <p>
        © 2026 Fernanda Feminina
    </p>

    <p>
        Uberlândia - Minas Gerais
    </p>

</footer>


</body>

</html>
"""


# ============================================================
# ROTAS
# ============================================================

@app.route("/")
def inicio():

    return render_template_string(
        HTML,
        horarios=HORARIOS,
        whatsapp=WHATSAPP,
        instagram=INSTAGRAM,
        endereco=ENDERECO
    )


@app.route("/agendar", methods=["POST"])
def agendar():

    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    data = request.form.get("data")
    horario = request.form.get("horario")
    observacao = request.form.get("observacao")

    # ========================================================
    # AQUI VOCÊ PODE SALVAR O AGENDAMENTO EM UM BANCO DE DADOS
    # ========================================================

    print("\n==============================")
    print("NOVO AGENDAMENTO")
    print("==============================")
    print("Nome:", nome)
    print("Telefone:", telefone)
    print("Data:", data)
    print("Horário:", horario)
    print("Observação:", observacao)
    print("==============================\n")

    # Criando mensagem para WhatsApp

    mensagem = (
        f"Olá, Fernanda! Gostaria de solicitar um agendamento.%0A%0A"
        f"*Nome:* {nome}%0A"
        f"*Telefone:* {telefone}%0A"
        f"*Data:* {data}%0A"
        f"*Horário:* {horario}%0A"
        f"*Observação:* {observacao or 'Nenhuma'}"
    )

    whatsapp_url = f"https://wa.me/{WHATSAPP}?text={mensagem}"

    return f"""
    <script>
        window.location.href = "{whatsapp_url}";
    </script>
    """


# ============================================================
# INICIAR SERVIDOR
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)
