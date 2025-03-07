# 💣 Campo Minado 🚩

## 🎮 Descrição do Projeto

Este projeto é uma implementação do clássico jogo **Campo Minado**, desenvolvido em Python utilizando a biblioteca `tkinter` para a interface gráfica. O objetivo do jogo é revelar todas as casas que **não contêm bombas**, evitando aquelas que estão minadas. O jogador pode marcar as casas que suspeita conterem bombas para ajudar na estratégia.

---

## 📜 Regras do Jogo

1. **Revelação de Casas**: O jogador deve clicar em uma casa para revelá-la. Se a casa estiver vazia, ela exibirá o número de bombas adjacentes.
2. **💣 Bombas**: Se o jogador revelar uma casa que contém uma bomba, o jogo termina e ele perde.
3. **🏆 Vitória**: O jogador vence o jogo quando todas as casas sem bombas são reveladas.
4. **🚩 Marcação de Bombas**: O jogador pode clicar com o botão direito do mouse para marcar uma casa que ele suspeita conter uma bomba. Isso ajuda a evitar cliques acidentais em casas minadas.

---

## 🕹️ Como Jogar

1. **Iniciar o Jogo**: Execute o arquivo `Main.py` para iniciar o jogo.
2. **Revelar Casas**: Clique com o botão **esquerdo** do mouse em uma casa para revelá-la.
3. **Marcar Bombas**: Clique com o botão **direito** do mouse para marcar uma casa que você suspeita conter uma bomba. Uma bandeirinha 🚩 será colocada.
4. **Contador de Bombas**: O contador de bombas restantes é exibido na área esquerda da tela.
5. **Fim do Jogo**: O jogo termina quando o jogador revela uma bomba 💣 ou quando todas as casas seguras são reveladas.

---

## 🛠️ Estrutura do Código

O projeto é composto pelos seguintes arquivos:

- **📄 Main.py**: Contém a lógica principal do jogo, incluindo a criação da interface gráfica e a inicialização das células do campo minado.
- **📄 utilidades.py**: Contém funções auxiliares para calcular a largura e altura da janela com base em porcentagens.
- **📄 celula.py**: Define a classe `Celula`, que representa cada casa do campo minado, incluindo a lógica de revelação, marcação e detecção de bombas.
- **📄 configurações.py**: Contém as configurações do jogo, como o tamanho da grade, largura e altura da janela, e o número de bombas.

---

## 👥 Autores

- **Dyego Nascimento Ferreira**
- **Gabriel Filipi Coelho**
- **Kayo Maldini**

---

## 🎨 Design e Estilo

O jogo foi projetado para ser visualmente atraente, com cores e ícones que remetem ao estilo clássico do Campo Minado:

- **💣 Bombas**: Quando uma bomba é revelada, a casa fica vermelha e exibe um ícone de bomba.
- **🚩 Bandeirinhas**: Casas marcadas como suspeitas de conter bombas são destacadas com uma cor laranja e um ícone de bandeira.
- **🎨 Cores**: As casas seguras reveladas têm cores suaves, enquanto as bombas e bandeiras são destacadas com cores vibrantes para facilitar a identificação.

---

## 🏁 Conclusão

Este projeto foi desenvolvido como parte de uma avaliação acadêmica, utilizando a linguagem Python e a biblioteca `tkinter` para criar uma interface gráfica simples e funcional. O jogo foi projetado para ser intuitivo e desafiador, seguindo as regras clássicas do Campo Minado. Durante o desenvolvimento, foram realizados testes para garantir o funcionamento correto do jogo, e o código foi organizado de forma modular para facilitar a manutenção e expansão futura.

Para jogar, basta executar o arquivo `Main.py` e seguir as instruções na tela. Boa sorte e divirta-se! 🎉

---

**🎮 Divirta-se e boa sorte no Campo Minado!** 💣🚩
