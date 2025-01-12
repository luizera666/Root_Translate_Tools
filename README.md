# 🌳 Root Translation Project

Este repositório contém uma tradução **não oficial** do jogo **Root** para o português do Brasil. A tradução foi feita com a ajuda de um **GPT personalizado**, combinando tradução automática com revisão manual.

> **Nota Pessoal:**  
> Eu não sou tradutor profissional, e meu conhecimento de inglês é bem limitado. Decidi fazer essa tradução porque a língua inglesa era uma barreira que me impedia de aproveitar completamente o jogo. Foi um processo longo e trabalhoso, e, embora a tradução esteja funcional, ela pode conter erros e imprecisões.  
> Como não vou dispor de mais tempo para continuar ajustando e melhorando a tradução, estou deixando este repositório com todas as ferramentas e métodos utilizados. O objetivo é facilitar para qualquer pessoa interessada em continuar ou adaptar essa tradução, seja para português ou para outros idiomas.

---

## 📦 Instalar uma Tradução

1. Navegue até a pasta `translate` no repositório.
2. Escolha a tradução desejada e baixe o arquivo **localization** correspondente.
3. Substitua o arquivo original localizado em:
   ```
   Root/Root_Data/StreamingAssets/Localization/win/localization
   ```
4. Para evitar que o jogo substitua automaticamente o arquivo traduzido por um original, exclua o seguinte arquivo de configuração:
   ```
   Root/Root_Data/game.cfg
   ```
   > Sem esse arquivo, o jogo não realizará a verificação de integridade online dos arquivos de localização.

---

## 🔧 Editor de Tradução

Este repositório também inclui um **editor de tradução com interface gráfica** desenvolvido para facilitar o processo de tradução e revisão.

### 🖥️ **Funcionalidades do Editor**

- Exibe as **chaves**, as **strings originais** (em inglês) e as **strings traduzidas** lado a lado.
- Permite a edição direta das strings.
- Possui um sistema de **busca avançada** com navegação entre resultados.
- Suporta a abertura de uma tradução em andamento ou a criação de uma nova tradução.
- Ao salvar, o editor valida automaticamente o número de chaves para evitar erros.

### ▶️ **Como Usar o Editor**

1. Execute o arquivo `editor_traducao.py`.
2. Escolha a opção:
   - **"Nova Tradução"**: Para iniciar uma tradução do zero.
   - **"Abrir Tradução"**: Para continuar uma tradução já iniciada.
3. Edite as strings conforme necessário.
4. Após finalizar, clique em **"Salvar Tradução"** e substitua o arquivo original.

---

## 🧩 **Como Extrair o Texto para Tradução**

Se você deseja iniciar uma nova tradução ou adaptar a existente para outra plataforma, siga este processo para extrair os textos:

1. **Localize o arquivo de localização**:
   O arquivo de localização pode ser encontrado no seguinte caminho na versão Windows:
   ```
   Root/Root_Data/StreamingAssets/Localization/win/localization
   ```
   
2. **Use a ferramenta [UABEA](https://github.com/nesrak1/UABEA):**
   - Abra o arquivo `localization` com a versão mais recente do **UABEA**.
   - Selecione o arquivo de texto que deseja extrair.
   - Vá em **Plugins > Export .txt** e salve o arquivo exportado.

3. **Edite livremente o arquivo extraído**:
   Agora você pode abrir o arquivo exportado e começar a tradução com o editor de tradução ou qualquer editor de texto.

### 🔄 **Como Reinserir o Texto Traduzido**

1. Após finalizar a tradução, abra novamente o **UABEA**.
2. Selecione o arquivo `localization` original.
3. Vá em **Plugins > Import .txt** e selecione o arquivo traduzido.
4. Salve as alterações e substitua o arquivo original pela nova versão.

---

## 🛠️ **Nota sobre a Tradução para Outras Plataformas**

Há uma possibilidade de que essa tradução funcione em outras plataformas onde o jogo **Root** está disponível, como **Android**, **iOS**, **PlayStation** e **Nintendo Switch**.

O principal ponto a ser verificado é se os arquivos de localização encontrados dentro da pasta `StreamingAssets` dessas plataformas possuem a **mesma quantidade de chaves** que o arquivo de localização da versão **Windows**. Se as chaves forem consistentes, é muito provável que a tradução funcione corretamente ao substituir o arquivo de localização.

### 💬 **Contribua com a Comunidade**

Caso tenha sucesso em adaptar a tradução para outras plataformas ou queira colaborar de outra forma, fique à vontade para abrir uma *issue* ou enviar um *pull request*. Toda ajuda é bem-vinda!

---
