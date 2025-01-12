# 🛠️ Editor de Strings

Este diretório contém o **Editor de Strings**, uma ferramenta criada para facilitar o processo de tradução dos arquivos de texto do jogo **Root**.

## Funcionalidades

- Abrir arquivos de strings existentes para edição.
- Criar uma nova tradução a partir de um arquivo base.
- Interface intuitiva que exibe a chave, o texto original e a tradução lado a lado.
- Permite busca e navegação rápida entre as strings.
- Salvar o arquivo traduzido no formato correto para reinserção no asset bundle.

## Como Usar o Editor

1. Certifique-se de que já extraiu o arquivo de texto do asset bundle, conforme explicado no [README principal](../../README.md#-extraindo-as-strings-para-tradução).
2. Abra o programa `StringEditor.exe`.
3. Escolha entre:

   - **Nova Tradução**: Para iniciar uma tradução do zero.
   - **Abrir Tradução**: Para continuar uma tradução já iniciada.

4. Edite as strings conforme necessário.  
5. Salve o arquivo traduzido usando a opção **Salvar Tradução**.

---

## 🔄 Inserindo a Tradução no Asset Bundle

Depois de salvar sua tradução, você precisa reinserir o arquivo no asset bundle do jogo. Para isso:

1. Abra o arquivo **localization** no UABEA.  
2. No menu `Plugins`, clique em `Import .txt` e selecione o arquivo traduzido.  
3. Salve as alterações no asset bundle e, em seguida, salve o bundle modificado.

Para mais detalhes sobre extração e inserção, consulte o [README principal](../../README.md#-extraindo-as-strings-para-tradução).
