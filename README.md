# 👁️ CountCam – Contador de Pessoas com Visão Computacional e IA

**CountCam** é um projeto de visão computacional que simula o funcionamento de uma câmera de segurança inteligente, capaz de contar automaticamente **quantas pessoas entram e saem de um ambiente**. A aplicação utiliza **OpenCV** para captura de vídeo e **MediaPipe Pose**, uma ferramenta de Inteligência Artificial desenvolvida pelo Google, para detectar poses humanas em tempo real.

---

## 🎯 Objetivo

O objetivo do projeto é resolver um problema comum do cotidiano: o controle do fluxo de pessoas em um local. Em vez de depender de sensores físicos ou contagem manual, a proposta utiliza uma webcam comum e inteligência artificial para detectar o movimento das pessoas e registrar se elas entraram ou saíram.

---

## 🧠 Técnicas de Inteligência Artificial

O projeto utiliza **MediaPipe Pose**, que emprega redes neurais profundas para detectar pontos do corpo humano (landmarks), como ombros, quadris, joelhos etc. O algoritmo identifica a posição dos **quadris** da pessoa e, com base na movimentação horizontal (eixo X), determina se a pessoa está entrando ou saindo do ambiente.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **OpenCV** – Captura e exibição de vídeo em tempo real
- **MediaPipe Pose** – Framework de IA para detecção de pose corporal

---

## 🧱 Como Funciona

1. O sistema inicia a captura da webcam.
2. Uma **linha vertical** é desenhada no centro da tela.
3. O código detecta os **pontos dos quadris** da pessoa usando IA.
4. Se a pessoa atravessa a linha da **esquerda para a direita**, é registrada uma **entrada**.
5. Se atravessa da **direita para a esquerda**, é registrada uma **saída**.
6. O contador é atualizado em tempo real e mostrado na tela.

---

## 📦 Instalação e Execução

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/CountCam.git
cd CountCam
