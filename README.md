# 🌳 Root Translation Project

Este repositório contém uma tradução **não oficial** do jogo **Root** para o português do Brasil. A tradução foi feita com a ajuda de um **GPT personalizado**, combinando tradução automática com revisão manual.

> **Nota Pessoal:**  
> Eu não sou tradutor profissional, e meu conhecimento de inglês é bem limitado. Decidi fazer essa tradução porque a língua inglesa era uma barreira que me impedia de aproveitar completamente o jogo. Foi um processo longo e trabalhoso, e, embora a tradução esteja funcional, ela pode conter erros e imprecisões.  
> Como não vou dispor de mais tempo para continuar ajustando e melhorando a tradução, estou deixando este repositório com todas as ferramentas e métodos utilizados. O objetivo é facilitar para qualquer pessoa interessada em continuar ou adaptar essa tradução, seja para português ou para outros idiomas.

---

## 📦 Instalar uma Tradução

### Via Release (Recomendado)

1. Acesse a seção de [Releases](https://github.com/luizera666/Root_Translate_Tools/releases) do repositório.
2. Baixe o arquivo compactado da tradução.
3. Extraia o arquivo compactado e substitua o arquivo **localization** original na pasta:

   `Root\Root_Data\StreamingAssets\Localization\win\`

4. Exclua o arquivo `game.cfg` na pasta:

   `Root\Root_Data\`

   Isso impedirá que o jogo baixe novamente os arquivos de localização originais.

5. Mude o idioma dentro do jogo para "Español". Esta tradução foi feita substituindo a tradução em Espanhol oficial do jogo, com o intuito de manter a tradução em Inglês. 
 

### Manualmente (Alternativo)

Se preferir, você pode seguir o tutorial completo para extrair, traduzir e reinserir as strings manualmente usando as ferramentas descritas abaixo.

---

## 🔧 Extraindo as Strings para Tradução

Para quem deseja criar novas traduções ou modificar as existentes, siga as instruções:

1. Abra o arquivo **localization** usando a ferramenta [UABEA](https://github.com/nesrak1/UABEA).
2. Selecione o arquivo de texto referente ao idioma que deseja usar como base (ex: `eu_US.txt`).
3. Vá até o menu `Plugins` e clique em `Export .txt`. Salve o arquivo exportado onde preferir.
4. Agora você pode editar o arquivo de texto livremente e traduzir as strings.

Para reinserir o arquivo traduzido:

1. No UABEA, selecione o arquivo **localization** novamente.
2. No menu `Plugins`, clique em `Import .txt` e escolha o arquivo traduzido.
3. Salve as alterações no asset bundle e, em seguida, salve o bundle modificado.

---

## 🛠️ Ferramentas

Na pasta `tools/stringeditor`, você encontrará uma ferramenta que facilita o processo de tradução, permitindo abrir arquivos de strings e editá-los diretamente em uma interface amigável. Para mais detalhes, consulte o [README da pasta stringeditor](./tools/stringeditor/README.md).

---

## 🌍 Colaborando com Novas Traduções

Se você deseja contribuir com traduções para outros idiomas, crie uma nova pasta dentro de `translate` seguindo a estrutura do diretório `pt_BR` como modelo. Insira tanto o arquivo de texto traduzido quanto o asset bundle modificado.

Se quiser colaborar diretamente com o repositório, fique à vontade para abrir uma **pull request**.

---

## 🔮 Possibilidades Futuras

Existe a possibilidade de que esta tradução funcione em outras plataformas do jogo, como Android e iOS, desde que os arquivos de localização encontrados em `StreamingAssets` tenham a mesma estrutura e chaves que os do Windows. Se você estiver interessado em testar e verificar isso, por favor, abra uma **issue** relatando seus resultados!

---

